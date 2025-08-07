from zai import ZhipuAiClient
import json
client = ZhipuAiClient()

def get_flight_number(date: str, departure: str, destination: str):
    flight_number = {
        "Beijing": {
            "Shanghai": "1234",
            "Guangzhou": "5678",
        },
        "Shanghai": {
            "Beijing": "4321",
            "Guangzhou": "8765",
        }
    }
    return {"flight_number": flight_number[departure][destination]}

def get_ticket_price(date: str, flight_number: str):
    return {"ticket_price": "1000"}

def parse_function_call(model_response, messages):
    # Handle function call results. According to the model's returned parameters, call the corresponding function.
    # After getting the function result, construct a tool message and call the model again, passing the function result as input.
    # The model will return the function result to the user in natural language.
    if model_response.choices[0].message.tool_calls:
        tool_call = model_response.choices[0].message.tool_calls[0]
        args = tool_call.function.arguments
        function_result = {}
        if tool_call.function.name == "get_flight_number":
            function_result = get_flight_number(**json.loads(args))
        if tool_call.function.name == "get_ticket_price":
            function_result = get_ticket_price(**json.loads(args))
        messages.append({
            "role": "tool",
            "content": f"{json.dumps(function_result)}",
            "tool_call_id": tool_call.id
        })
        response = client.chat.completions.create(
            model="glm-4",  # Specify the model name to use
            messages=messages,
            tools=tools,
        )
        print(response.choices[0].message)
        messages.append(response.choices[0].message)

messages = []
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_flight_number",
            "description": "Query the flight number for a given date, departure, and destination",
            "parameters": {
                "type": "object",
                "properties": {
                    "departure": {
                        "description": "Departure city",
                        "type": "string"
                    },
                    "destination": {
                        "description": "Destination city",
                        "type": "string"
                    },
                    "date": {
                        "description": "Date",
                        "type": "string",
                    }
                },
                "required": ["departure", "destination", "date"]
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_ticket_price",
            "description": "Query the ticket price for a specific flight on a specific date",
            "parameters": {
                "type": "object",
                "properties": {
                    "flight_number": {
                        "description": "Flight number",
                        "type": "string"
                    },
                    "date": {
                        "description": "Date",
                        "type": "string",
                    }
                },
                "required": ["flight_number", "date"]
            },
        }
    },
]

# Clear conversation
messages = []
messages.append({"role": "system", "content": "Do not assume or guess the values of function parameters. If the user's description is unclear, ask the user to provide the necessary information."})
messages.append({"role": "user", "content": "Help me check the flights from Beijing to Guangzhou on January 23."})

response = client.chat.completions.create(
    model="glm-4",  # Specify the model name to use
    messages=messages,
    tools=tools,
)
print(response.choices[0].message)
messages.append(response.choices[0].message)

parse_function_call(response, messages)

messages.append({"role": "user", "content": "What is the price of flight 8321?"})
response = client.chat.completions.create(
    model="glm-4",  # Specify the model name to use
    messages=messages,
    tools=tools,
)
print(response.choices[0].message)
messages.append(response.choices[0].message)

parse_function_call(response, messages)