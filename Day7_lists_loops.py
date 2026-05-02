# Day 7: Lists + Loops = Bulk Canada Analysis
print("=== DAY 7: ANALYZING MULTIPLE OFFERS ===")

# From Day 6 - your function, unchanged
def calculate_above_market(offer_salary, city):
    if city == "Toronto": avg = 85000
    elif city == "Vancouver": avg = 90000
    elif city == "Calgary": avg = 80000
    else: avg = 82000
    return offer_salary - avg

# NEW: A LIST = container for multiple items
cities_to_check = ["Toronto", "Vancouver", "Calgary", "Montreal", "Remote"]
test_salary = 90000  # Pretend you got $90k offers in all cities

print(f"Checking $90k offer across {len(cities_to_check)} cities...")
print("-" * 40)

# NEW: A LOOP = do something to EVERY item in the list
for city in cities_to_check:
    difference = calculate_above_market(test_salary, city)
    print(f"{city}: ${difference} vs market")

    print("\n=== BULK OFFER ANALYZER ===")

# Copy your full function from Day 6
def analyze_offer(offer_salary, city, your_experience, required_experience, remote_days):
    difference = calculate_above_market(offer_salary, city)
    
    if difference < 0:
        decision = f"❌ REJECT: ${abs(difference)} below {city} market"
    elif difference >= 10000 and your_experience > required_experience:
        decision = f"✅ ACCEPT: ${difference} above market + overqualified"
    elif difference >= 0 and remote_days >= 3:
        decision = f"⚠️ NEGOTIATE: Only ${difference} above market"
    else:
        decision = f"🤔 MAYBE: ${difference} above market"
    return decision

# NEW: List of dictionaries = each dictionary is 1 job offer
job_offers = [
    {"salary": 95000, "city": "Toronto", "your_exp": 4, "req_exp": 3, "remote": 2},
    {"salary": 85000, "city": "Vancouver", "your_exp": 2, "req_exp": 3, "remote": 4},
    {"salary": 100000, "city": "Calgary", "your_exp": 5, "req_exp": 2, "remote": 1},
    {"salary": 78000, "city": "Montreal", "your_exp": 3, "req_exp": 3, "remote": 5},
    {"salary": 82000, "city": "Remote", "your_exp": 3, "req_exp": 2, "remote": 5}
]

# The money loop: 1 function, 5 offers, 3 lines
print("Analyzing 5 offers from your LinkedIn...")
print("-" * 40)
for offer in job_offers:
    result = analyze_offer(
        offer["salary"], 
        offer["city"], 
        offer["your_exp"], 
        offer["req_exp"], 
        offer["remote"]
    )
    print(f"{offer['city']} ${offer['salary']//1000}k: {result}")

print("-" * 40)
print(f"Total offers processed: {len(job_offers)}")