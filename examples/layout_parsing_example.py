"""
Layout Parsing Example

This example demonstrates how to use the layout_parsing API to parse
images and PDFs for OCR with detailed layout detection.
"""
from zai import ZaiClient

def layout_parsing_example_with_url():
    """Example using an image URL for layout parsing."""
    client = ZaiClient()

    # Image URL to parse
    image_url = "https://cdn.bigmodel.cn/static/platform/images/trialcenter/example/visual_img1.jpeg"

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


if __name__ == "__main__":
    # Run the URL example with the test image
    layout_parsing_example_with_url()
