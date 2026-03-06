# Profile Card Program

name = "Asantewa Appiah"
cohort = "Tech4Girls Backend"
age = 21
favorite_topic = "Python Basics"
current_week = 3

# String methods
name = name.title()
favorite_topic = favorite_topic.replace("Basics", "Fundamentals")

# Weeks remaining
weeks_left = 12 - current_week

# Output profile card
print("========== PROFILE CARD ==========")
print(f"Name: {name}")
print(f"Cohort: {cohort}")
print(f"Age: {age}")
print(f"Favourite Topic: {favorite_topic}")
print(f"Current Week: {current_week}")
print("----------------------------------")
print(f"Weeks left in program: {weeks_left}")
print("==================================")

