from zai import ZaiClient
import time
import json
import traceback

client = ZaiClient(
    base_url="",
    api_key=""
)


def file_parser_create_example(file_path, tool_type, file_type):
    """
    Example: Create a file parsing task
    """
    print("=== File Parser Create Example ===")
    with open(file_path, 'rb') as f:
        print("Submitting file parsing task ...")
        response = client.file_parser.create(
            file=f,
            file_type=file_type,
            tool_type=tool_type,
        )
        print("Task created successfully. Response:")
        print(response)
        # Usually you can get task_id
        task_id = getattr(response, "task_id", None)
        return task_id


def file_parser_content_example(task_id, format_type="download_link"):
    """
    Example: Get file parsing result
    """
    print("=== File Parser Content Example ===")
    try:
        print(f"Querying parsing result for task_id: {task_id}")
        response = client.file_parser.content(
            task_id=task_id,
            format_type=format_type
        )
        return response
    except Exception as err:
        print("Failed to get parsing result:", traceback.format_exc())
        return None


def file_parser_complete_example():
    """
    Full Example: Submit file for parsing, then poll until result is ready
    """
    # 1. Create parsing task
    # Please modify the local file path
    file_path = 'your file path'
    task_id = file_parser_create_example(file_path=file_path, tool_type="lite", file_type="pdf")
    if not task_id:
        print("Could not submit file for parsing.")
        return

    # 2. Poll to get the result
    max_wait = 60  # Wait up to 1 minute
    wait_time = 0
    while wait_time < max_wait:
        print(f"Waiting {wait_time}/{max_wait} seconds before querying result...")
        # format_type = text / download_link
        response = file_parser_content_example(task_id=task_id, format_type="download_link")

        result = response.json()
        if result.get("status") == "processing":
            print(result)

            time.sleep(5)
            wait_time += 5
        else:
            print(result)
            break
    print("File parser demo completed.")


if __name__ == "__main__":
    print("=== File Parsing Quick Demo ===\n")
    file_parser_complete_example()
