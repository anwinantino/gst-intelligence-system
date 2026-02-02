from app.rag.pdf_loader import load_pdf
from app.rag.chunker import chunk_gst_text
from app.rag.indexer import index_chunks


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

    index_chunks(all_chunks)
    print(f"Ingested {len(all_chunks)} GST chunks.")


if __name__ == "__main__":
    main()
