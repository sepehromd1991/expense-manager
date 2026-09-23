import tkinter as tk
import expense
window= tk.Tk()
window.title("Expense Manager")
label=tk.Label(window,text="Expense Manager")
label.pack()
result_label=tk.Label(window,text="")
result_label.pack()
def add_expense():
    new_window=tk.Toplevel(window)
    label=tk.Label(new_window,text="Add Expense")
    label.pack()
    label=tk.Label(new_window,text="Title:")
    label.pack()
    title_entry=tk.Entry(new_window)
    title_entry.pack()
    label=tk.Label(new_window,text="Amount:")
    label.pack()
    amount_entry=tk.Entry(new_window)
    amount_entry.pack()
    label=tk.Label(new_window,text="Category:")
    label.pack()
    category_entry=tk.Entry(new_window)
    category_entry.pack()
    message_label=tk.Label(new_window,text="")
    message_label.pack()
    def save():
        title=title_entry.get()
        if title=="":
            message_label.config(text="Title cannot be empty")
            return
        try:
            amount=int(amount_entry.get())
        except ValueError:
            message_label.config(text="Amount must be a number")
            return
        if amount <0:
            message_label.config(text="Amount cannot be negative")
            return
        category=category_entry.get()
        if category=="":
            message_label.config(text="Category cannot be empty")
            return
        expense.add_expense_data(title,amount,category)
        new_window.destroy()
    save_button=tk.Button(new_window,text="save",command=save)
    save_button.pack()
button1=tk.Button(window,text="Add Expense",command= add_expense)
button1.pack()
def show_expenses():
    if expense.expenses==[]:
        result_label.config(text="No expenses")
        return
    text=""
    for expense_item in expense.expenses:
        text=text+ f"Title:{expense_item['title']} | Amount:{expense_item['amount']} | Category:{expense_item['category']}\n"
    result_label.config(text=text)
button2=tk.Button(window,text="Show Expenses",command=show_expenses)
button2.pack()
def delete_expense():
    new_window=tk.Toplevel(window)
    label=tk.Label(new_window,text="Title:")
    label.pack()
    title_entry=tk.Entry(new_window)
    title_entry.pack()
    message_label=tk.Label(new_window,text="")
    message_label.pack()
    def delete():
        title=title_entry.get()
        found=False
        for expense_item in expense.expenses:
            if expense_item["title"].lower()==title.lower():
                found=True
                expense.expenses.remove(expense_item)
                expense.save_expenses()
                message_label.config(text="Expense deleted")
                break
        if not found:
            message_label.config(text="Expense not found")
    delete_button=tk.Button(new_window,text="Delete",command=delete)
    delete_button.pack()
button3=tk.Button(window,text="Delete Expense",command=delete_expense)
button3.pack()
def total_expense():
    if expense.expenses==[]:
        result_label.config(text="No expenses")
        return
    total=0
    for expense_item in expense.expenses:
        total=total + expense_item["amount"]
    result_label.config(text=f"total:{total}")
button4=tk.Button(window,text="Total Expenses",command=total_expense)
button4.pack()
def search_expense():
    new_window=tk.Toplevel(window)
    label=tk.Label(new_window,text="Title:")
    label.pack()
    title_entry=tk.Entry(new_window)
    title_entry.pack()
    result_search=tk.Label(new_window,text="")
    result_search.pack()
    def search():
        title=title_entry.get()
        found=False
        for expense_item in expense.expenses:
            if expense_item["title"].lower()==title.lower():
                found=True
                result_search.config(text=f"Title:{expense_item['title']} | Amount:{expense_item['amount']} | Category:{expense_item['category']}")
        if not found:
            result_search.config(text="Expense not found")        
    search_button=tk.Button(new_window,text="Search",command=search)
    search_button.pack()            
button5=tk.Button(window,text="Search Expense",command=search_expense)
button5.pack()
def edit_expense():
    new_window=tk.Toplevel(window)
    label=tk.Label(new_window,text="Current Title:")
    label.pack()
    title_entry=tk.Entry(new_window)
    title_entry.pack()
    label=tk.Label(new_window,text="New Title:")
    label.pack()
    new_title_entry=tk.Entry(new_window)
    new_title_entry.pack()
    label=tk.Label(new_window,text="New Amount:")
    label.pack()
    new_amount_entry=tk.Entry(new_window)
    new_amount_entry.pack()
    label=tk.Label(new_window,text="New Category:")
    label.pack()
    new_category_entry=tk.Entry(new_window)
    new_category_entry.pack()
    message_label=tk.Label(new_window,text="")
    message_label.pack()
    def edit():
        title=title_entry.get()
        found=False
        for expense_item in expense.expenses:
            if expense_item["title"].lower()==title.lower():
                found=True
                try:
                    new_amount=int(new_amount_entry.get())
                except ValueError:
                    message_label.config(text="Amount must be a number")
                    return
                if new_amount<0:
                    message_label.config(text="Amount cannot be negative")
                    return
                new_title=new_title_entry.get()
                if new_title=="":
                    message_label.config(text="Title cannot be empty")
                    return
                new_category=new_category_entry.get()
                if new_category=="":
                    message_label.config(text="Category cannot be empty")
                    return
                expense_item["amount"]=new_amount
                expense_item["title"]=new_title
                expense_item["category"]=new_category
                expense.save_expenses()
                message_label.config(text="Expense Edited")
                break
        if not found:
            message_label.config(text="Expense not found")    
    edit_button=tk.Button(new_window,text="Edit",command=edit)
    edit_button.pack()            
button6=tk.Button(window,text="Edit Expense",command=edit_expense)
button6.pack()
def total_category():
    new_window=tk.Toplevel(window)
    label=tk.Label(new_window,text="Category:")
    label.pack()
    category_entry=tk.Entry(new_window)
    category_entry.pack()
    message_label=tk.Label(new_window,text="")
    message_label.pack()
    def calculate():
        category=category_entry.get()
        total=0
        for expense_item in expense.expenses:
            if expense_item["category"].lower()==category.lower():
                total=total+expense_item["amount"]
                found=True
        if not found:
            message_label.config(text=f"total:{total}")
        else:
            message_label.config(text=f"total:{total}")
    calculate_button=tk.Button(new_window,text="Calculate",command=calculate)
    calculate_button.pack()
button7=tk.Button(window,text="Total Category",command=total_category)
button7.pack()
window.mainloop()