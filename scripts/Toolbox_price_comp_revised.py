class Toolbox:
    def __init__(self, name, dimensions, cost, quantity=1):
        self.name = name
        self.dimensions = (
            dimensions  # List of (length, width, height) tuples for each box
        )
        self.cost = cost
        self.quantity = quantity

    def total_volume_cubic_feet(self):
        total_volume = 0
        for dim in self.dimensions:
            length, width, height = dim
            single_volume = (
                length * width * height
            ) / 1728  # 1 cubic foot = 1728 cubic inches
            total_volume += single_volume
        return total_volume * self.quantity

    def price_per_cubic_foot(self):
        return self.cost / self.total_volume_cubic_feet()


# Define the toolboxes with verified dimensions and prices
toolboxes = [
    Toolbox(
        "Milwaukee Packout 3 Part Combo",
        [(22.1, 18.6, 14.9), (22.1, 16.3, 11.1), (22.1, 16.2, 6.5)],
        279,
    ),
    Toolbox(
        "Dewalt Tough System 3 Part Combo",
        [(21.6, 14.4, 16.7), (21.6, 14.4, 8.9), (21.6, 14.4, 4.5)],
        249,
    ),
    Toolbox(
        "Ridgid ProGear 2.0 3 Part Combo",
        [(22.2, 19.5, 16), (22.2, 13.25, 12.25), (22.2, 13.25, 6.5)],
        204,
    ),
    Toolbox(
        "Husky Build Out 3 Part Combo",
        [(22.4, 18.9, 15.5), (22.4, 16.8, 11.7), (22.4, 16.8, 6.5)],
        149,
    ),
    Toolbox(
        "Husky Connect 3 Part Combo",
        [(22.0, 11.5, 9.0), (22.0, 14.0, 12.0), (22.0, 16.5, 16.5)],
        199,
    ),
    Toolbox(
        "ToughBuilt StackTech 3-Piece Storage System",
        [(22.3, 19.7, 15.5), (21.0, 16.0, 11.7), (21.0, 16.0, 7.2)],
        299,
    ),
    Toolbox(
        "Klein MODbox 3 Part Combo",
        [(22.6, 19.9, 15.5), (22, 15.5, 11.7), (22, 15.5, 6.6)],
        319,
    ),
]

# Define medium boxes with verified dimensions and prices
medium_boxes = [
    Toolbox("Milwaukee Packout Medium Box", [(22.1, 16.3, 11.1)], 69),
    Toolbox("Dewalt Tough System Medium Box", [(21.6, 14.4, 8.9)], 79),
    Toolbox("Ridgid ProGear 2.0 Medium Box", [(22.2, 13.25, 12.25)], 59),
    Toolbox("Husky Build Out Medium Box", [(22.4, 16.8, 11.7)], 64),
    Toolbox("Husky Connect Medium Box", [(22.0, 14.0, 12.0)], 59),
    Toolbox("ToughBuilt StackTech Medium Box", [(21.0, 16.0, 11.7)], 89),
    Toolbox("Klein MODbox Medium Box", [(22, 15.5, 11.7)], 99),
]

# Define small part organizers with verified dimensions and prices
small_part_organizers = [
    Toolbox("Milwaukee Packout Small Part Organizer", [(22.1, 11.3, 6.5)], 49),
    Toolbox("Dewalt Tough System Small Part Organizer", [(21.6, 14.4, 4.5)], 59),
    Toolbox("Ridgid ProGear 2.0 Small Part Organizer", [(22.2, 14.0, 5.9)], 39),
    Toolbox("Husky Build Out Small Part Organizer", [(21.5, 16.8, 4.37)], 33),
    Toolbox("Husky Connect Small Part Organizer", [(22.0, 11.5, 9.0)], 39),
    Toolbox("ToughBuilt StackTech Small Part Organizer", [(21.0, 16.0, 7.2)], 59),
    Toolbox("Klein MODbox Small Part Organizer", [(18.5, 12.3, 8.1)], 69),
    Toolbox("HDX small parts organizer", [(15, 11.5, 4.7)], 11),
]

