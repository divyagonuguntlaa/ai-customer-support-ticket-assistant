
import os
from openai import OpenAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class SupportAnalysis(BaseModel):
    category: str = Field(
        description="Category of the customer issue"
    )
    urgency: str = Field(
        description="One of Low, Medium, High, or Critical"
    )
    sentiment: str = Field(
        description="Customer sentiment: Positive, Neutral, or Negative"
    )
    summary: str
    suggested_response: str
    recommended_action: str


def analyze_ticket(complaint: str) -> SupportAnalysis:
    response = client.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI customer support assistant. "
                    "Analyze customer complaints and produce "
                    "structured support recommendations. "
                    "Choose a category such as Billing, Account Access, "
                    "Technical Issue, Subscription, or Other. "
                    "Urgency must be Low, Medium, High, or Critical. "
                    "Use Critical only for severe, time-sensitive cases. "
                    "Identify sentiment, summarize the issue, draft a "
                    "polite response, and recommend a next action. "
                    "Never claim an issue has been fixed or a refund "
                    "has been processed. Do not request passwords, "
                    "payment card numbers, or authentication codes."
                ),
            },
            {
                "role": "user",
                "content": f"Customer complaint:\n{complaint[:10000]}",
            },
        ],
        response_format=SupportAnalysis,
    )

    result = response.choices[0].message.parsed

    if result is None:
        raise ValueError("The AI could not analyze this ticket.")

    return result
