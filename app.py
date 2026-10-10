from logger import logger
from flask import Flask, render_template, request, redirect, url_for, flash
from database import (
    create_table,
    add_expense,
    get_expenses,
    get_expense,
    update_expense,
    delete_expense
)

app = Flask(__name__)
app.secret_key = "expense-tracker-secret-key"

create_table()


@app.route("/")
def home():
    try:
        expenses = get_expenses()
        total = sum(expense["amount"] for expense in expenses)

        logger.info("Dashboard opened successfully")

        return render_template(
            "index.html",
            expenses=expenses,
            total=total
        )

    except Exception:
        logger.exception("Error loading dashboard")
        return "Something went wrong while loading expenses.", 500


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        try:
            title = request.form["title"].strip()
            amount = float(request.form["amount"])
            category = request.form["category"]
            expense_date = request.form["expense_date"]
            description = request.form["description"].strip()

            if not title:
                flash("Title is required!", "error")
                return redirect(url_for("add"))

            if amount <= 0:
                flash("Amount must be greater than 0!", "error")
                return redirect(url_for("add"))

            add_expense(
                title,
                amount,
                category,
                expense_date,
                description
            )

            flash("Expense added successfully!", "success")
            return redirect(url_for("home"))

        except ValueError:
            flash("Please enter a valid amount!", "error")
            return redirect(url_for("add"))

        except Exception as error:
            print("Error:", error)
            flash("Something went wrong!", "error")
            return redirect(url_for("add"))

    return render_template("add_expense.html")


@app.route("/edit/<int:expense_id>", methods=["GET", "POST"])
def edit(expense_id):
    expense = get_expense(expense_id)

    if not expense:
        flash("Expense not found!", "error")
        return redirect(url_for("home"))

    if request.method == "POST":
        try:
            title = request.form["title"].strip()
            amount = float(request.form["amount"])
            category = request.form["category"]
            expense_date = request.form["expense_date"]
            description = request.form["description"].strip()

            if not title:
                flash("Title is required!", "error")
                return redirect(url_for("edit", expense_id=expense_id))

            if amount <= 0:
                flash("Amount must be greater than 0!", "error")
                return redirect(url_for("edit", expense_id=expense_id))

            update_expense(
                expense_id,
                title,
                amount,
                category,
                expense_date,
                description
            )

            flash("Expense updated successfully!", "success")
            return redirect(url_for("home"))

        except ValueError:
            flash("Please enter a valid amount!", "error")
            return redirect(url_for("edit", expense_id=expense_id))

        except Exception as error:
            print("Error:", error)
            flash("Something went wrong!", "error")
            return redirect(url_for("edit", expense_id=expense_id))

    return render_template(
        "edit_expense.html",
        expense=expense
    )


@app.route("/delete/<int:expense_id>")
def delete(expense_id):
    try:
        deleted = delete_expense(expense_id)

        if deleted:
            flash("Expense deleted successfully!", "success")
        else:
            flash("Expense not found!", "error")

    except Exception as error:
        print("Error:", error)
        flash("Something went wrong!", "error")

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)