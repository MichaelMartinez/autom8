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


# import tkinter for GUI interface

import tkinter as tk

# create main window
# ==================

root = tk.Tk()
root.title("Tucson Fire Pension Calculator")

# create labels for the input fields
# ==================================


age_label = tk.Label(root, text="Age")
dead_age_label = tk.Label(root, text="Age of Death")
highest_salary_label = tk.Label(root, text="Highest Salary")

# create entry fields for the input
# =================================


age_entry = tk.Entry(root)
dead_age_entry = tk.Entry(root)
highest_salary_entry = tk.Entry(root)

# pack the labels and entry fields onto the window
# ================================================


age_label.pack()
age_entry.pack()
dead_age_label.pack()
dead_age_entry.pack()
highest_salary_label.pack()
highest_salary_entry.pack()


hourly_wage_entry = tk.Entry(root)
hours_per_week_entry = tk.Entry(root)
weeks_per_year_entry = tk.Entry(root)
years_worked_entry = tk.Entry(root)

# pack the labels and entry fields onto the window
# ================================================
hourly_wage_label = tk.Label(root, text="Hourly Wage")
hours_per_week_label = tk.Label(root, text="Hours Worked Per Week")
weeks_per_year_label = tk.Label(root, text="Weeks Worked Per Year")
years_worked_label = tk.Label(root, text="Years Worked")

hourly_wage_label.pack()
hourly_wage_entry.pack()
hours_per_week_label.pack()
hours_per_week_entry.pack()
weeks_per_year_label.pack()
weeks_per_year_entry.pack()
years_worked_label.pack()
years_worked_entry.pack()

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
    age = int(age_entry.get())
    dead_age = int(dead_age_entry.get())
    highest_salary = float(highest_salary_entry.get())
    retirement_years = int(dead_age - age)

    # calculate the monthly benefit based on years of service and highest salary

    monthly_benefit = 0.025 * service_years * highest_salary / 12

    # calculate the total benefit based on monthly benefit and retirement years
    total_benefit = monthly_benefit * 12 * retirement_years
    # create a label to display the monthly benefit
    monthly_benefit_label = tk.Label(
        root, text="Monthly Benefit for 20 years: $%.2f" % monthly_benefit)
    monthly_benefit_label.pack()
    # create a label to display the total benefit
    total_benefit_label = tk.Label(
        root, text="Total Benefit: $%.2f over %d years" % (
            total_benefit, retirement_years)
    )
    total_benefit_label.pack()

    monthly_deposit = monthly_benefit

    # Initialize variables
    balance = 0.0
    interest_rate = 0.07
    num_of_years = 5
    num_of_months = num_of_years * 12

    # Calculate balance after 5 years
    for i in range(num_of_months):
        balance += monthly_deposit
        balance *= (1 + interest_rate/12)**(12/12)

    total_benefit_with_drop = total_benefit + balance
# Output the final balance
    print(f"After {num_of_years} years, your balance would be ${balance:.2f}")
    # create a label to display the drop amount
    drop_amount_label = tk.Label(
        root, text="Total with 5 years of Drop: $%.2f" % (
            total_benefit_with_drop)
    )
    drop_amount_label.pack()


    # create a button to calculate the pension benefit
    # ================================================
calculate_button = tk.Button(
    root, text="Calculate Benefit", command=calculate_pension)
calculate_button.pack()

# alternate scenarios where one retires without a drop and starts a new job
# ======================================================================


def calculate_pension_no_drop():
    # create new entry fields for the input
    # =================================
    # fields are hourly wage, hours worked per week, weeks worked per year, and years worked
    # create entry fields for the input
    # =================================
    global monthly_benefit, retirement_years, total_benefit, monthly_deposit, balance, interest_rate, num_of_years, num_of_months, monthly_wage, total_wage

    # calculate the dollar amount of the new job
    hourly_wage = float(hourly_wage_entry.get())
    hours_per_week = float(hours_per_week_entry.get())
    weeks_per_year = float(weeks_per_year_entry.get())
    years_worked = float(years_worked_entry.get())
    monthly_wage = hourly_wage * hours_per_week * 4
    total_wage = monthly_wage * 12 * years_worked

    # create a lable to display the monthly wage
    monthly_wage_label = tk.Label(
        root, text="Monthly Wage at menial job: $%.2f" % (monthly_wage))
    monthly_wage_label.pack()

    # create a label to display the total wage
    total_wage_label = tk.Label(
        root, text="Total Wage at menial job: $%.2f" % total_wage)
    total_wage_label.pack()
    is_it_worth_it()


# create button to calculate the new job
# =====================================
calculate_button_no_drop = tk.Button(
    root, text="Calculate New Job", command=calculate_pension_no_drop)
calculate_button_no_drop.pack()


def is_it_worth_it():
    global monthly_benefit, retirement_years, highest_salary, total_benefit, monthly_deposit, balance, interest_rate, num_of_years, num_of_months, monthly_wage, total_wage

    # calculate the difference between the two scenarios
    diff_monthly = monthly_benefit - monthly_wage

    # drop amount vs total wage
    diff_drop = balance - total_wage

    # monthly benefits for 25 years
    monthly_benefit_25 = 0.025 * 25 * highest_salary / 12
    # monthly benefits for 30 years
    monthly_benefit_30 = 0.025 * 30 * highest_salary / 12

    # calculate the total benefit based on monthly benefit and retirement years
    total_benefit = monthly_benefit * 12 * retirement_years
    # calculate the total benefit based on monthly benefit and retirement years
    total_benefit_25 = monthly_benefit_25 * 12 * retirement_years
    # calculate the total benefit based on monthly benefit and retirement years
    total_benefit_30 = monthly_benefit_30 * 12 * retirement_years

    diff_total_25 = total_benefit_25 - total_benefit
    diff_total_30 = total_benefit_30 - total_benefit

    # create a label to display the difference between the two scenarios
    # ================================================
    monthly_diff_label = tk.Label(
        root, text="Difference in Monthly Income: $%.2f" % diff_monthly)
    monthly_diff_label.pack()

    drop_diff_label = tk.Label(
        root, text="Difference in Drop Amount: $%.2f" % diff_drop)
    drop_diff_label.pack()

    total_benefit_25_label = tk.Label(
        root, text="Total Benefit for 25 Years service: $%.2f with %d years of retirement" % (total_benefit_25, retirement_years))
    total_benefit_25_label.pack()

    total_diff_25_label = tk.Label(
        root, text="Difference in Total Benefit for 25 Years service compared to 20: $%.2f" % diff_total_25)
    total_diff_25_label.pack()

    total_benefit_30_label = tk.Label(
        root, text="Total Benefit for 30 Years service: $%.2f with %d years of retirement" % (total_benefit_30, retirement_years))
    total_benefit_30_label.pack()

    total_diff_30_label = tk.Label(
        root, text="Difference in Total Benefit for 30 Years service compared to 20: $%.2f" % diff_total_30)
    total_diff_30_label.pack()


# calculate the difference between the two scenarios
# ================================================
# run the main loop
# =================
root.mainloop()
