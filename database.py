import sqlite3

DATABASE_NAME = "expenses.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            expense_date TEXT NOT NULL,
            description TEXT
        )
    """)

    connection.commit()
    connection.close()


def add_expense(title, amount, category, expense_date, description):
    connection = get_connection()

    cursor = connection.execute("""
        INSERT INTO expenses
        (title, amount, category, expense_date, description)
        VALUES (?, ?, ?, ?, ?)
    """, (title, amount, category, expense_date, description))

    connection.commit()
    expense_id = cursor.lastrowid
    connection.close()

    return expense_id


def get_expenses():
    connection = get_connection()

    expenses = connection.execute("""
        SELECT * FROM expenses
        ORDER BY expense_date DESC
    """).fetchall()

    connection.close()

    return [dict(expense) for expense in expenses]


def get_expense(expense_id):
    connection = get_connection()

    expense = connection.execute("""
        SELECT * FROM expenses
        WHERE id = ?
    """, (expense_id,)).fetchone()

    connection.close()

    if expense:
        return dict(expense)

    return None


def update_expense(
    expense_id,
    title,
    amount,
    category,
    expense_date,
    description
):
    connection = get_connection()

    cursor = connection.execute("""
        UPDATE expenses
        SET title = ?,
            amount = ?,
            category = ?,
            expense_date = ?,
            description = ?
        WHERE id = ?
    """, (
        title,
        amount,
        category,
        expense_date,
        description,
        expense_id
    ))

    connection.commit()
    updated = cursor.rowcount
    connection.close()

    return updated


def delete_expense(expense_id):
    connection = get_connection()

    cursor = connection.execute("""
        DELETE FROM expenses
        WHERE id = ?
    """, (expense_id,))

    connection.commit()
    deleted = cursor.rowcount
    connection.close()

    return deleted