import asyncio
import os
import time

from zai import ZaiClient

# Try to load .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # If python-dotenv is not installed, continue using system environment variables
    pass

api_key = os.getenv('ZAI_API_KEY')
if not api_key:
    print("Please set the ZAI_API_KEY environment variable or configure it in the .env file")
    exit()

class VideoGenerator:
    def __init__(self, api_key: str):
        self.client = ZaiClient(api_key=api_key)

    async def video_generate(
        self,
        prompt: str,
        quality: str = 'speed',
        with_audio: bool = True,
        max_wait_time: int = 300,
    ):
        """
        Asynchronous video generation method

        Args:
            prompt: Video generation prompt
            quality: Output mode, "quality" for quality priority, "speed" for speed priority
            with_audio: Whether to include audio
            size: Video resolution, supports up to 4K (e.g., "3840x2160")
            fps: Frame rate, can be 30 or 60
            max_wait_time: Maximum wait time (seconds)

        Returns:
            Video generation result
        """
        try:
            # Submit generation task
            print('Submitting video generation task...')
            response = self.client.videos.generations(
                model='cogvideox-2',
                prompt=prompt,
                quality=quality,
                with_audio=with_audio,
            )

            print(f'Task submitted successfully, Task ID: {response.id}')
            print(f'Initial response: {response}')

            # Asynchronously wait for task completion
            task_id = response.id
            start_time = time.time()

            while True:
                # Check for timeout
                if time.time() - start_time > max_wait_time:
                    raise TimeoutError(f'Video generation timeout, exceeded {max_wait_time} seconds')

                # Get task result
                print(f'Querying task status... (waited {int(time.time() - start_time)} seconds)')
                result = self.client.videos.retrieve_videos_result(id=task_id)

                print(f'Task status: {result}')

                # Check if task is completed
                if hasattr(result, 'task_status'):
                    if result.task_status == 'SUCCESS':
                        print('Video generation completed!')
                        return result
                    elif result.task_status == 'FAIL':
                        raise Exception(f'Video generation failed: {result}')
                    elif result.task_status in ['PROCESSING', 'SUBMITTED']:
                        print(f'Task in progress, status: {result.task_status}')
                    else:
                        print(f'Unknown status: {result.task_status}')
                else:
                    # If no task_status field, check other possible status fields
                    print(f'Checking result structure: {result}')

                # Wait 5 seconds before querying again
                await asyncio.sleep(5)

        except Exception as e:
            print(f'Error occurred during video generation: {e}')
            raise


# Usage example
async def main():
    generator = VideoGenerator(api_key)
    try:
        result = await generator.video_generate(
            prompt='A beautiful sunset beach scene with a beautiful girl',
            quality='quality',
            with_audio=True,
        )
        print('\n=== Final Result ===')
        print(result)

    except Exception as e:
        print(f'Generation failed: {e}')


if __name__ == '__main__':
    asyncio.run(main())
