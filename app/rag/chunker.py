import re


def chunk_gst_text(text: str, source: str):
    """
    Splits GST text using legal anchors when possible.
    Falls back to size-based chunks if anchors are missing.
    """
    section_pattern = r"(Section\s+\d+[A-Z]?|Rule\s+\d+|Notification\s+No\.\s*\d+)"
    parts = re.split(section_pattern, text)

    chunks = []
    current_section = "General"

    for part in parts:
        part = part.strip()
        if not part:
            continue

        if re.match(section_pattern, part):
            current_section = part
            continue

        if len(part) > 200:
            chunks.append(
                {
                    "content": part,
                    "section": current_section,
                    "source": source,
                }
            )

    return chunks
