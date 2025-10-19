import tkinter as tk
from tkinter import messagebox

FILENAME = "expenses.txt"


def read_expenses():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        return []


def add_expense():
    category = category_entry.get()
    amount = amount_entry.get()

    if not category or not amount:
        messagebox.showwarning("Қате", "Барлық өрісті толтырыңыз!")
        return

    try:
        amount = int(amount)
    except ValueError:
        messagebox.showerror("Қате", "Сома бүтін сан болуы керек!")
        return

    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(f"{category} - {amount} тг\n")

    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    update_listbox()
    messagebox.showinfo("✅", f"{category} қосылды!")


def delete_expense():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Қате", "Жою үшін элементті таңдаңыз!")
        return

    index = selected[0]
    expenses = read_expenses()
    deleted = expenses.pop(index)

    with open(FILENAME, "w", encoding="utf-8") as f:
        for line in expenses:
            f.write(line + "\n")

    update_listbox()
    messagebox.showinfo("🗑", f"{deleted} өшірілді!")


def show_total():
    total = 0
    expenses = read_expenses()
    for line in expenses:
        try:
            value = int(line.split('-')[1].replace('тг', '').strip())
            total += value
        except:
            pass
    messagebox.showinfo("💰 Жалпы сома", f"Барлығы: {total} тг")


def update_listbox():
    listbox.delete(0, tk.END)
    for exp in read_expenses():
        listbox.insert(tk.END, exp)


# --- Терезе ---
root = tk.Tk()
root.title("💼 Expense Tracker GUI")
root.geometry("400x400")
root.resizable(False, False)
# root.iconbitmap("icon.ico")

# --- UI элементтері ---
tk.Label(root, text="Категория:").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Label(root, text="Сома (тг):").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Button(root, text="Қосу", command=add_expense).pack(pady=5)
tk.Button(root, text="Жою", command=delete_expense).pack(pady=5)
tk.Button(root, text="Жалпы соманы көру", command=show_total).pack(pady=5)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

update_listbox()

root.mainloop()
