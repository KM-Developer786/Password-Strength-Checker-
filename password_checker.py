print("my name is moiz ")
import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make it at least 8 characters long.")

    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Mix upper and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1
    else:
        feedback.append("Include a special character.")

    if score == 4:
        return "Strong Password!", []
    elif score == 3:
        return "Moderate Password.", feedback
    else:
        return "Weak Password!", feedback

pwd = input("Enter a password: ")
rating, tips = check_password_strength(pwd)

print("\nResult:", rating)

for tip in tips:
    print("->", tip)
