import asyncio
import os
import time
from typing import List, Optional

from zai import ZaiClient

class VideoModelsExamples:
    def __init__(self):
        self.client = ZaiClient()

    async def cogvideox3_text_to_video(
        self,
        prompt: str,
        quality: str = "quality",
        with_audio: bool = True,
        size: str = "1920x1080",
        fps: int = 30,
        max_wait_time: int = 300,
    ):
        """
        cogvideox-3 text-to-video generation
        
        Args:
            prompt: Video generation prompt
            quality: Output mode, "quality" for quality priority, "speed" for speed priority
            with_audio: Whether to include audio
            size: Video resolution, supports up to 4K (e.g., "3840x2160")
            fps: Frame rate, can be 30 or 60
            max_wait_time: Maximum wait time (seconds)
        """
        print("=== cogvideox-3 Text-to-Video ===")
        try:
            response = self.client.videos.generations(
                model="cogvideox-3",
                prompt=prompt,
                quality=quality,
                with_audio=with_audio,
                size=size,
                fps=fps,
            )
            return await self._wait_for_completion(response.id, max_wait_time)
        except Exception as e:
            print(f"cogvideox-3 text-to-video failed: {e}")
            raise

    async def cogvideox3_image_to_video(
        self,
        image_url: str,
        prompt: str,
        quality: str = "quality",
        with_audio: bool = True,
        size: str = "1920x1080",
        fps: int = 30,
        max_wait_time: int = 300,
    ):
        """
        cogvideox-3 image-to-video generation
        
        Args:
            image_url: Image URL or Base64 encoding
            prompt: Video generation prompt
            quality: Output mode, "quality" for quality priority, "speed" for speed priority
            with_audio: Whether to include audio
            size: Video resolution, supports up to 4K (e.g., "3840x2160")
            fps: Frame rate, can be 30 or 60
            max_wait_time: Maximum wait time (seconds)
        """
        print("=== cogvideox-3 Image-to-Video ===")
        try:
            response = self.client.videos.generations(
                model="cogvideox-3",
                image_url=image_url,
                prompt=prompt,
                quality=quality,
                with_audio=with_audio,
                size=size,
                fps=fps,
            )
            return await self._wait_for_completion(response.id, max_wait_time)
        except Exception as e:
            print(f"cogvideox-3 image-to-video failed: {e}")
            raise

    async def cogvideox3_start_end_video(
        self,
        image_urls: List[str],
        prompt: str,
        quality: str = "quality",
        with_audio: bool = True,
        size: str = "1920x1080",
        fps: int = 30,
        max_wait_time: int = 300,
    ):
        """
        cogvideox-3 start-end frame video generation
        
        Args:
            image_urls: List of start and end frame image URLs
            prompt: Video generation prompt
            quality: Output mode, "quality" for quality priority, "speed" for speed priority
            with_audio: Whether to include audio
            size: Video resolution, supports up to 4K (e.g., "3840x2160")
            fps: Frame rate, can be 30 or 60
            max_wait_time: Maximum wait time (seconds)
        """
        print("=== cogvideox-3 Start-End Frame Video ===")
        try:
            response = self.client.videos.generations(
                model="cogvideox-3",
                image_url=image_urls,
                prompt=prompt,
                quality=quality,
                with_audio=with_audio,
                size=size,
                fps=fps,
            )
            return await self._wait_for_completion(response.id, max_wait_time)
        except Exception as e:
            print(f"cogvideox-3 start-end frame video failed: {e}")
            raise

    async def cogvideox2_text_to_video(
        self,
        prompt: str,
        quality: str = "speed",
        with_audio: bool = True,
        max_wait_time: int = 300,
    ):
        """
        cogvideox-2 text-to-video generation
        
        Args:
            prompt: Video generation prompt
            quality: Output mode, "quality" for quality priority, "speed" for speed priority
            with_audio: Whether to include audio
            max_wait_time: Maximum wait time (seconds)
        """
        print("=== cogvideox-2 Text-to-Video ===")
        try:
            response = self.client.videos.generations(
                model="cogvideox-2",
                prompt=prompt,
                quality=quality,
                with_audio=with_audio,
            )
            return await self._wait_for_completion(response.id, max_wait_time)
        except Exception as e:
            print(f"cogvideox-2 text-to-video failed: {e}")
            raise

    async def viduq1_text_to_video(
        self,
        prompt: str,
        style: str = "general",
        duration: int = 5,
        aspect_ratio: str = "16:9",
        size: str = "1920x1080",
        movement_amplitude: str = "auto",
        max_wait_time: int = 300,
    ):
        """
        viduq1-text text-to-video generation
        Args:
            prompt: Video generation prompt
            style: Video style (e.g., "general", "anime")
            duration: Video duration in seconds
            aspect_ratio: Aspect ratio (e.g., "16:9")
            size: Video resolution
            movement_amplitude: Movement amplitude (e.g., "auto")
            quality: Output mode
            with_audio: Whether to include audio
            max_wait_time: Maximum wait time (seconds)
        """
        print("=== viduq1-text Text-to-Video ===")
        try:
            response = self.client.videos.generations(
                model="viduq1-text",
                prompt=prompt,
                style=style,
                duration=duration,
                aspect_ratio=aspect_ratio,
                size=size,
                movement_amplitude=movement_amplitude,
            )
            return await self._wait_for_completion(response.id, max_wait_time)
        except Exception as e:
            print(f"viduq1-text text-to-video failed: {e}")
            raise

    async def viduq1_image_to_video(
        self,
        image_url: str,
        prompt: str,
        duration: int = 5,
        size: str = "1920x1080",
        movement_amplitude: str = "auto",
        max_wait_time: int = 300,
    ):
        """
        viduq1-image image-to-video generation
        Args:
            image_url: Image URL or Base64 encoding
            prompt: Video generation prompt
            duration: Video duration in seconds
            size: Video resolution
            movement_amplitude: Movement amplitude (e.g., "auto")
            quality: Output mode
            with_audio: Whether to include audio
            max_wait_time: Maximum wait time (seconds)
        """
        print("=== viduq1-image Image-to-Video ===")
        try:
            response = self.client.videos.generations(
                model="viduq1-image",
                image_url=image_url,
                prompt=prompt,
                duration=duration,
                size=size,
                movement_amplitude=movement_amplitude,
            )
            return await self._wait_for_completion(response.id, max_wait_time)
        except Exception as e:
            print(f"viduq1-image image-to-video failed: {e}")
            raise

    async def viduq1_start_end_video(
        self,
        image_urls: List[str],
        prompt: str,
        duration: int = 5,
        size: str = "1920x1080",
        movement_amplitude: str = "auto",
        max_wait_time: int = 300,
    ):
        """
        viduq1-start-end start-end frame video generation
        Args:
            image_urls: List of start and end frame image URLs
            prompt: Video generation prompt
            duration: Video duration in seconds
            size: Video resolution
            movement_amplitude: Movement amplitude (e.g., "auto")
            quality: Output mode
            with_audio: Whether to include audio
            max_wait_time: Maximum wait time (seconds)
        """
        print("=== viduq1-start-end Start-End Frame Video ===")
        try:
            response = self.client.videos.generations(
                model="viduq1-start-end",
                image_url=image_urls,
                prompt=prompt,
                duration=duration,
                size=size,
                movement_amplitude=movement_amplitude,
            )
            return await self._wait_for_completion(response.id, max_wait_time)
        except Exception as e:
            print(f"viduq1-start-end start-end frame video failed: {e}")
            raise

    async def vidu2_image_to_video(
        self,
        image_url: str,
        prompt: str,
        duration: int = 4,
        size: str = "1280x720",
        movement_amplitude: str = "auto",
        max_wait_time: int = 300,
    ):
        """
        vidu2-image image-to-video generation
        Args:
            image_url: Image URL or Base64 encoding
            prompt: Video generation prompt
            duration: Video duration in seconds
            size: Video resolution
            movement_amplitude: Movement amplitude (e.g., "auto")
            with_audio: Whether to include audio
            quality: Output mode
            max_wait_time: Maximum wait time (seconds)
        """
        print("=== vidu2-image Image-to-Video ===")
        try:
            response = self.client.videos.generations(
                model="vidu2-image",
                image_url=image_url,
                prompt=prompt,
                duration=duration,
                size=size,
                movement_amplitude=movement_amplitude,
            )
            return await self._wait_for_completion(response.id, max_wait_time)
        except Exception as e:
            print(f"vidu2-image image-to-video failed: {e}")
            raise

    async def vidu2_start_end_video(
        self,
        image_urls: List[str],
        prompt: str,
        duration: int = 4,
        size: str = "1280x720",
        movement_amplitude: str = "auto",
        max_wait_time: int = 300,
    ):
        """
        vidu2-start-end start-end frame video generation
        Args:
            image_urls: List of start and end frame image URLs
            prompt: Video generation prompt
            duration: Video duration in seconds
            size: Video resolution
            movement_amplitude: Movement amplitude (e.g., "auto")
            with_audio: Whether to include audio
            quality: Output mode
            max_wait_time: Maximum wait time (seconds)
        """
        print("=== vidu2-start-end Start-End Frame Video ===")
        try:
            response = self.client.videos.generations(
                model="vidu2-start-end",
                image_url=image_urls,
                prompt=prompt,
                duration=duration,
                size=size,
                movement_amplitude=movement_amplitude,
            )
            return await self._wait_for_completion(response.id, max_wait_time)
        except Exception as e:
            print(f"vidu2-start-end start-end frame video failed: {e}")
            raise

    async def vidu2_reference_video(
        self,
        image_url: List[str],
        prompt: str,
        duration: int = 4,
        aspect_ratio: str = "16:9",
        size: str = "1280x720",
        movement_amplitude: str = "auto",
        max_wait_time: int = 300,
        with_audio: bool = True,
    ):
        """
        vidu2-reference reference video generation
        Args:
            image_url: Reference image URLs
            prompt: Video generation prompt
            duration: Video duration in seconds
            aspect_ratio: Aspect ratio (e.g., "16:9")
            size: Video resolution
            movement_amplitude: Movement amplitude (e.g., "auto")
            with_audio: Whether to include audio
            quality: Output mode
            max_wait_time: Maximum wait time (seconds)
        """
        print("=== vidu2-reference Reference Video Generation ===")
        try:
            response = self.client.videos.generations(
                model="vidu2-reference",
                image_url=image_url,
                prompt=prompt,
                duration=duration,
                aspect_ratio=aspect_ratio,
                size=size,
                movement_amplitude=movement_amplitude,
                with_audio=with_audio,
            )
            return await self._wait_for_completion(response.id, max_wait_time)
        except Exception as e:
            print(f"vidu2-reference reference video generation failed: {e}")
            raise

    async def _wait_for_completion(self, task_id: str, max_wait_time: int = 300):
        """
        Common method to wait for task completion
        """
        start_time = time.time()
        
        while True:
            # Check for timeout
            if time.time() - start_time > max_wait_time:
                raise TimeoutError(f"Video generation timeout, exceeded {max_wait_time} seconds")

            # Get task result
            print(f"Querying task status... (waited {int(time.time() - start_time)} seconds)")
            result = self.client.videos.retrieve_videos_result(id=task_id)

            print(f"Task status: {result}")

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


