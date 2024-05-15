class Toolbox:
    def __init__(self, name, dimensions, interior_dimensions, cost, quantity=1):
        self.name = name
        self.dimensions = (
            dimensions  # List of (length, width, height) tuples for each box
        )
        self.interior_dimensions = (
            interior_dimensions  # List of (length, width, height) tuples for each box
        )
        self.cost = cost
        self.quantity = quantity

    def total_volume_cubic_feet(self, use_interior=False):
        total_volume = 0
        dims = self.interior_dimensions if use_interior else self.dimensions
        for dim in dims:
            length, width, height = dim
            single_volume = (
                length * width * height
            ) / 1728  # 1 cubic foot = 1728 cubic inches
            total_volume += single_volume
        return total_volume * self.quantity

    def price_per_cubic_foot(self, use_interior=False):
        return self.cost / self.total_volume_cubic_feet(use_interior)


# Define the toolboxes with exterior and interior dimensions and prices
toolboxes = [
    Toolbox(
        "Milwaukee Packout 3 Part Combo",
        [(22.1, 18.6, 14.9), (22.1, 16.3, 11.1), (22.1, 16.2, 6.5)],
        [(19.1, 14.6, 13.9), (19.7, 13.2, 8.5), (19.1, 14.6, 3.9)],
        279,
    ),
    Toolbox(
        "Klein MODbox 3 Part Combo",
        [(22.6, 19.9, 15.5), (22, 15.5, 11.7), (22, 15.5, 6.6)],
        [(19.6, 13.6, 13.4), (19.1, 13.6, 9.2), (19.7, 13.2, 4.5)],
        319,
    ),
    Toolbox(
        "Husky Build Out 3 Part Combo",
        [(22.4, 18.9, 15.5), (22.4, 16.8, 11.7), (22.4, 16.8, 6.5)],
        [(18.5, 13.4, 14.3), (18.5, 12.9, 9.0), (20.1, 13.2, 4.0)],
        149,
    ),
    Toolbox(
        "Ridgid ProGear 2.0 3 Part Combo",
        [(22.2, 19.5, 16), (22.2, 13.25, 12.25), (22.2, 13.25, 6.5)],
        [(19.5, 12, 14), (19.5, 11, 10.2), (19.5, 11, 4.25)],
        204,
    ),
]


# Function to print toolbox details
def print_toolbox_details(toolboxes, description):
    results = []
    results.append(description)
    for toolbox in toolboxes:
        total_volume_exterior = toolbox.total_volume_cubic_feet(use_interior=False)
        price_per_cubic_foot_exterior = toolbox.price_per_cubic_foot(use_interior=False)

        total_volume_interior = toolbox.total_volume_cubic_feet(use_interior=True)
        price_per_cubic_foot_interior = toolbox.price_per_cubic_foot(use_interior=True)

        results.append(f"{toolbox.name}:")
        results.append(f"  Dimensions (LxWxH) for each box: {toolbox.dimensions}")
        results.append(
            f"  Total Volume (Exterior): {total_volume_exterior:.4f} cubic feet"
        )
        results.append(
            f"  Price per cubic foot (Exterior): ${price_per_cubic_foot_exterior:.4f}"
        )
        results.append(
            f"  Interior Dimensions (LxWxH) for each box: {toolbox.interior_dimensions}"
        )
        results.append(
            f"  Total Volume (Interior): {total_volume_interior:.4f} cubic feet"
        )
        results.append(
            f"  Price per cubic foot (Interior): ${price_per_cubic_foot_interior:.4f}"
        )
        results.append("")

    # Sort toolboxes by price per cubic foot (Interior)
    sorted_toolboxes_interior = sorted(
        toolboxes, key=lambda x: x.price_per_cubic_foot(use_interior=True)
    )
    results.append("Sorted by price per cubic foot (Interior):")
    for toolbox in sorted_toolboxes_interior:
        results.append(
            f"{toolbox.name} - Price per cubic foot (Interior): ${toolbox.price_per_cubic_foot(use_interior=True):.4f}"
        )

    # Sort toolboxes by price per cubic foot (Exterior)
    sorted_toolboxes_exterior = sorted(
        toolboxes, key=lambda x: x.price_per_cubic_foot(use_interior=False)
    )
    results.append("Sorted by price per cubic foot (Exterior):")
    for toolbox in sorted_toolboxes_exterior:
        results.append(
            f"{toolbox.name} - Price per cubic foot (Exterior): ${toolbox.price_per_cubic_foot(use_interior=False):.4f}"
        )

    return results


# Generate results for all categories
results_combo = print_toolbox_details(toolboxes, "Combo Toolboxes:")

# Write all results to a text file
with open("toolbox_prices_both.txt", "w") as file:
    for line in results_combo:
        file.write(line + "\n")

print("Results saved to toolbox_prices_both.txt")
