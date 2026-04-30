age = 28  # Change to your real age
education = "masters"  # options: "high_school", "bachelors", "masters", "phd"
ielts_score = 8.5  # Out of 9.0

if age <= 35 and education == "masters" and ielts_score >= 7.0:
    print("✅ You likely qualify! 450+ points")
elif age <= 35 and ielts_score >= 7.0:
    print("⚠️ Maybe qualify. Need 400+ points. Improve education")
else:
    print("❌ Low chance. Work on age, IELTS, or education")