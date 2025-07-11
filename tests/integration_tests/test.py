import time

from zai import ZaiClient

client = ZaiClient()  # Fill in your own API Key

response = client.videos.generations(
	model='cogvideo',
	prompt='一个年轻的艺术家在一片彩虹上用调色板作画。',
	# prompt="A cartoon fox dancing happily jazz in the forest."
	# prompt="This is a car commercial describing the racing adventure of a 30-year-old race car driver wearing a red helmet. The background is blue sky and harsh desert environment, filmed in cinematic style using 35mm film with vivid colors."
)
print(response)
task_id = response.id
task_status = response.task_status
get_cnt = 0

while task_status == 'PROCESSING' and get_cnt <= 40:
	result_response = client.videos.retrieve_videos_result(id=task_id)
	print(result_response)
	task_status = result_response.task_status

	time.sleep(2)
	get_cnt += 1
