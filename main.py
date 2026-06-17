import json
import os

FILE_NAME = "data.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def add_expense():
    try:
        amount = float(input("مبلغ را وارد کنید: "))
    except ValueError:
        print("خطا: مبلغ باید یک عدد باشد! لطفاً دوباره تلاش کنید.")
        return

    category = input("دسته‌بندی (مثلاً غذا، خرید، حمل‌ونقل): ")
    description = input("توضیحات: ")

    expenses = load_data()
    expenses.append({
        "amount": amount,
        "category": category,
        "description": description
    })
    save_data(expenُses)
    print("هزینه با موفقیت ذخیره شد!")


def view_expenses():
    expenses = load_data()

    if not expenses:
        print("هنوز هیچ هزینه‌ای ثبت نشده.")
        return

    print("\n--- لیست هزینه‌ها ---")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. مبلغ: {expense['amount']} | دسته: {expense['category']} | توضیح: {expense['description']}")

def show_total():
    expenses = load_data()
    total = sum(expense["amount"] for expense in expenses)
    print(f"جمع کل هزینه‌ها: {total}")

def menu():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. افزودن هزینه")
        print("2. نمایش هزینه‌ها")
        print("3. نمایش جمع کل")
        print("4. خروج")

        choice = input("یک گزینه انتخاب کنید: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("خروج از برنامه...")
            break
        else:
            print("گزینه نامعتبر است.")

menu()