import os
import time
from zai import ZaiClient

def stream_web_search_example():
    print("=== GLM-4 Streaming Web Search Example ===")
    tools = [{
        "type": "web_search",
        "web_search": {
            "enable": "True",
            "search_engine": "search_pro",
            "search_result": "True",
            "search_prompt": "You are a financial analyst. Please concisely summarize the key information from the web search: {{search_result}}, rank by importance and mark the source date. The current date is April 11, 2025.",
            "count": "5",
            "search_domain_filter": "www.sohu.com",
            "search_recency_filter": "noLimit",
            "content_size": "high"
        }
    }]
    messages = [{
        "role": "user",
        "content": "Major financial events, policy changes, and market data in April 2025."
    }]
    client = ZaiClient()
    response = client.chat.completions.create(
        model="glm-4-air",
        messages=messages,
        tools=tools,
        stream=True
    )
    for chunk in response:
        print(chunk.choices[0].delta)

def sync_example():
    print("=== GLM-4 Synchronous Example ===")
    client = ZaiClient()
    response = client.chat.completions.create(
        model="glm-4-plus",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who provides professional, accurate, and insightful advice."},
            {"role": "user", "content": "I'm very interested in the planets of the solar system, especially Saturn. Please provide basic information about Saturn, including its size, composition, ring system, and any unique astronomical phenomena."},
        ]
    )
    print(response)

def async_example():
    print("=== GLM-4 Async Example ===")
    client = ZaiClient()
    response = client.chat.asyncCompletions.create(
        model="glm-4-plus",
        messages=[
            {
                "role": "user",
                "content": "As the king of fairy tales, please write a short fairy tale with the theme of always keeping a kind heart. The story should inspire children's interest in learning and imagination, and help them better understand and accept the morals and values contained in the story."
            }
        ],
    )
    print(response)
    return response.id

def async_result_example(task_id):
    print("=== GLM-4 Async Result Polling Example ===")
    task_status = ''
    get_cnt = 0
    client = ZaiClient()
    while task_status != 'SUCCESS' and task_status != 'FAILED' and get_cnt <= 40:
        result_response = client.chat.asyncCompletions.retrieve_completion_result(id=task_id)
        print(result_response)
        task_status = getattr(result_response, 'task_status', None)
        time.sleep(2)
        get_cnt += 1

def main():
    stream_web_search_example()
    print("\n" + "="*50 + "\n")
    sync_example()
    print("\n" + "="*50 + "\n")
    task_id = async_example()
    print("\n" + "="*50 + "\n")
    async_result_example(task_id)

if __name__ == "__main__":
    main() 