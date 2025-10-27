from zai import ZhipuAiClient

def main():
    client = ZhipuAiClient()
    # create chat completion with tool calls and streaming
    response = client.chat.completions.create(
        model="glm-4.6",
        messages=[
            {"role": "user", "content": "How is the weather in Beijing and Shanghai? Please provide the answer in Celsius."},
        ],
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "Get the weather information for a specific location",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {"type": "string", "description": "City, eg: Beijing, Shanghai"},
                            "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                        },
                        "required": ["location"]
                    }
                }
            }
        ],
        stream=True,  # enable streaming
        tool_stream=True  # enable tool call streaming
    )

    # init variables to collect streaming data
    reasoning_content = ""  # reasoning content
    content = ""  # response content
    final_tool_calls = {}  # tool call data
    reasoning_started = False  # is reasoning started
    content_started = False  # is content started

    # process streaming response
    for chunk in response:
        if not chunk.choices:
            continue

        delta = chunk.choices[0].delta

        # process streaming reasoning output
        if hasattr(delta, 'reasoning_content') and delta.reasoning_content:
            if not reasoning_started and delta.reasoning_content.strip():
                print("\n🧠 Thinking: ")
                reasoning_started = True
            reasoning_content += delta.reasoning_content
            print(delta.reasoning_content, end="", flush=True)

        # process streaming answer content output
        if hasattr(delta, 'content') and delta.content:
            if not content_started and delta.content.strip():
                print("\n\n💬 Answer: ")
                content_started = True
            content += delta.content
            print(delta.content, end="", flush=True)

        # process streaming tool call info
        if delta.tool_calls:
            for tool_call in delta.tool_calls:
                index = tool_call.index
                if index not in final_tool_calls:
                    # add new tool call
                    final_tool_calls[index] = tool_call
                    final_tool_calls[index].function.arguments = tool_call.function.arguments
                else:
                    # append tool call params by streaming index
                    final_tool_calls[index].function.arguments += tool_call.function.arguments

    # output the final construct tool call info
    if final_tool_calls:
        print("\n📋 Function Calls Triggered:")
        for index, tool_call in final_tool_calls.items():
            print(f"  {index}: Function Name: {tool_call.function.name}, Params: {tool_call.function.arguments}")

if __name__ == "__main__":
    main()