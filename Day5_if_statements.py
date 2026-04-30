# Day 5: if/else for Canada Job Hunt Decisions
print("=== CANADA JOB SMART FILTER ===")

cities = ["Toronto", "Montreal", "Vancouver", "Calgary", "Ottawa"]
salaries = [85000, 75000, 90000, 80000, 78000]
french_needed = [False, True, False, False, True]

min_salary = 80000  # Your target salary
speak_french = True  # Change to True if you do

print(f"Filtering jobs: Min ${min_salary} CAD, French: {speak_french}")
print("-" * 45)
# Loop + if/else = Smart filtering
qualified_jobs = 0

for i in range(len(cities)):
    city = cities[i]
    salary = salaries[i]
    needs_french = french_needed[i]

    # Decision time: Do you qualify?
    if salary >= min_salary and needs_french == speak_french:
        print(f"✅ APPLY: {city} - ${salary} CAD")
        qualified_jobs += 1
    else:
        print(f"❌ Skip: {city} - Reason: ", end="")
        if salary < min_salary:
            print(f"Salary ${salary} < ${min_salary}")
        else:
            print(f"French required but you put {speak_french}")

    print("-" * 45)

print(f"\nResult: You can apply to {qualified_jobs} out of {len(cities)} cities")
print("Day 5 analysis complete!")