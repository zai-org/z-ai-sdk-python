import time
from zai import ZaiClient

# Async chat completions example: create task and poll result
# Prerequisite: set ZAI_API_KEY in your environment.


def create_async_task():
    """Create an async chat completion task and return its id."""
    client = ZaiClient()
    response = client.chat.asyncCompletions.create(
        model='glm-4.6',
        messages=[
            {
                "role": "user",
                "content": "Please write a short fairy tale about keeping a kind heart that encourages learning and imagination."
            }
        ]
    )
    print("Task created:", response)
    return response.id


def poll_result(task_id, interval_sec: int = 2, max_attempts: int = 40):
    """Poll the async task result until it succeeds or fails."""
    client = ZaiClient()
    attempt = 0
    status = ""
    while attempt < max_attempts:
        result = client.chat.asyncCompletions.retrieve_completion_result(id=task_id)
        print("Polling result:", result)
        status = getattr(result, "task_status", "") or ""
        # Handle different enum cases and capitalizations
        if status in ("SUCCESS", "FAIL"):
            if status in ("SUCCESS"):
                try:
                    content = result.choices[0].message.content
                except Exception:
                    content = None
                if content:
                    print("Final content:")
                    print(content)
            else:
                print("Task failed, status:", status)
            break
        time.sleep(interval_sec)
        attempt += 1
    else:
        print("Polling timed out, final status:", status)


def main():
    """Run the async task creation and polling demo."""
    task_id = create_async_task()
    poll_result(task_id)


if __name__ == "__main__":
    main()