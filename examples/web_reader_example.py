from zai import ZaiClient


def web_reader_example():
    client = ZaiClient()
    response = client.web_reader.web_reader(
        url="https://www.example.com/",
        return_format="markdown",  # or "text"
        retain_images=True,
        with_links_summary=True,
    )

    # Print full response model
    print(response)

    # Access structured fields
    if response.reader_result:
        data = response.reader_result
        print("Title:", data.title)
        print("Published:", data.published_time)
        print("URL:", data.url)
        print("Content length:", len(data.content or ""))


if __name__ == "__main__":
    web_reader_example()