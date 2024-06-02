import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Function to calculate monthly mortgage payment
def calculate_monthly_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    num_payments = years * 12
    monthly_payment = (
        principal
        * (monthly_rate * (1 + monthly_rate) ** num_payments)
        / ((1 + monthly_rate) ** num_payments - 1)
    )
    return monthly_payment


# Function to generate amortization schedule
def generate_amortization_schedule(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    num_payments = years * 12
    monthly_payment = calculate_monthly_payment(principal, annual_rate, years)
    balance = principal
    amortization_schedule = []

    for month in range(1, num_payments + 1):
        interest_payment = balance * monthly_rate
        principal_payment = monthly_payment - interest_payment
        balance -= principal_payment
        amortization_schedule.append(
            (month, monthly_payment, principal_payment, interest_payment, balance)
        )

    return pd.DataFrame(
        amortization_schedule,
        columns=[
            "Month",
            "Monthly Payment",
            "Principal Payment",
            "Interest Payment",
            "Remaining Balance",
        ],
    )


# Parameters
home_price_down_payment = 450000  # Home price in the down payment scenario
down_payment_amount = 90000  # Down payment amount
home_price_no_down_payment = 450000  # Home price in the no down payment scenario
annual_interest_rate_down_payment = (
    6.0  # Annual interest rate for down payment scenario
)
annual_interest_rate_no_down_payment = (
    6.0  # Annual interest rate for no down payment scenario
)
loan_term_years = 30  # Loan term in years
homeowners_insurance = 1800  # Homeowners insurance annual lump sum

# Calculate loan amounts
loan_amount_down_payment = home_price_down_payment - down_payment_amount
loan_amount_no_down_payment = home_price_no_down_payment

# Calculate monthly mortgage payments
monthly_payment_down_payment = calculate_monthly_payment(
    loan_amount_down_payment, annual_interest_rate_down_payment, loan_term_years
)
monthly_payment_no_down_payment = calculate_monthly_payment(
    loan_amount_no_down_payment, annual_interest_rate_no_down_payment, loan_term_years
)

# Calculate assessed values and property taxes
assessed_value_down_payment = home_price_down_payment * 0.10
assessed_value_no_down_payment = home_price_no_down_payment * 0.10
property_tax_down_payment = assessed_value_down_payment * 0.10
property_tax_no_down_payment = assessed_value_no_down_payment * 0.10

# Calculate monthly property taxes and homeowners insurance
monthly_property_tax_down_payment = property_tax_down_payment / 12
monthly_property_tax_no_down_payment = property_tax_no_down_payment / 12
monthly_homeowners_insurance = homeowners_insurance / 12

# Calculate total monthly payments including taxes and insurance
total_monthly_payment_down_payment = (
    monthly_payment_down_payment
    + monthly_property_tax_down_payment
    + monthly_homeowners_insurance
)
total_monthly_payment_no_down_payment = (
    monthly_payment_no_down_payment
    + monthly_property_tax_no_down_payment
    + monthly_homeowners_insurance
)

# Generate amortization schedules
schedule_down_payment = generate_amortization_schedule(
    loan_amount_down_payment, annual_interest_rate_down_payment, loan_term_years
)
schedule_no_down_payment = generate_amortization_schedule(
    loan_amount_no_down_payment, annual_interest_rate_no_down_payment, loan_term_years
)

# Calculate the extra monthly cost for the no down payment scenario
extra_monthly_cost = (
    total_monthly_payment_no_down_payment - total_monthly_payment_down_payment
)

# Calculate cumulative extra payments over time
months = np.arange(1, loan_term_years * 12 + 1)
cumulative_extra_payments = extra_monthly_cost * months

# Find the break-even point
break_even_point = np.argmax(cumulative_extra_payments >= down_payment_amount)

# Create output directory
output_dir = "purchase_calculations"
os.makedirs(output_dir, exist_ok=True)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(
    months,
    cumulative_extra_payments,
    label="Cumulative Extra Payments (No Down Payment Scenario)",
)
plt.axhline(
    y=down_payment_amount,
    color="r",
    linestyle="--",
    label=f"Down Payment Amount: ${down_payment_amount}",
)
plt.axvline(
    break_even_point,
    color="g",
    linestyle="--",
    label=f"Break-even Point: {break_even_point} months",
)
plt.xlabel("Months")
plt.ylabel("Cumulative Extra Payments ($)")
plt.title("Cumulative Extra Payments vs Down Payment Amount")
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(output_dir, "cumulative_extra_payments_450.png"))
plt.show()

# Display the break-even point
print(
    f"Break-even point: {break_even_point} months, or {break_even_point // 12} years and {break_even_point % 12} months."
)

# Save amortization schedules as markdown tables
schedule_down_payment_markdown = schedule_down_payment.head(24).to_markdown(index=False)
schedule_no_down_payment_markdown = schedule_no_down_payment.head(24).to_markdown(
    index=False
)

with open(
    os.path.join(output_dir, "amortization_schedule_down_payment_450.md"), "w"
) as f:
    f.write("# Amortization Schedule - Down Payment Scenario\n\n")
    f.write(schedule_down_payment_markdown)

with open(
    os.path.join(output_dir, "amortization_schedule_no_down_payment_450.md"), "w"
) as f:
    f.write("# Amortization Schedule - No Down Payment Scenario\n\n")
    f.write(schedule_no_down_payment_markdown)

# Display the total monthly payments including property taxes and homeowners insurance
print(
    f"\nTotal Monthly Payment - Down Payment Scenario: ${total_monthly_payment_down_payment:.2f}"
)
print(
    f"Total Monthly Payment - No Down Payment Scenario: ${total_monthly_payment_no_down_payment:.2f}"
)
