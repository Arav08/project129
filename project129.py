import csv

data = []

with open ("dwarf_stars.csv", "r") as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        data.append(row)

headers = data[0]
dwarf_planet_data = data[1:]

# Converting all planet names to lowercase
for data_point in dwarf_planet_data:
    data_point[2] = data_point[2].lower()

# Sorting all planets in alphabetical order
dwarf_planet_data.sort(key = lambda dwarf_planet_data: dwarf_planet_data[2])

with open ("dwarf_sorted.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(dwarf_planet_data)

# Remove blank lines from the sorted csv
with open ("dwarf_sorted.csv") as input, open("dwarf_sorted1.csv", "w", newline = "") as output:
    writer = csv.writer(output)

    for row in csv.reader(input):
        if any (field.strip() for field in row):
            writer.writerow(row)