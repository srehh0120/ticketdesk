from groq import Groq
from config import Config
import json

client = Groq(
    api_key=Config.GROQ_API_KEY
)
def calculate_priority(impact, urgency):

    matrix = {
        ("HIGH", "HIGH"): "P1",
        ("HIGH", "MEDIUM"): "P2",
        ("HIGH", "LOW"): "P2",
        ("MEDIUM", "HIGH"): "P2",
        ("MEDIUM", "MEDIUM"): "P3",
        ("MEDIUM", "LOW"): "P3",
        ("LOW", "HIGH"): "P3",
        ("LOW", "MEDIUM"): "P4",
        ("LOW", "LOW"): "P4"
    }

    return matrix.get(
        (impact.upper(), urgency.upper()),
        "P4"
    )
TEAM_MAP = {

    "Software Issue": "IT Operations",

    "Network Issue": "Network Team",

    "Security Issue": "Security Team",

    "Email Issue": "Email Support",

    "Finance Issue": "Finance",

    "HR Issue": "HR"

}

def analyze_ticket(ticket):

    prompt = f"""
You are an IT Helpdesk Analyst.

Analyze this support ticket.

Return ONLY raw JSON.

Do not use markdown.
Do not use ```json.
Do not add explanations.

{{
    "summary":"",
    "category":"",
    "impact":"",
    "urgency":"",
    "resolution":""
}}
Determine Impact:

        HIGH:
        - Entire company affected
        - Multiple departments affected
        - Business operations stopped
        - Customer-facing service unavailable

        MEDIUM:
        - Team or department affected
        - Important functionality unavailable

        LOW:
        - Single user affected
        - Minor inconvenience


Determine Urgency:

    HIGH:
    - Immediate attention required
    - Critical business deadlines affected

    MEDIUM:
    - Work can continue temporarily
    - Should be fixed soon

    LOW:
   - Can wait
    - Minimal business impact

Provide a short suggested resolution.

Requirements:
- Maximum 4 steps
- Practical IT troubleshooting steps
- Plain English
- Return as a single string
Category can be:
- Software Issue
- Hardware Issue
- Network Issue
- Security Issue
- Email Issue
Ticket:
{ticket}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    result= response.choices[0].message.content
    result = json.loads(result)
    print(result)
    impact=result['impact']
    urgency=result['urgency']
    result['priority']=calculate_priority(impact,urgency)
    result['team']=TEAM_MAP.get(result['category'],'IT Operations')
   #print(result['priority'])
    return result

