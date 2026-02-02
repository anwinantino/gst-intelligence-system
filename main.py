import sys
from app.orchestrator.runner import run_orchestrator


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"<your query>\"")
        sys.exit(1)

    query = sys.argv[1]
    response = run_orchestrator(query)

    print("\n================= ANSWER =================\n")
    print(response)
    print("\n==========================================\n")


if __name__ == "__main__":
    main()
