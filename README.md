# Expense Tracker 💰📊

An all-in-one desktop application built with Python to track personal expenses. It features a modern Tkinter GUI, uses a PostgreSQL database for reliable storage, and includes data synchronization, import/export (CSV/Excel), and data visualization (Pie Chart) capabilities.

## ✨ Features

* **Database Integration:** Stores all expense data in a PostgreSQL database for persistence and reliability.
* **JSON Fallback:** Automatically syncs data to a local `expenses.json` file for backup/manual inspection.
* **Modern GUI:** User-friendly interface built with the Tkinter library.
* **Expense Management:** Easily add new expenses with category and amount, and delete existing entries.
* **Search Functionality:** Filter expenses in the list by searching keywords in the category or amount.
* **Data Statistics:** Quick view of the minimum and maximum expense amounts and their categories.
* **Data Visualization:** Generate a **Pie Chart** using Matplotlib to visualize the distribution of expenses by category.
* **Data Import/Export:**
    * Export expenses to **CSV** and **Excel (.xlsx)** files.
    * Import expenses from **CSV** and **Excel (.xlsx)** files, seamlessly merging with existing database records.

## 🛠️ Prerequisites

Before running the application, ensure you have the following installed:

1.  **Python 3.x**
2.  A running **PostgreSQL** database instance.