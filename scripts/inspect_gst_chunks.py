from app.rag.pdf_loader import load_pdf
from app.rag.chunker import chunk_gst_text


def main():
    pdf_path = "data/gst_docs/gst_master.pdf"
    source = "GST Master Document"

    pages = load_pdf(pdf_path)

    all_chunks = []
    for page in pages:
        chunks = chunk_gst_text(
            page.page_content,
            source=source,
        )
        all_chunks.extend(chunks)

    print(f"Total chunks created: {len(all_chunks)}\n")

    # Print first 10 chunks for inspection
    for i, chunk in enumerate(all_chunks[:10], start=1):
        print("=" * 80)
        print(f"Chunk {i}")
        print(f"Source  : {chunk['source']}")
        print(f"Section : {chunk['section']}")
        print("-" * 80)
        print(chunk["content"][:1500])  # limit output
        print()


if __name__ == "__main__":
    main()
