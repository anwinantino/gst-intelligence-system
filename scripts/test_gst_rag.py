from app.agents.gst_rag_agent import GSTRAGAgent


def main():
    agent = GSTRAGAgent()

    query = "What is the turnover limit for GST registration?"
    result = agent.answer(query)

    print("\nANSWER:\n", result.answer)
    print("\nSOURCES:")
    for s in result.sources:
        print("-", s)


if __name__ == "__main__":
    main()
