from zai import ZaiClient

client = ZaiClient(
    base_url="",
    api_key=""
)


def handwriting_ocr_example():
    """
    Full Example: Submit image for recognition and wait for the result to be returned.
    """
    # Create recognition task
    # Please modify the local file path
    file_path = 'Your image path'
    with open(file_path, 'rb') as f:
        print("Submitting a handwriting recognition task ...")
        response = client.ocr.handwriting_ocr(
            file=f,
            tool_type="hand_write",
            probability=True
        )
        print("Task created successfully. Response:")
        print(response)

    print("Handwriting OCR demo completed.")


if __name__ == "__main__":
    print("=== Handwriting recognition quick demo ===\n")
    handwriting_ocr_example()
