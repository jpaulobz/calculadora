import tkinter as tk
from tkinter import ttk

class CurrencyExchangeCalculator:
    def __init__(self, active_users, max_credit_percent, min_credit_percent,
                 withdrawal_count, investment_count):
        self.active_users = active_users
        self.max_credit_percent = max_credit_percent
        self.min_credit_percent = min_credit_percent
        self.withdrawal_count = withdrawal_count
        self.investment_count = investment_count
        
    def calculate_exchange_rate(self):
        user_factor = 1 + self.active_users / 1000
        withdrawal_factor = 1 - self.withdrawal_count / 100
        investment_factor = 1 + self.investment_count / 100
        
        exchange_rate = user_factor * withdrawal_factor * investment_factor
        exchange_rate = max(self.min_credit_percent / 100, exchange_rate)
        exchange_rate = min(self.max_credit_percent / 100, exchange_rate)
        
        return exchange_rate

def calculate_button_clicked():
    active_users = int(active_users_entry.get())
    max_credit_percent = float(max_credit_percent_entry.get())
    min_credit_percent = float(min_credit_percent_entry.get())
    withdrawal_count = int(withdrawal_count_entry.get())
    investment_count = int(investment_count_entry.get())
    
    calculator = CurrencyExchangeCalculator(active_users, max_credit_percent,
                                            min_credit_percent, withdrawal_count,
                                            investment_count)
    
    exchange_rate = calculator.calculate_exchange_rate()
    result_label.config(text=f"Calculated exchange rate: {exchange_rate:.4f}")

# Create the main application window
root = tk.Tk()
root.title("Currency Exchange Calculator")

# Create and arrange input fields and labels
active_users_label = ttk.Label(root, text="Number of Active Users:")
active_users_label.pack()
active_users_entry = ttk.Entry(root)
active_users_entry.pack()

max_credit_percent_label = ttk.Label(root, text="Max Credit Percentage:")
max_credit_percent_label.pack()
max_credit_percent_entry = ttk.Entry(root)
max_credit_percent_entry.pack()

min_credit_percent_label = ttk.Label(root, text="Min Credit Percentage:")
min_credit_percent_label.pack()
min_credit_percent_entry = ttk.Entry(root)
min_credit_percent_entry.pack()

withdrawal_count_label = ttk.Label(root, text="Withdrawal Count:")
withdrawal_count_label.pack()
withdrawal_count_entry = ttk.Entry(root)
withdrawal_count_entry.pack()

investment_count_label = ttk.Label(root, text="Investment Count:")
investment_count_label.pack()
investment_count_entry = ttk.Entry(root)
investment_count_entry.pack()

calculate_button = ttk.Button(root, text="Calculate", command=calculate_button_clicked)
calculate_button.pack()

result_label = ttk.Label(root, text="")
result_label.pack()

# Start the GUI event loop
root.mainloop()
