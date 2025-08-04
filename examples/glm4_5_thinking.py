import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import time
import traceback
from typing import Optional

from example_types import MessageList, SamplerBase
from zai import ZhipuAiClient


class ZaiSampler(SamplerBase):
    """
    Sample from TGI's completion API
    """

    def __init__(
        self,
        model: str = "glm-4.5",
        api_key: str = '',
        system_message: Optional[str] = None,
        temperature: float = 0.0,
        max_tokens: int = 4096,
        stream: bool = False,
    ):
        self.system_message = system_message
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.model = model
        self.client = ZhipuAiClient(api_key=api_key)
        self.stream = stream
        
    def get_resp(self, message_list):
        for _ in range(3):
            try:
                chat_completion = self.client.chat.completions.create(
                    messages=message_list,
                    model=self.model,
                    temperature=self.temperature,
                    top_p=self.top_p,
                    max_tokens=self.max_tokens
                )
                output = chat_completion.choices[0].message.content
                return output
            except Exception as e:
                print(f"Exception: {e}\nTraceback: {traceback.format_exc()}")
                time.sleep(1)
                continue
        print(f"failed, last exception: {e if 'e' in locals() else ''}")
        return ''


    def get_resp_stream(self, message_list, top_p=-1, temperature=-1):
        temperature = temperature if temperature > 0 else self.temperature
        top_p = top_p if top_p > 0 else 0.95
        final = ''
        for _ in range(200):
            try:
                chat_completion_res = self.client.chat.completions.create(
                    model=self.model,
                    messages=message_list,
                    thinking={
                        "type": "enabled",
                    },
                    stream=True,
                    max_tokens=self.max_tokens,
                    temperature=temperature
                )
                for chunk in chat_completion_res:
                    if chunk.choices[0].delta.content:
                        final += chunk.choices[0].delta.content
                break
            except Exception as e:
                final = ""
                print(f"Exception: {e}\nTraceback: {traceback.format_exc()}")
                time.sleep(5)
                continue
            
        if final == '':
            print(f"failed in get_resp for 50 times, last exception: {e if 'e' in locals() else ''}")
            return ''
        
        content = ''
        if '</think>' in final:
            content = final.split("</think>")[-1].strip()
            if not content:
                content = final[-512:].strip()
        else:
            content = final[-512:].strip()
        
        return content
    
    def __call__(self, message_list: MessageList, top_p=0.95, temperature=0.6) -> str:
        if self.system_message:      
            message_list = [
                {
                    "role": "system", "content": self.system_message
                }
            ] + message_list

        if not self.stream:
            return self.get_resp(message_list, top_p, temperature)
        else:
            return self.get_resp_stream(message_list, top_p, temperature)
        

if __name__ == "__main__":
    client = ZaiSampler(model="glm-4.5", api_key=os.getenv("ZAI_API_KEY"), stream=True)
    messages = [
        {"role": "user", "content": "Hi?"},
    ]
    response = client(messages)
    print(response)