# This tinkter calculator gives estimates of how much a total benefit one will recieve
# from the tucson fire pension. It is based on years of service, age, and total highest salary.
# the calculator has 4 entry fields, one for years of service, one for age, one for
# highest salary, and one for years of retirement.
# 50% of the total highest salary is earned for 20 years of
# service, 62.5% of the total highest salary is earned for 25 years of service, 75% of the
# total highest salary is earned for 30 years of service. This should be calculated on a
# monthly basis based on total highest salary and 2.5% per year of service.
# The total benefit is the sum of the monthly benefits.
# The monthly benefit is calculated by multiplying the total highest salary by the
# percentage earned for the years of service. The monthly benefit is then multiplied by
# the number of months of retirement. The total benefit is the sum of the monthly
# benefits.


import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog

# create main window
# ==================

root = tk.Tk()
root.title("Tucson Fire Pension Calculator")

# create labels for the input fields
# ==================================

input_labels = ["Age", "Age of Death", "Highest Salary", "Hourly Wage", "Hours Worked Per Week", "Weeks Worked Per Year", "Years Worked"]
input_entries = []

for label in input_labels:
    input_label = tk.Label(root, text=label)
    input_label.pack()
    input_entry = tk.Entry(root)
    input_entry.pack()
    input_entries.append(input_entry)

# create a scrolling text box for output
# ======================================

output_box = scrolledtext.ScrolledText(root, width=110, height=30, wrap=tk.WORD)
output_box.pack()

#global variables
monthly_benefit = 0
total_benefit = 0
monthly_deposit = 0
balance = 0
interest_rate = 0
num_of_years = 0
num_of_months = 0
monthly_wage = 0
total_wage = 0
highest_salary = 0
retirement_years = 0

# create a function to calculate the pension benefit
# ==================================================

def calculate_pension():
    global monthly_benefit, retirement_years, highest_salary, total_benefit, monthly_deposit, balance, interest_rate, num_of_years, num_of_months, monthly_wage, total_wage
    # get the input values from the entry fields
    service_years = 20
    age = int(input_entries[0].get())
    dead_age = int(input_entries[1].get())
    highest_salary = float(input_entries[2].get())
    retirement_years = int(dead_age - age)

    # calculate the monthly benefit based on years of service and highest salary
    monthly_benefit = 0.025 * service_years * highest_salary / 12

    # calculate the total benefit based on monthly benefit and retirement years
    total_benefit = monthly_benefit * 12 * retirement_years
    
    # calculate the balance after 5 years with monthly deposit and interest rate
    monthly_deposit = monthly_benefit
    balance = 0.0
    interest_rate = 0.07
    num_of_years = 5
    num_of_months = num_of_years * 12
    for i in range(num_of_months):
        balance += monthly_deposit
        balance *= (1 + interest_rate/12)**(12/12)
    total_benefit_with_drop = total_benefit + balance
    
    # display the output in the scrolling text box
    output_box.delete('1.0', tk.END)
    output_box.insert(tk.INSERT, f"Monthly Benefit for 20 years: ${monthly_benefit:.2f}\n")
    output_box.insert(tk.INSERT, f"\n===================================================\n")
    output_box.insert(tk.INSERT, f"Total Benefit: ${total_benefit:.2f} over {retirement_years} years\n")
    output_box.insert(tk.INSERT, f"\n===================================================\n")
    output_box.insert(tk.INSERT, f"Total with 5 years of Drop: ${total_benefit_with_drop:.2f}\n")
    output_box.insert(tk.INSERT, f"\n===================================================\n")

def calculate_pension_no_drop():
    global monthly_benefit, retirement_years, total_benefit, monthly_deposit, balance, interest_rate, num_of_years, num_of_months, monthly_wage, total_wage
    hourly_wage = float(input_entries[3].get())
    hours_per_week = float(input_entries[4].get())
    weeks_per_year = float(input_entries[5].get())
    years_worked = float(input_entries[6].get())
    monthly_wage = hourly_wage * hours_per_week * 4
    total_wage = monthly_wage * 12 * years_worked
    # calculate the difference between the two scenarios
    
    diff_drop = balance - total_wage
    monthly_benefit_25 = 0.025 * 25 * highest_salary / 12
    monthly_benefit_30 = 0.025 * 30 * highest_salary / 12
    print(monthly_benefit)
    print(monthly_wage)
    print(monthly_benefit_25)
    job_plus_pension = monthly_benefit + monthly_wage
    diff_monthly = job_plus_pension - monthly_benefit_25
    total_benefit = monthly_benefit * 12 * retirement_years
    total_benefit_25 = monthly_benefit_25 * 12 * retirement_years
    total_benefit_30 = monthly_benefit_30 * 12 * retirement_years
    diff_total_25 = total_benefit_25 - total_benefit
    diff_total_30 = total_benefit_30 - total_benefit

    # display the output in the scrolling text box
    output_box.insert(tk.INSERT, f"\nMonthly Wage at menial job: ${monthly_wage:.2f}\n")
    output_box.insert(tk.INSERT, f"\n===================================================\n")
    output_box.insert(tk.INSERT, f"Total Wage at menial job: ${total_wage:.2f}\n after {years_worked} years\n")
    output_box.insert(tk.INSERT, f"\n===================================================\n")
    output_box.insert(tk.INSERT, f"Difference in Monthly Income between regular job + pension (${monthly_wage:.2f} + {monthly_benefit:.2f}) and staying on FD until 25 years ({monthly_benefit_25:.2f}): ${diff_monthly:.2f}\n")
    output_box.insert(tk.INSERT, f"\n===================================================\n")
    output_box.insert(tk.INSERT, f"Difference in 5 years at drop (${balance:.2f}) and wages earned working ({total_wage}): ${diff_drop:.2f}\n")
    output_box.insert(tk.INSERT, f"\n===================================================\n")
    output_box.insert(tk.INSERT, f"Total Benefit for 25 Years service: ${total_benefit_25:.2f} with {retirement_years} years of retirement\n")
    output_box.insert(tk.INSERT, f"\n===================================================\n")
    output_box.insert(tk.INSERT, f"Difference in Total Benefit for 25 Years service compared to 20: ${diff_total_25:.2f}\n")
    output_box.insert(tk.INSERT, f"\n===================================================\n")
    output_box.insert(tk.INSERT, f"Total Benefit for 30 Years service: ${total_benefit_30:.2f} with {retirement_years} years of retirement\n")
    output_box.insert(tk.INSERT, f"\n===================================================\n")
    output_box.insert(tk.INSERT, f"Difference in Total Benefit for 30 Years service compared to 20: ${diff_total_30:.2f}\n")

#create buttons to calculate the pension benefits
#================================================
calculate_button = tk.Button(root, text="Calculate Benefit", command=calculate_pension)
calculate_button.pack()

calculate_button_no_drop = tk.Button(root, text="Calculate New Job", command=calculate_pension_no_drop)
calculate_button_no_drop.pack()

#create a function to save the output to a markdown file
#======================================================
def save_output():
    # open a file dialog to select the file to save to
    file_path = filedialog.asksaveasfilename(defaultextension=".md")
    # write the output to the file
    with open(file_path, "w") as f:
        f.write(output_box.get("1.0", tk.END))

#create a button to save the output to a markdown file
#====================================================
save_button = tk.Button(root, text="Save Output", command=save_output)
save_button.pack()

#run the main loop
#=================
root.mainloop()