# Define two-drawer boxes with verified dimensions and prices
two_drawer_boxes = [
    Toolbox("Milwaukee Packout Two-Drawer Box", [(22.1, 16.3, 14.1)], 156),
    Toolbox("Dewalt Tough System Two-Drawer Box", [(21.8, 12.4, 12.6)], 129),
    Toolbox("Ridgid ProGear 2.0 Two-Drawer Box", [(22.3, 16.2, 15.2)], 99),
    Toolbox("Husky Build Out Two-Drawer Box", [(22.2, 14.6, 14.6)], 124),
    Toolbox("Husky Connect Two-Drawer Box", [(22.0, 14.0, 13.5)], 109),
    Toolbox("ToughBuilt StackTech Two-Drawer Box", [(21.0, 16.0, 13.8)], 149),
    Toolbox("Klein MODbox Two-Drawer Box", [(21.6, 15.3, 13.6)], 159),
]

# Define small boxes with verified dimensions and prices
small_boxes = [
    Toolbox("Milwaukee Packout Small Box", [(22.1, 11.3, 6.5)], 59),
    Toolbox("Dewalt Tough System Small Box", [(21.6, 14.4, 4.5)], 69),
    Toolbox("Ridgid ProGear 2.0 Small Box", [(22.2, 13.25, 6.5)], 49),
    Toolbox("Husky Build Out Small Box", [(21.5, 16.8, 4.37)], 39),
    Toolbox("Husky Connect Small Box", [(22.0, 11.5, 9.0)], 49),
    Toolbox("ToughBuilt StackTech Small Box", [(21.0, 16.0, 7.2)], 69),
    Toolbox("Klein MODbox Small Box", [(18.5, 12.3, 8.1)], 79),
]


# Function to print toolbox details
def print_toolbox_details(toolboxes, description):
    results = []
    results.append(description)
    for toolbox in toolboxes:
        total_volume_cubic_feet = toolbox.total_volume_cubic_feet()
        price_per_cubic_foot = toolbox.price_per_cubic_foot()

        results.append(f"{toolbox.name}:")
        results.append(f"  Dimensions (LxWxH) for each box: {toolbox.dimensions}")
        results.append(f"  Quantity: {toolbox.quantity}")
        results.append(f"  Total Volume: {total_volume_cubic_feet:.4f} cubic feet")
        results.append(f"  Cost: ${toolbox.cost}")
        results.append(f"  Price per cubic foot: ${price_per_cubic_foot:.4f}")
        results.append("")

    # Sort toolboxes by price per cubic foot
    sorted_toolboxes = sorted(toolboxes, key=lambda x: x.price_per_cubic_foot())
    results.append("Sorted by price per cubic foot:")
    for toolbox in sorted_toolboxes:
        results.append(
            f"{toolbox.name} - Price per cubic foot: ${toolbox.price_per_cubic_foot():.4f}"
        )

    return results


# Generate results for all categories
results_combo = print_toolbox_details(toolboxes, "Combo Toolboxes:")
results_medium = print_toolbox_details(medium_boxes, "Medium Boxes:")
results_small = print_toolbox_details(small_part_organizers, "Small Part Organizers:")
results_two_drawer = print_toolbox_details(two_drawer_boxes, "Two-Drawer Boxes:")
results_small_boxes = print_toolbox_details(small_boxes, "Small Boxes:")

# Write all results to a text file
with open("toolbox_prices.txt", "w") as file:
    for line in (
        results_combo
        + ["\n"]
        + results_medium
        + ["\n"]
        + results_small
        + ["\n"]
        + results_two_drawer
        + ["\n"]
        + results_small_boxes
    ):
        file.write(line + "\n")

print("Results saved")
