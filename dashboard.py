import anthropic
import pandas as pd

API_KEY = "api_key_here"

grocery_file = r"C:\Users\George Ben\Downloads\Grocery_Shop_Data.xlsx"
steel_file = r"C:\Users\George Ben\Downloads\Steel_Company_Data.xlsx"

grocery_df = pd.read_excel(grocery_file, sheet_name="Monthly_Summary")
steel_df = pd.read_excel(steel_file, sheet_name="Monthly_Summary")

grocery_summary = grocery_df.tail(6).to_string()
steel_summary = steel_df.tail(6).to_string()

client = anthropic.Anthropic(api_key=API_KEY)

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": f"""
You are a business analyst. Analyze this data and give 5 bullet point insights. Use plain text only, no emojis, no markdown symbols like ** or ##. No numbering. Write each insight as a short paragraph separated by a blank line. Keep it concise.

GROCERY SHOP - Last 6 months:
{grocery_summary}

STAINLESS STEEL COMPANY - Last 6 months:
{steel_summary}

Give practical recommendations to improve sales and operations.
"""}
    ]
)

print("=== CLAUDE AI INSIGHTS ===")
print(message.content[0].text)

with open("insights.txt", "w", encoding="utf-8") as f:
    f.write(message.content[0].text)

print("\nInsights saved to insights.txt!")