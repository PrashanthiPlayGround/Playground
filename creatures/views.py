from django.shortcuts import render

# Mythical creatures data (using a dictionary instead of a database)
creatures = [
    {"name": "Kraken", "strength": 85, "speed": 60, "intelligence": 75, "legends": 30, "rarity": 70},
    {"name": "Phoenix", "strength": 70, "speed": 95, "intelligence": 88, "legends": 40, "rarity": 95},
    {"name": "Dragon", "strength": 95, "speed": 80, "intelligence": 85, "legends": 50, "rarity": 90},
    {"name": "Minotaur", "strength": 78, "speed": 55, "intelligence": 60, "legends": 20, "rarity": 50},
]

# Function to calculate ranking score
def calculate_rank(strength, speed, intelligence, legends, rarity):
    return (strength * 0.4) + (speed * 0.2) + (intelligence * 0.2) + (legends * 0.1) + (rarity * 0.1)

# View function
def creature_ranking(request):
    creature_data = []

    for creature in creatures:
        score = calculate_rank(
            creature["strength"], creature["speed"], creature["intelligence"], creature["legends"], creature["rarity"]
        )
        
        # Categorizing creatures based on their score
        if score > 85:
            category = "Legendary"
        elif score > 60:
            category = "Rare"
        else:
            category = "Extinct"

        creature_data.append({
            "name": creature["name"],
            "strength": creature["strength"],
            "speed": creature["speed"],
            "intelligence": creature["intelligence"],
            "legends": creature["legends"],
            "rarity": creature["rarity"],
            "score": round(score, 2),
            "category": category
        })

    # **Sort the creatures by score in descending order**
    sorted_creatures = sorted(creature_data, key=lambda x: x["score"], reverse=True)

    context = {
        "creatures": sorted_creatures
    }

    return render(request, "creature_ranking.html", context)
