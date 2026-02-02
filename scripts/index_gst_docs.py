from app.rag.indexer import index_gst_pdf

if __name__ == "__main__":
    pdf_path = "data/gst_docs/gst_master.pdf"
    count = index_gst_pdf(pdf_path)
    print(f"✅ Indexed {count} GST chunks into Pinecone")
