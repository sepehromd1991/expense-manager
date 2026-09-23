import json
def load_expenses():
    try:
        with open("expense.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
expenses=load_expenses()
def save_expenses():
    with open("expense.json","w") as file:
        json.dump(expenses,file,indent=4)
def add_expense():
    title=input("title:")
    if title=="":
        print("title cannot be empty")
        return
    try:
        amount=int(input("amount:"))
        if amount < 0:
            print("amount cannot be negative")
            return
    except ValueError:
        print("Please enter a number")
        return
    category=input("category:")
    if category=="":
        print("category cannot be empty")
        return
    expense={"title":title,"amount":amount,"category":category}
    expenses.append(expense)
    save_expenses()
def show_expense():
    if expenses==[]:
        print("no expenses")
        return
    for expense in expenses:
        print(f"Title {expense['title']} | Amount {expense['amount']} | Category {expense['category']}")
def total_expense():
    if expenses==[]:
        print("no expenses")
        return
    total=0
    for expense in expenses:
        total=total+expense["amount"]
    print("total:",total)   
def delete_expense():
    title=input("title:")
    found=False
    for expense in expenses:
        if expense["title"].lower()==title.lower():
            found=True
            expenses.remove(expense)
            save_expenses()
            print("delete")
            break
    if not found:
        print("not found")
def search_expense():
    title=input("title:")
    category=input("category:")
    found=False
    for expense in expenses:
        if title.lower() in expense["title"].lower() or category.lower() in expense["category"].lower():
            found=True
            print(expense["title"],expense["amount"],expense["category"])
    if not found:
        print("not found")
def total_category():
    category=input("category:")
    total=0
    found=False
    for expense in expenses:
        if expense["category"].lower()==category.lower():
            total=total+expense["amount"]
            found=True
    if not found:
        print("category not found")
        return
    print("total:",total)
def edit_expense():
    title=input("title:")
    found=False
    for expense in expenses:
        if expense["title"].lower()==title.lower():
            found=True
            try:
                new_amount=int(input("new_amount:"))
                if new_amount<0:
                    print("amount cannot be negative")
                    return
            except ValueError:
                print("please enter a number")
                return
            expense["amount"]=new_amount
            new_title=input("new_title:")
            if new_title=="":
                print("title cannot be empty")
                return
            new_category=input("new_category:")
            if new_category=="":
                print("category cannot be empty")
                return
            expense["title"]=new_title
            expense["category"]=new_category
            save_expenses()
            break
    if not found:
        print("not found")
def add_expense_data(title,amount,category):
    expense={"title":title,"amount":amount,"category":category}
    expenses.append(expense)
    save_expenses()
def show_menu():
    print("1.add")
    print("2.show")
    print("3.total")
    print("4.delete")
    print("5.search")
    print("6.total category")
    print("7.edit")
    print("8.exit")
def exit_expense():
    print("exit")
if __name__=="__main__":
    while True:
        show_menu()
        choice=input("choice:")
        if choice=="1":
            add_expense()
        elif choice=="2":
            show_expense()
        elif choice=="3":
            total_expense()
        elif choice=="4":
            delete_expense()
        elif choice=="5":
            search_expense()
        elif choice=="6":
            total_category()
        elif choice=="7":
            edit_expense()
        elif choice=="8":
            exit_expense()
            break
        else:
            print("invalid choice")