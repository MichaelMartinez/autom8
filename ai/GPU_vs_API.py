# Graphical Representation
import matplotlib.pyplot as plt

# Define a function to calculate the total cost of ownership for buying a GPU
def gpu_cost(gpu_cost, energy_price, gpu_wattage, depreciation_rate, usage_hours_per_year, depreciation_years):
    # Calculate the electricity cost per year
    electricity_cost_per_year = (gpu_wattage * usage_hours_per_year) / 1000 * energy_price
    
    # Calculate the depreciation cost per year
    depreciation_cost_per_year = gpu_cost / depreciation_years
    
    # Calculate the total cost of ownership per year
    total_cost_per_year = electricity_cost_per_year + depreciation_cost_per_year
    
    # Print the cumulative variables that make up the total cost of ownership
    print("Electricity cost per year: ${:.2f}".format(electricity_cost_per_year))
    print("Depreciation cost per year: ${:.2f}".format(depreciation_cost_per_year))
    
    return total_cost_per_year

# Define a function to calculate the total cost of ownership for using an API
def api_cost(tokens_input_per_year, tokens_output_per_year, price_per_million_input, price_per_million_output, subscription_cost):
    # Calculate the total cost of input tokens
    input_cost = (tokens_input_per_year / 1e6) * price_per_million_input
    output_cost = (tokens_output_per_year / 1e6) * price_per_million_output
    total_cost_per_year = input_cost + output_cost + (subscription_cost *12)
    
    # Print the cumulative variables that make up the total cost of ownership
    print("Input cost per year: ${:.2f}".format(input_cost))
    print("Output cost per year: ${:.2f}".format(output_cost))
    
    return total_cost_per_year

# Get user input for GPU costs
gpu_cost_input = float(input("Enter the cost of the GPU: $"))
energy_price_input = float(input("Enter the price of energy per kilowatt: $/kWh"))
gpu_wattage_input = float(input("Enter the GPU wattage: W"))
depreciation_rate_input = float(input("Enter the depreciation rate per year: %"))
usage_hours_per_year_input = float(input("Enter the number of hours the GPU will be used per year: "))
depreciation_years_input = float(input("Enter the number of years to depreciate the GPU: "))

# Get user input for API costs
tokens_input_per_year_input = float(input("Enter the number of input tokens per year: "))
tokens_output_per_year_input = float(input("Enter the number of output tokens per year: "))
price_per_million_input_input = float(input("Enter the price per million input tokens: $"))
price_per_million_output_input = float(input("Enter the price per million output tokens: $"))
subscription_cost_input = float(input("Enter the subscription cost per year: $"))

# Calculate the total cost of ownership for buying a GPU
gpu_total_cost_per_year = gpu_cost(gpu_cost_input, energy_price_input, gpu_wattage_input, depreciation_rate_input/100, usage_hours_per_year_input, depreciation_years_input)

# Calculate the total cost of ownership for using an API
api_total_cost_per_year = api_cost(tokens_input_per_year_input, tokens_output_per_year_input, price_per_million_input_input, price_per_million_output_input, subscription_cost_input)

# Print the results
print("Total cost of ownership per year for buying a GPU: ${:.2f}".format(gpu_total_cost_per_year))
print("Total cost of ownership per year for using an API: ${:.2f}".format(api_total_cost_per_year))

# Multi-year cost projection
def multi_year_projection(initial_cost, years, annual_operation_cost):
    total_costs = [initial_cost + annual_operation_cost]
    for year in range(1, years):
        total_costs.append(total_costs[-1] + annual_operation_cost)
    return total_costs

years_to_project = 5  # Project costs over 5 years
gpu_costs_over_time = multi_year_projection(0, years_to_project, gpu_total_cost_per_year)
api_costs_over_time = multi_year_projection(0, years_to_project, api_total_cost_per_year)

print("GPU costs over 5 years: ", gpu_costs_over_time)
print("API costs over 5 years: ", api_costs_over_time)



def plot_costs(gpu_costs, api_costs, years):
    plt.plot(range(years), gpu_costs, label='GPU Costs')
    plt.plot(range(years), api_costs, label='API Costs')
    plt.xlabel('Years')
    plt.ylabel('Total Cost ($)')
    plt.title('Cost Comparison Over Time')
    plt.legend()
    plt.show()

# Call the plotting function
plot_costs(gpu_costs_over_time, api_costs_over_time, years_to_project)

# Sensitivity Analysis
# Adjust energy price and see the effect
energy_price_variation = [energy_price_input * (1 + i * 0.05) for i in range(5)]  # 0%, 5%, 10%, 15%, 20% increase
costs_with_varied_energy_prices = [gpu_cost(gpu_cost_input, price, gpu_wattage_input, depreciation_rate_input/100, usage_hours_per_year_input, depreciation_years_input) for price in energy_price_variation]

print("Costs with varied energy prices: ", costs_with_varied_energy_prices)
