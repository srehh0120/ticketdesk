from ai_utils import analyze_ticket

ticket = """
Laptop is running slow after Windows update.
Unable to open Outlook and Teams.
"""

result = analyze_ticket(ticket)

print(result)
print(result['summary'])