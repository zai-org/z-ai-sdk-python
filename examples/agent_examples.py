from zai import ZaiClient
import asyncio
import time

# ==================== General Translation Scenario ====================

def translate_text():
    """General translation example"""
    client = ZaiClient()
    response = client.agents.invoke(
        agent_id="general_translation",
        stream=True,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Hello, how are you today?"
                    }
                ]
            }
        ],
        custom_variables={
            "source_lang": "en",  # Source language: en(English), zh(Chinese), ja(Japanese), ko(Korean), fr(French), de(German), es(Spanish), ru(Russian), ar(Arabic), pt(Portuguese)
            "target_lang": "zh"   # Target language
        }
    )
    
    print("Translation result:")
    for chunk in response:
        print(chunk, end="", flush=True)
    print()

# ==================== Special Effects Video Generation Scenario ====================

async def async_special_effects_video_example():
        """
        Async special effects video generation example
        Includes result querying functionality
        """
        print("=== Async Special Effects Video Generation Example ===")
        
        # Submit async task
        print("Submitting async special effects video generation task...")
        client = ZaiClient()
        response = client.agents.invoke(
            agent_id="vidu_template_agent",
            custom_variables={
                "template": "french_kiss"
            },
            messages=[{
                "role": "user",
                "content": [{
                    "type": "text",
                    "text": "The two figures in the painting gradually approach each other, then kiss passionately, alternating with deep and firm intensity"
                }, {
                    "type": "image_url",
                    "image_url": "https://i0.sinaimg.cn/edu/2011/1125/U4999P42DT20111125164101.jpg"
                }]
            }]
        )
        print(response)
        
        # Get async task ID
        async_id = response.async_id
        if async_id:
            print(f"Async task ID: {async_id}")
            
            # Poll for results
            max_wait_time = 300  # Maximum wait time 5 minutes
            start_time = time.time()
            
            while True:
                if time.time() - start_time > max_wait_time:
                    print("Query timeout")
                    break
                
                print(f"Querying task status... (waited {int(time.time() - start_time)} seconds)")
                result = client.agents.async_result(
                    agent_id="vidu_template_agent",
                    async_id=async_id
                )
                
                # Check task status
                status = result.status
                if status == "success":
                    print("Special effects video generation completed!")
                    print(result)
                    break
                elif status == "failed":
                    print("Special effects video generation failed!")
                    break
                elif status in ["pending"]:
                    print(f"Task in progress, status: {status}")
                else:
                    print(f"Unknown status: {status}")
                
                # Wait 5 seconds before querying again
                await asyncio.sleep(5)
        else:
            print("Failed to get async task ID")

# ==================== Usage Examples ====================

async def main():
    print("=== Agent Quick Invocation Examples ===\n")
    
    # 1. General translation
    print("1. General translation example:")
    translate_text()
    
    print("\n" + "="*50 + "\n")
    
    # 2. Special effects video generation
    print("2. Special effects video generation example:")
    result = await async_special_effects_video_example()
    print(result)
    
    print("\n=== Examples completed ===") 

if __name__ == "__main__":
    asyncio.run(main())