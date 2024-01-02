import tkinter as tk


def calculate_pension():
    # Parse the user input
    years_worked = int(entry_years_worked.get())
    highest_salary = float(entry_highest_salary.get())
    current_age = int(entry_current_age.get())
    increase_rate = float(entry_increase_rate.get()) / 100
    age_of_death = int(entry_age_of_death.get())

    # Check for invalid input
    if years_worked < 20:
        label_monthly_benefit.config(
            text="Invalid years worked (must be at least 20)")
        return
    if highest_salary < 0:
        label_monthly_benefit.config(
            text="Invalid highest salary (must be non-negative)")
        return
    if current_age <= 0:
        label_monthly_benefit.config(
            text="Invalid current age (must be positive)")
        return
    if increase_rate < 0:
        label_monthly_benefit.config(
            text="Invalid increase rate (must be non-negative)")
        return
    if age_of_death <= current_age:
        label_monthly_benefit.config(
            text="Invalid age of death (must be greater than current age)")
        return

    # Calculate the monthly benefit amount
    benefit_percentage = 0.5 + (years_worked - 20) * 0.025
    monthly_benefit = benefit_percentage * highest_salary / 12
    projected_benefit = monthly_benefit * \
        (1 + increase_rate) ** (current_age - 20)
    future_value = projected_benefit * \
        ((1 + increase_rate) ** (age_of_death - current_age))
    total_pension = monthly_benefit * 12 * (age_of_death - current_age)

    # Calculate the monthly benefit amount for the selected scenario
    # if scenario.get() == "20 years":
    #     benefit_percentage = 0.5 + (years_worked - 20) * 0.025
    # elif scenario.get() == "25 years":
    #     benefit_percentage = 0.5 + (years_worked - 20) * 0.03
    # elif scenario.get() == "30 years":
    #     benefit_percentage = 0.5 + (years_worked - 20) * 0.035
    # monthly_benefit = benefit_percentage * highest_salary
    # projected_benefit = monthly_benefit * \
    #     (1 + increase_rate) ** (current_age - 20)
    # future_value = projected_benefit * \
    #     ((1 + increase_rate) ** (age_of_death - current_age))
    # total_pension = monthly_benefit * 12 * (age_of_death - current_age)

    # Update the output fields
    label_monthly_benefit.config(
        text=f"Monthly benefit amount: ${monthly_benefit:,.2f}")
    label_projected_benefit.config(
        text=f"Projected monthly benefit at retirement age: ${projected_benefit:,.2f}")
    label_future_value.config(
        text=f"Projected future value based on CPI: ${future_value:,.2f}")
    label_total_pension.config(
        text=f"Total pension benefit: ${total_pension:,.2f}")


def clear_fields():
    # Clear the input fields
    entry_years_worked.delete(0, tk.END)
    entry_highest_salary.delete(0, tk.END)
    entry_current_age.delete(0, tk.END)
    entry_increase_rate.delete(0, tk.END)
    entry_age_of_death.delete(0, tk.END)

    # Clear the output fields
    label_monthly_benefit.config(text="Monthly benefit amount:")
    label_projected_benefit.config(
        text="Projected monthly benefit at retirement age:")
    label_future_value.config(text="Projected future value based on CPI:")
    label_total_pension.config(text="Total pension benefit:")


window = tk.Tk()
window.title("Firefighter Pension Calculator")


# Create the input fields and labels
label_years_worked = tk.Label(window, text="Years Worked:")
entry_years_worked = tk.Entry(window)
label_highest_salary = tk.Label(window, text="Highest Salary:")
entry_highest_salary = tk.Entry(window)
label_current_age = tk.Label(window, text="Current Age:")
entry_current_age = tk.Entry(window)
label_increase_rate = tk.Label(window, text="Percentage Increase per Year:")
entry_increase_rate = tk.Entry(window)
label_age_of_death = tk.Label(window, text="Age of Death:")
entry_age_of_death = tk.Entry(window)

# Create the output labels
label_monthly_benefit = tk.Label(window, text="Monthly benefit amount:")
label_projected_benefit = tk.Label(
    window, text="Projected monthly benefit at retirement age:")
label_future_value = tk.Label(
    window, text="Projected future value based on CPI:")
label_total_pension = tk.Label(window, text="Total pension benefit:")

# Create the buttons
button_calculate = tk.Button(
    window, text="Calculate", command=calculate_pension)
button_clear = tk.Button(window, text="Clear", command=clear_fields)

# Arrange the widgets on the window
label_years_worked.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_years_worked.grid(row=0, column=1, padx=10, pady=5)
label_highest_salary.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entry_highest_salary.grid(row=1, column=1, padx=10, pady=5)
label_current_age.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
entry_current_age.grid(row=2, column=1, padx=10, pady=5)
label_increase_rate.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
entry_increase_rate.grid(row=3, column=1, padx=10, pady=5)
label_age_of_death.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
entry_age_of_death.grid(row=4, column=1, padx=10, pady=5)

label_monthly_benefit.grid(row=5, column=0, padx=10, pady=5)
label_projected_benefit.grid(row=6, column=0, padx=10, pady=5)
label_future_value.grid(row=7, column=0, padx=10, pady=5)
label_total_pension.grid(row=8, column=0, padx=10, pady=5)

button_calculate.grid(row=9, column=0, padx=10, pady=5)
button_clear.grid(row=9, column=1, padx=10, pady=5)

# Start the main event loop
window.mainloop()
