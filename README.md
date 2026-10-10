# 💰 Expense Tracker

## Project Overview
Expense Tracker is a Python web application developed using Flask and SQLite. It helps users record, view, update, and delete their daily expenses while tracking total spending.

## Features
- Add new expenses
- View all expense records
- Edit existing expenses
- Delete expenses
- Calculate total expenses
- Categorize expenses
- Validate expense inputs
- Log application events and errors
- Display success and error messages

## Technology Stack
- Python
- Flask
- SQLite
- HTML
- CSS
- Python Logging

## Project Structure

```text
expense-tracker/
├── app.py
├── database.py
├── logger.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   ├── index.html
│   ├── add_expense.html
│   └── edit_expense.html
└── static/
    └── style.css
```

## Database Schema

The `expenses` table contains:

| Column | Description |
|---|---|
| id | Unique expense ID |
| title | Expense title |
| amount | Expense amount |
| category | Expense category |
| expense_date | Date of expense |
| description | Additional details |

## Setup Instructions

1. Install Python.
2. Clone or download the repository.
3. Create and activate a virtual environment.
4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the application:

```bash
python app.py
```

6. Open `http://127.0.0.1:5000` in your browser.

## Learning Outcomes

This project demonstrates Python web development, Flask routing, SQLite database integration, CRUD operations, input validation, exception handling, logging, and basic frontend development.

## Future Improvements
- User authentication
- Monthly expense reports
- Expense charts and analytics
- Cloud deployment

## Author
Sakshi Kumari