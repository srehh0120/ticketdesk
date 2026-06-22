# TicketDesk – AI Helpdesk Ticket Management System

TicketDesk is an AI-powered helpdesk ticket management system built using Flask, MySQL, and Groq LLMs. The application automates the initial ticket triage process by analyzing support requests, generating summaries, classifying issues, determining impact and urgency, assigning priorities, and routing tickets to the appropriate support team.

## Features
- AI-powered ticket classification
- Automatic priority assignment (P1–P4)
- Impact and urgency analysis
- Intelligent team routing
- Ticket lifecycle management
  - Open
  - In Progress
  - Resolved
  - Closed
- Team-specific dashboards
- Ticket history and details view
- MySQL database integration
- Flask-based web application


### AI Ticket Analysis

* Automatic ticket summarization
* Issue categorization
* Impact assessment
* Urgency assessment
* Team assignment

### Priority Matrix

Instead of allowing AI to directly assign priorities, TicketDesk uses a predefined priority matrix based on Impact and Urgency.

| Impact | Urgency | Priority |
| ------ | ------- | -------- |
| High   | High    | P1       |
| High   | Medium  | P2       |
| High   | Low     | P2       |
| Medium | High    | P2       |
| Medium | Medium  | P3       |
| Medium | Low     | P3       |
| Low    | High    | P3       |
| Low    | Medium  | P4       |
| Low    | Low     | P4       |

### Dashboard

* View all submitted tickets
* Priority statistics
* Impact and urgency tracking
* Priority filtering
* Ticket details page

### Ticket Details

Each ticket contains:

* Original ticket text
* AI-generated summary
* Category
* Impact
* Urgency
* Priority
* Assigned support team
* Timestamp

---
<img width="1888" height="868" alt="image" src="https://github.com/user-attachments/assets/096a5a4d-c85a-4b9a-be91-8f516182ecdd" />
<img width="1905" height="868" alt="image" src="https://github.com/user-attachments/assets/5f265d79-19cb-48c8-9fbd-dfa54cfd3eb7" />
<img width="1892" height="862" alt="image" src="https://github.com/user-attachments/assets/cc905c44-febe-439d-8d6f-e520529617f4" />


## Tech Stack

### Backend

* Python
* Flask

### Database

* MySQL

### AI

* Groq API
* Llama 3.3 70B Versatile

### Frontend

* HTML
* CSS
* JavaScript
* Jinja2 Templates

---

## Project Workflow

User submits a ticket

↓

AI analyzes the ticket

↓

Extracts:

* Summary
* Category
* Impact
* Urgency
* Assigned Team

↓

Priority Matrix

↓

Priority Generated (P1–P4)

↓

Stored in MySQL

↓

Displayed in Dashboard

---

## Example

### Input Ticket

Production database server is down. Customers cannot access services and business operations have stopped.

### AI Analysis

Summary:
Production database outage affecting customers.

Category:
Software Issue

Impact:
High

Urgency:
High

Assigned Team:
Database Support

Priority:
P1

---

## Installation

### Clone Repository

```bash
git clone https://github.com/srehh0120/ticketdesk.git
cd ticketdesk
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

### Run Application

```bash
python app.py
```

Open:

http://127.0.0.1:5000

---

## Learning Outcomes

* Flask Web Development
* MySQL Integration
* RESTful Design Principles
* AI API Integration
* Prompt Engineering
* Dashboard Development
* Priority Matrix Implementation
* Ticket Management Workflows

---

## Future Improvements

* Ticket Status Tracking
* AI Resolution Suggestions
* Search Functionality
* Analytics Dashboard
* PDF Report Export
* User Authentication
* SLA Monitoring

---

## Author

**Sreehari B**

B.Tech Computer Science & Engineering
College of Engineering Chengannur

GitHub: https://github.com/srehh0120
