# Day 8: Reading Real CSV Data Like a Pro
import csv  # Python's built-in tool for CSV files

print("=== DAY 8: READING TORONTO JOBS CSV ===")

# Copy your functions from Day 7
def calculate_above_market(offer_salary, city):
    if city == "Toronto": avg = 85000
    elif city == "Vancouver": avg = 90000
    elif city == "Calgary": avg = 80000
    else: avg = 82000
    return offer_salary - avg

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

# NEW: Read the CSV file
job_offers = []  # Empty list to store all rows

with open('toronto_jobs.csv', 'r') as file:
    csv_reader = csv.DictReader(file)  # Reads each row as a dictionary
    for row in csv_reader:
        job_offers.append(row)  # Add each row to our list

print(f"Loaded {len(job_offers)} jobs from CSV")
print("-" * 50)

print("\n=== RUNNING ANALYZER ON CSV DATA ===")
print("-" * 50)

for job in job_offers:
    # CSV gives us strings. Convert to integers for math
    salary = int(job['salary'])
    your_exp = int(job['your_experience'])
    req_exp = int(job['required_experience'])
    remote = int(job['remote_days'])
    city = job['city']
    title = job['job_title']
    
    # Run your Day 6/7 brain
    decision = analyze_offer(salary, city, your_exp, req_exp, remote)
    
    # Print like a real report
    print(f"{title} | ${salary//1000}k | {decision}")

print("-" * 50)
print(f"Total jobs analyzed: {len(job_offers)}")
print("✅ Day 8 Complete: CSV → Analysis → Report")