class Organizer:
    def __init__(self, name, length, width, height, cost, quantity=1):
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.cost = cost
        self.quantity = quantity

    def total_volume(self):
        # Calculate the total interior volume for all organizers in the pack
        single_volume = self.length * self.width * self.height
        return single_volume * self.quantity

    def price_per_cubic_inch(self):
        # Calculate price per cubic inch
        return self.cost / self.total_volume()

    def price_per_cubic_mm(self):
        # Calculate price per cubic millimeter
        return self.cost / (
            self.total_volume() * 16387.064
        )  # 1 cubic inch = 16387.064 cubic millimeters

    def price_per_cubic_foot(self):
        # Calculate price per cubic foot
        return self.cost / (
            self.total_volume() / 1728
        )  # 1 cubic foot = 1728 cubic inches

    def price_per_cubic_meter(self):
        # Calculate price per cubic meter
        return self.cost / (
            self.total_volume() * 0.000016387064
        )  # 1 cubic inch = 0.000016387064 cubic meters


organizers = [
    Organizer("Craftsman 3 Pack", 11.5, 8.5, 2.5, 25, 3),
    Organizer("Home Depot HDX - 2pk", 15, 11.6, 2.6, 10, 2),
    Organizer("Dewalt 20 part pro 2pk", 17.4, 11, 3, 33, 2),
    Organizer("Milwaukee Packout 11 compartment", 19, 14.5, 6.6, 50, 1),
    Organizer("Husky 22 compartment", 22.25, 12.5, 6.34, 40, 1),
    Organizer(
        "Connect 2-Drawer 13-Compartment Small Parts Organizer", 21.5, 12.2, 7.25, 45, 1
    ),
    Organizer("Husky 10 compartment 2pk", 22, 12, 4.5, 40, 2),
    Organizer("Ryobi 10 compartment", 20, 18, 6, 47, 1),
    Organizer("Ridgid 10 compartment", 22, 13, 5, 35, 1),
    Organizer("Walmart Hart small parts with bins", 20.3, 13.6, 4.5, 22, 1),
    Organizer(
        "HART Stack System Tool Box with Small Blue Organizer & Dividers",
        21,
        13.6,
        6,
        29,
        1,
    ),
    Organizer("BOSCH L-BOXX-2 6 In. x 14 In. x 17.5 In.", 17.5, 14, 6, 50, 1),
    Organizer("Festool 204840 Systainer", 15.6, 11.6, 4.125, 67, 1),
    Organizer(
        "Hart Catalever, No Stack - 18.20 x 9.70 x 11.80 Inches", 18.2, 11.8, 9.7, 25, 1
    ),
    Organizer("Toughbuilt TechStack small part org", 21, 16, 7.2, 70, 1),
    Organizer("Metabo Metabox 215", 15.6, 11.65, 8.46, 38, 1),
]

# Calculate and print the price per cubic inch, price per cubic millimeter, price per cubic foot, price per cubic meter, and total volume for each organizer
results = []
for organizer in organizers:
    total_volume = organizer.total_volume()
    price_per_cubic_inch = organizer.price_per_cubic_inch()
    price_per_cubic_mm = organizer.price_per_cubic_mm()
    price_per_cubic_foot = organizer.price_per_cubic_foot()
    price_per_cubic_meter = organizer.price_per_cubic_meter()

    results.append(f"{organizer.name}:")
    results.append(
        f"  Dimensions (LxWxH): {organizer.length} x {organizer.width} x {organizer.height} inches"
    )
    results.append(f"  Quantity: {organizer.quantity}")
    results.append(f"  Total Volume: {total_volume:.4f} cubic inches")
    results.append(f"  Cost: ${organizer.cost}")
    results.append(f"  Price per cubic inch: ${price_per_cubic_inch:.4f}")
    results.append(f"  Price per cubic millimeter: ${price_per_cubic_mm:.6f}")
    results.append(f"  Price per cubic foot: ${price_per_cubic_foot:.4f}")
    results.append(f"  Price per cubic meter: ${price_per_cubic_meter:.4f}")
    results.append("")

# Sort organizers by price per cubic inch
sorted_organizers = sorted(organizers, key=lambda x: x.price_per_cubic_inch())
results.append("Organizers sorted by price per cubic inch:")
for organizer in sorted_organizers:
    results.append(
        f"{organizer.name} - Price per cubic inch: ${organizer.price_per_cubic_inch():.4f}"
    )

# Sort organizers by price per cubic millimeter
sorted_organizers_mm = sorted(organizers, key=lambda x: x.price_per_cubic_mm())
results.append("\nOrganizers sorted by price per cubic millimeter:")
for organizer in sorted_organizers_mm:
    results.append(
        f"{organizer.name} - Price per cubic millimeter: ${organizer.price_per_cubic_mm():.6f}"
    )

# Sort organizers by price per cubic foot
sorted_organizers_ft = sorted(organizers, key=lambda x: x.price_per_cubic_foot())
results.append("\nOrganizers sorted by price per cubic foot:")
for organizer in sorted_organizers_ft:
    results.append(
        f"{organizer.name} - Price per cubic foot: ${organizer.price_per_cubic_foot():.4f}"
    )

# Sort organizers by price per cubic meter
sorted_organizers_m = sorted(organizers, key=lambda x: x.price_per_cubic_meter())
results.append("\nOrganizers sorted by price per cubic meter:")
for organizer in sorted_organizers_m:
    results.append(
        f"{organizer.name} - Price per cubic meter: ${organizer.price_per_cubic_meter():.4f}"
    )

# Write results to a text file
with open("organizer_prices.txt", "w") as file:
    for line in results:
        file.write(line + "\n")

print("Results saved to organizer_prices.txt")
