from app.orchestrator.intent import classify_intent

if __name__ == "__main__":
    print(classify_intent("Store this invoice INV-002"))
    print(classify_intent("What is GST on laptops?"))
    print(classify_intent("Calculate GST for invoice INV-001"))

