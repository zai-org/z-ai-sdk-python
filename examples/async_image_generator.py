import asyncio
import time

from zai import ZaiClient


class AsyncImageGenerator:
    def __init__(self):
        self.client = ZaiClient()

    async def generate_image(
        self,
        prompt: str,
        model: str = 'glm-image',
        size: str = None,
        quality: str = None,
        max_wait_time: int = 300,
    ):
        """
        Asynchronous image generation method

        Args:
            prompt: Image generation prompt
            model: Model to use for image generation
            size: Size of the generated image
            quality: Quality level of the generated image
            max_wait_time: Maximum wait time (seconds)

        Returns:
            Image generation result
        """
        try:
            # Submit generation task
            print('Submitting image generation task...')
            response = self.client.images.async_generations(
                model=model,
                prompt=prompt,
                size=size,
                quality=quality,
            )

            print(f'Task submitted successfully, Task ID: {response.id}')
            print(f'Initial response: {response}')

            # Asynchronously wait for task completion
            task_id = response.id
            start_time = time.time()

            while True:
                # Check for timeout
                if time.time() - start_time > max_wait_time:
                    raise TimeoutError(f'Image generation timeout, exceeded {max_wait_time} seconds')

                # Get task result
                print(f'Querying task status... (waited {int(time.time() - start_time)} seconds)')
                result = self.client.images.retrieve_images_result(id=task_id)

                print(f'Task status: {result.task_status}')

                # Check if task is completed
                if result.task_status == 'SUCCESS':
                    print('Image generation completed!')
                    return result
                elif result.task_status == 'FAIL':
                    raise Exception(f'Image generation failed: {result}')
                elif result.task_status in ['PROCESSING']:
                    print(f'Task in progress, status: {result.task_status}')
                else:
                    print(f'Unknown status: {result.task_status}')

                # Wait 3 seconds before querying again
                await asyncio.sleep(30)

        except Exception as e:
            print(f'Error occurred during image generation: {e}')
            raise


# Usage example
async def main():
    generator = AsyncImageGenerator()
    try:
        result = await generator.generate_image(
            prompt='A beautiful sunset over the ocean with colorful clouds',
            model='glm-image',
        )
        print('\n=== Final Result ===')
        print(f'Task Status: {result.task_status}')
        print(f'Request ID: {result.request_id}')
        if result.image_result:
            for i, img in enumerate(result.image_result):
                print(f'Image {i + 1} URL: {img.url}')

    except Exception as e:
        print(f'Generation failed: {e}')


if __name__ == '__main__':
    asyncio.run(main())
