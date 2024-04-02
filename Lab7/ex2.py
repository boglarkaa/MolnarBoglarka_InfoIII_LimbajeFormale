options = {
    "A": {
        "name": "beach vacation",
        "attributes": ["beach", "medium", "sunny"],
    },
    "B": {"name": "mountain vacation", "attributes": ["mountain", "low", "mixed"]},
    "C": {
        "name": "city vacation",
        "attributes": ["city", "high", "rainy"],
    },
}

budget = input("Enter your budget (low, medium, high): ")
interest = input("Enter your interest (beach, mountain, city): ")
weather = input("Enter your prefered weather (sunny, rainy, mixed): ")

scores = {}
for option, attrs in options.items():
    score = 0
    if attrs["attributes"][0] == interest:
        score += 1
    if budget == "low" and "low" in attrs["attributes"]:
        score += 1
    elif budget == "medium" and "medium" in attrs["attributes"]:
        score += 1
    elif budget == "high" and "high" in attrs["attributes"]:
        score += 1
    if weather == "sunny" and "sunny" in attrs["attributes"]:
        score += 1
    elif weather == "rainy" and "rainy" in attrs["attributes"]:
        score += 1
    elif weather == "mixed" and "mixed" in attrs["attributes"]:
        score += 1
    scores[option] = score

best_option = max(scores, key=scores.get)
print("Best option:", options[best_option]["name"])