# Usage examples
async def main():
    # Please fill in your API Key
    examples = VideoModelsExamples()

    # Sample image and video URLs (please replace with actual URLs)
    sample_image_url = "https://i0.sinaimg.cn/edu/2011/1125/U4999P42DT20111125164101.jpg"
    sample_first_frame = "https://gd-hbimg.huaban.com/ccee58d77afe8f5e17a572246b1994f7e027657fe9e6-qD66In_fw1200webp"
    sample_last_frame = "https://gd-hbimg.huaban.com/cc2601d568a72d18d90b2cc7f1065b16b2d693f7fa3f7-hDAwNq_fw1200webp"
    ref_image_url = [
        "https://gd-hbimg.huaban.com/ccee58d77afe8f5e17a572246b1994f7e027657fe9e6-qD66In_fw1200webp", 
        "https://gd-hbimg.huaban.com/cc2601d568a72d18d90b2cc7f1065b16b2d693f7fa3f7-hDAwNq_fw1200webp", 
        "https://gd-hbimg.huaban.com/cc2601d568a72d18d90b2cc7f1065b16b2d693f7fa3f7-hDAwNq_fw1200webp"
        ]

    try:
        # 1. cogvideox-3 text-to-video
        print("\n" + "="*50)
        result1 = await examples.cogvideox3_text_to_video(
            prompt="Peter Rabbit driving a car, wandering on the road, with a happy and joyful expression on his face.",
            quality="quality",
            with_audio=True,
            size="1920x1080",
            fps=30,
        )
        print("cogvideox-3 text-to-video result:", result1)

        # 2. cogvideox-3 image-to-video
        print("\n" + "="*50)
        result2 = await examples.cogvideox3_image_to_video(
            image_url=sample_image_url,
            prompt="Make the scene come alive",
            quality="quality",
            with_audio=True,
            size="1920x1080",
            fps=30,
        )
        print("cogvideox-3 image-to-video result:", result2)

        # 3. cogvideox-3 start-end frame video
        print("\n" + "="*50)
        result3 = await examples.cogvideox3_start_end_video(
            image_urls=[sample_first_frame, sample_last_frame],
            prompt="Make the scene come alive",
            quality="speed",
            with_audio=True,
            size="1920x1080",
            fps=30,
        )
        print("cogvideox-3 start-end frame video result:", result3)

        # 4. cogvideox-2 text-to-video
        print("\n" + "="*50)
        result4 = await examples.cogvideox2_text_to_video(
            prompt="Peter Rabbit driving a car, wandering on the road, with a happy and joyful expression on his face.",
            quality="speed",
            with_audio=True,
        )
        print("cogvideox-2 text-to-video result:", result4)

        # 5. viduq1-text text-to-video
        print("\n" + "="*50)
        print(os.environ.get("ZAI_API_KEY"))
        result5 = await examples.viduq1_text_to_video(
            prompt="Peter Rabbit driving a car, wandering on the road, with a happy and joyful expression on his face.",
            style="general",
            duration=5,
            aspect_ratio="16:9",
            size="1920x1080",
            movement_amplitude="auto",
        )
        print("viduq1-text text-to-video result:", result5)

        # 6. viduq1-image image-to-video
        print("\n" + "="*50)
        result6 = await examples.viduq1_image_to_video(
            image_url=sample_image_url,
            prompt="Peter Rabbit driving a car, wandering on the road, with a happy and joyful expression on his face.",
            duration=5,
            size="1920x1080",
            movement_amplitude="auto",
        )
        print("viduq1-image image-to-video result:", result6)

        # 7. viduq1-start-end start-end frame video
        print("\n" + "="*50)
        result7 = await examples.viduq1_start_end_video(
            image_urls=[sample_first_frame, sample_last_frame],
            prompt="Peter Rabbit driving a car, wandering on the road, with a happy and joyful expression on his face.",
            duration=5,
            size="1920x1080",
            movement_amplitude="auto",
        )
        print("viduq1-start-end start-end frame video result:", result7)

        # 8. vidu2-image image-to-video
        print("\n" + "="*50)
        result8 = await examples.vidu2_image_to_video(
            image_url=sample_image_url,
            prompt="Peter Rabbit driving a car, wandering on the road, with a happy and joyful expression on his face.",
            duration=4,
            size="1280x720",
            movement_amplitude="auto",
        )
        print("vidu2-image image-to-video result:", result8)

        # 9. vidu2-start-end start-end frame video
        print("\n" + "="*50)
        result9 = await examples.vidu2_start_end_video(
            image_urls=[sample_first_frame, sample_last_frame],
            prompt="Peter Rabbit driving a car, wandering on the road, with a happy and joyful expression on his face.",
            duration=4,
            size="1280x720",
            movement_amplitude="auto",
        )
        print("vidu2-start-end start-end frame video result:", result9)

        # 10. vidu2-reference reference video generation
        print("\n" + "="*50)
        result10 = await examples.vidu2_reference_video(
            image_url=ref_image_url,
            prompt="Peter Rabbit driving a car, wandering on the road, with a happy and joyful expression on his face.",
            duration=4,
            aspect_ratio="16:9",
            size="1280x720",
            movement_amplitude="auto",
            with_audio=True,
        )
        print("vidu2-reference reference video generation result:", result10)
    except Exception as e:
        print(f"Video generation failed: {e}")
        raise e
    finally:
        print("\n=== Examples completed ===") 

if __name__ == "__main__":
    asyncio.run(main())