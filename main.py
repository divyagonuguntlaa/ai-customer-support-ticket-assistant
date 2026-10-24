
from tools import analyze_ticket


def main():
    print("\n=== AI Customer Support Ticket Assistant ===")
    print("Describe the customer's issue below.")
    print("Enter a blank line when you finish.\n")

    lines = []

    while True:
        line = input()
        if not line.strip():
            break
        lines.append(line)

    complaint = "\n".join(lines).strip()

    if not complaint:
        print("Please enter a customer complaint.")
        return

    try:
        result = analyze_ticket(complaint)

        print("\n========== TICKET ANALYSIS ==========")
        print(f"\nCategory: {result.category}")
        print(f"Urgency: {result.urgency}")
        print(f"Sentiment: {result.sentiment}")

        print(f"\nSummary:\n{result.summary}")

        print("\nSuggested Customer Response:")
        print(result.suggested_response)

        print("\nRecommended Next Action:")
        print(result.recommended_action)

        print("\nAnalysis completed successfully.")

    except Exception as error:
        print(f"\nError: {error}")
        print(
            "Check your API key, internet connection, "
            "and available API credits."
        )


if __name__ == "__main__":
    main()
