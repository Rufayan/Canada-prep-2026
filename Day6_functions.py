# Day 6: Functions = Reusable Canadian Logic
print("=== DAY 6: FUNCTIONS FOR CANADA 2026 ===")

# A function is just a named recipe you can run anytime
def greet_analyst(name, city):
    print(f"Hello {name}! Ready to analyze data in {city}?")
    print("Your GitHub streak proves you're serious 🇨🇦")

# Call the function = run the recipe
greet_analyst("Rufayan", "Toronto")
greet_analyst("Future You", "Vancouver")

print("-" * 40)

# Function that TAKES data and GIVES BACK an answer
def calculate_above_market(offer_salary, city):
    # Step 1: Set avg salary based on city
    if city == "Toronto":
        avg = 85000
    elif city == "Vancouver":
        avg = 90000
    elif city == "Calgary":
        avg = 80000
    elif city == "Montreal":
        avg = 75000
    else:  # Remote or other
        avg = 82000
    
    # Step 2: Do the math
    difference = offer_salary - avg
    
    # Step 3: return the answer = send data back out of the function
    return difference

# Now use the function like a calculator
toronto_diff = calculate_above_market(95000, "Toronto")
vancouver_diff = calculate_above_market(85000, "Vancouver") 
calgary_diff = calculate_above_market(100000, "Calgary")

print(f"Toronto $95k offer: ${toronto_diff} vs market")
print(f"Vancouver $85k offer: ${vancouver_diff} vs market") 
print(f"Calgary $100k offer: ${calgary_diff} vs market")

def analyze_offer(offer_salary, city, your_experience, required_experience, remote_days):
    # Reuse our first function inside this one = function composition
    difference = calculate_above_market(offer_salary, city)
    
    # Decision logic from yesterday, but now reusable
    if difference < 0:
        decision = f"❌ REJECT: ${abs(difference)} below {city} market"
    elif difference >= 10000 and your_experience > required_experience:
        decision = f"✅ ACCEPT: ${difference} above market + you’re overqualified"
    elif difference >= 0 and remote_days >= 3:
        decision = f"⚠️ NEGOTIATE: Only ${difference} above market. Ask for 3+ remote days or $5k more"
    else:
        decision = f"🤔 MAYBE: ${difference} above market. Keep interviewing"
    
    return decision

# Test it on 3 real scenarios
print("\n=== JOB OFFER ANALYZER ===")
result1 = analyze_offer(95000, "Toronto", 4, 3, 2)
result2 = analyze_offer(85000, "Vancouver", 2, 3, 4) 
result3 = analyze_offer(82000, "Remote", 3, 2, 2)

print(f"Toronto $95k: {result1}")
print(f"Vancouver $85k: {result2}")
print(f"Remote $82k: {result3}")