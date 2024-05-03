

def calculate_annual_rent_cost(pages_per_year, cost_per_token_input, cost_per_token_output, update_factor):
    tokens_per_page = 2000
    cost_per_page = ((tokens_per_page / 1_000_000) * cost_per_token_input) + ((tokens_per_page / 1_000_000) * cost_per_token_output)
    annual_cost = cost_per_page * pages_per_year
    return annual_cost * update_factor  # Adjusted for access to the latest technology

def calculate_annual_buy_cost(gpu_cost, power_cost_per_kWh, power_usage_watts, lifespan_years, pages_per_year, software_update_cost):
    kWh_per_year = (power_usage_watts / 1000) * 24 * 365
    annual_power_cost = kWh_per_year * power_cost_per_kWh
    costs_per_year = [0] * lifespan_years
    costs_per_year[0] = gpu_cost + annual_power_cost + software_update_cost
    for year in range(1, lifespan_years):
        costs_per_year[year] = annual_power_cost + software_update_cost
    return costs_per_year

# Inputs
pages_per_year = int(input("Enter the number of pages processed per year: "))
gpu_cost = float(input("Enter the cost of the GPU: "))
power_cost_per_kWh = 0.12
power_usage_watts = 400
lifespan_years = int(input("Enter the expected lifespan of the GPU in years: "))
software_update_cost = float(input("Enter annual software/model update cost for owned GPU: "))
update_factor = 1.05
input_per_million_tokens = float(input("enter the input cost per million tokens:"))
output_per_million_tokens = (float(input("enter the output cost per million tokens:")))

# Calculate costs
annual_rent_costs = [calculate_annual_rent_cost(pages_per_year, input_per_million_tokens, output_per_million_tokens, update_factor) for _ in range(lifespan_years)]
buy_costs_per_year = calculate_annual_buy_cost(gpu_cost, power_cost_per_kWh, power_usage_watts, lifespan_years, pages_per_year, software_update_cost)

# Print results and compare
print("\nYearly Cost Comparison (Renting vs. Buying):")
cumulative_rent_cost = 0
rent_surpasses_buy_cost = None
for year in range(lifespan_years):
    cumulative_rent_cost += annual_rent_costs[year]
    if cumulative_rent_cost > gpu_cost and rent_surpasses_buy_cost is None:
        rent_surpasses_buy_cost = year + 1
    print(f"Year {year + 1}: Renting: ${annual_rent_costs[year]:.2f} (Cumulative: ${cumulative_rent_cost:.2f}), Buying: ${buy_costs_per_year[year]:.2f}")

# When does rent surpass initial buy cost?
if rent_surpasses_buy_cost:
    print(f"\nRenting costs surpass initial GPU purchase cost in year: {rent_surpasses_buy_cost}")
else:
    print("\nRenting costs do not surpass initial GPU purchase cost within the expected lifespan.")

# Determine if buying becomes cheaper in any year
cheaper_years = [year + 1 for year in range(lifespan_years) if buy_costs_per_year[year] < annual_rent_costs[year]]
if cheaper_years:
    print(f"\nBuying becomes cheaper starting in year: {cheaper_years[0]}")
else:
    print("\nRenting is more cost-effective over the GPU's expected lifespan.")