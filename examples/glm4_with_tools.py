from zai import ZaiClient
import json

client = ZaiClient()

# 定义天气查询函数
def get_weather(city: str) -> dict:
    """获取指定城市的天气信息"""
    # 这里应该调用真实的天气API
    weather_data = {
        "city": city,
        "temperature": "22°C",
        "condition": "晴天",
        "humidity": "65%",
        "wind_speed": "5 km/h"
    }
    return weather_data

# 函数描述格式
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "获取指定城市的当前天气信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名称，例如：北京、上海"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

# 发起对话请求
response = client.chat.completions.create(
    model="glm-4-plus",
    messages=[
        {"role": "user", "content": "北京今天天气怎么样？"}
    ],
    tools=tools,
    tool_choice="auto",
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content, end="", flush=True)

# 处理函数调用
message = response.choices[0].message
if message.tool_calls:
    for tool_call in message.tool_calls:
        if tool_call.function.name == "get_weather":
            # 解析参数
            args = json.loads(tool_call.function.arguments)
            city = args["city"]

            # 调用函数
            weather_result = get_weather(city)
            
            # 将结果返回给模型
            messages = [
                {"role": "user", "content": "北京今天天气怎么样？"},
                message,
                {
                    "role": "tool",
                    "content": json.dumps(weather_result, ensure_ascii=False),
                    "tool_call_id": tool_call.id
                }
            ]

            # 获取最终回答
            final_response = client.chat.completions.create(
                model="glm-4-plus",
                messages=messages,
                tools=tools,
                stream=True
            )
            
            for chunk in final_response:
                print(chunk.choices[0].delta.content, end="", flush=True)