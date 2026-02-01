"""
Layout Parsing Example

This example demonstrates how to use the layout_parsing API to parse
images and PDFs for OCR with detailed layout detection.

The API returns:
- Markdown formatted text
- Detailed layout information (element positions, types, content)
- Visualization images
"""
from zai import ZaiClient

def layout_parsing_example_with_url():
    """Example using an image URL for layout parsing."""
    client = ZaiClient(
        base_url=BASE_URL,
        api_key=API_KEY
    )

    # Image URL to parse
    image_url = "https://cdn.bigmodel.cn/static/platform/images/trialcenter/example/visual_img1.jpeg"

    print("=== Layout Parsing Example (URL) ===\n")
    print(f"Sending request to parse image: {image_url}")

    try:
        response = client.layout_parsing.create(
            model="glm-ocr",
            file=image_url,
            use_layout_details=True  # Get detailed layout info
        )

        print("\n✓ Request successful!")
        print(f"Task ID: {response.id}")
        print(f"Model: {response.model}")
        print(f"Created at: {response.created}")
        print(f"Request ID: {response.request_id}")

        # Print document info
        if response.data_info:
            print(f"\nDocument Info:")
            print(f"  - Total pages: {response.data_info.num_pages}")
            if response.data_info.pages:
                for i, page in enumerate(response.data_info.pages):
                    print(f"  - Page {i+1}: {page.width}x{page.height}")

        # Print markdown results
        print(f"\n=== Markdown Results ===\n")
        print(response.md_results)

        # Print layout details if available
        if response.layout_details:
            print(f"\n=== Layout Details ===")
            for page_idx, page_details in enumerate(response.layout_details):
                print(f"\nPage {page_idx + 1}:")
                for element in page_details:
                    print(f"  [{element.index}] {element.label}: {element.content[:50] if element.content else 'N/A'}...")
                    if element.bbox_2d:
                        print(f"       BBox: {element.bbox_2d}")

        # Print visualization URLs
        if response.layout_visualization:
            print(f"\n=== Visualization URLs ===")
            for i, url in enumerate(response.layout_visualization):
                print(f"  Page {i + 1}: {url}")

    except Exception as e:
        print(f"\n✗ Error: {e}")
        raise


def layout_parsing_example_with_base64():
    """Example using a base64 encoded image for layout parsing."""
    client = ZaiClient()

    print("\n=== Layout Parsing Example (Base64) ===\n")
    print("Note: Replace 'your_base64_encoded_image' with an actual base64 string")

    # Example with base64 (you would read and encode an actual image file)
    # import base64
    # with open("image.png", "rb") as f:
    #     base64_image = base64.b64encode(f.read()).decode("utf-8")
    #     base64_url = f"data:image/png;base64,{base64_image}"

    # For demonstration, this shows the API usage
    # Uncomment and use with actual base64 data:
    """
    response = client.layout_parsing.create(
        model="glm-ocr",
        file="data:image/jpeg;base64,/9j/4AAQ...",  # your base64 data
        use_layout_details=True
    )
    print(response.md_results)
    """
    print("(Skipping base64 example - no actual image data provided)")


def layout_parsing_example_with_pdf_pages():
    """Example using PDF with page range selection."""
    client = ZaiClient(
        base_url=BASE_URL,
        api_key=API_KEY
    )

    print("\n=== Layout Parsing Example (PDF with page range) ===\n")
    print("Note: Replace 'your_pdf_url' with an actual PDF URL")

    # For demonstration, this shows the API usage
    # Uncomment and use with actual PDF:
    """
    pdf_url = "https://example.com/document.pdf"

    response = client.layout_parsing.create(
        model="glm-ocr",
        file=pdf_url,
        use_layout_details=True,
        start_page_id=1,  # Start from page 1
        end_page_id=5,    # Parse up to page 5
        request_id="unique-request-id-123",  # Optional custom request ID
        user_id="user-456"  # Optional user ID for tracking
    )

    print(f"Parsed {response.data_info.num_pages} pages")
    print(response.md_results)
    """
    print("(Skipping PDF example - no actual PDF URL provided)")


if __name__ == "__main__":
    # Run the URL example with the test image
    layout_parsing_example_with_url()

    # Uncomment to run other examples:
    # layout_parsing_example_with_base64()
    # layout_parsing_example_with_pdf_pages()
