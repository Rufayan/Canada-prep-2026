# Day 4: Lists + Loops for Canada Job Hunt
print("=== CANADA CITY SALARY ANALYZER ===")

# List 1: Target cities
cities = ["Toronto", "Montreal", "Vancouver", "Calgary", "Ottawa"]

# List 2: Avg Data Analyst salary CAD - matching order
salaries = [85000, 75000, 90000, 80000, 78000]

# List 3: French required? 
french_needed = [False, True, False, False, True]

print(f"Checking {len(cities)} cities for jobs...")
print("-" * 35)
# Loop through all cities and print job summary
for i in range(len(cities)):
    city = cities[i]
    salary = salaries[i]
    needs_french = french_needed[i]

    print(f"City: {city}")
    print(f"Avg Salary: ${salary} CAD")
    print(f"French Required: {needs_french}")
    print("-" * 35)

print("Day 4 analysis complete!")