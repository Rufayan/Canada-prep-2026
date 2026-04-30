# Day 5 Bonus: Should you take the Canadian tech job offer?
print("=== CANADA TECH OFFER ANALYZER ===")

# Change these to test different offers
city = "Toronto"  # Options: "Toronto", "Vancouver", "Calgary", "Montreal", "Remote"
offer_salary = 95000  # CAD per year
years_experience_required = 3
your_experience = 4
remote_days = 2  # Days per week remote allowed

# Canadian market data 2026
avg_salaries_junior = {
    "Toronto": 85000,
    "Vancouver": 90000,
    "Calgary": 80000,
    "Montreal": 75000,
    "Remote": 82000
}

# Get the average salary for the selected city, default to Remote if city not found
avg_city_junior = avg_salaries_junior.get(city, avg_salaries_junior["Remote"])

print(f"Offer: ${offer_salary} in {city} | You have {your_experience} years exp")
print("-" * 50)

# YOUR LOGIC HERE: Use if/elif/else to decide
if offer_salary < avg_city_junior:
    print(f"❌ REJECT: Below market (Avg: ${avg_city_junior})")
elif offer_salary >= avg_city_junior + 10000 and your_experience > years_experience_required:
    print(f"✅ ACCEPT: Great offer!")
elif offer_salary >= avg_city_junior and remote_days >= 3:
    print(f"⚠️ NEGOTIATE: Ask for more remote days or 5k")
else:
    print(f"🤔 MAYBE: Accept but keep interviewing")

# Bonus: Add a line that calculates how much above/below market: offer - avg_salary
market_difference = offer_salary - avg_city_junior
print(f"Market difference: ${market_difference}")