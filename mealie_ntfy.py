import requests
from datetime import datetime, timedelta

# --- CONFIGURATION ---
MEALIE_URL = "http://localhost:9000"  # Update with your Mealie local IP/port if needed
API_TOKEN = "YOUR_MEALIE_API_TOKEN"   # Replace with your Mealie API Token
NTFY_URL = "https://ntfy.sh/your-secret-mealie-topic" # Replace with your ntfy topic/server

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def generate_weekly_meals():
    start_date = datetime.now()
    weekly_plan = []

    print("Generating random meals for the next 7 days...")

    for i in range(7):
        target_date = start_date + timedelta(days=i)
        date_str = target_date.strftime("%Y-%m-%d")
        day_name = target_date.strftime("%A")

        # Call Mealie API to assign a random dinner for this date
        payload = {
            "date": date_str,
            "entryType": "dinner"
        }
        
        response = requests.post(f"{MEALIE_URL}/api/households/mealplans/random", json=payload, headers=headers)
        
        if response.status_code == 200 or response.status_code == 201:
            data = response.json()
            # Depending on Mealie version, the recipe name might be structured differently
            recipe_name = data.get("recipe", {}).get("name", "Random Recipe")
            weekly_plan.append(f"• **{day_name} ({date_str})**: {recipe_name}")
        else:
            weekly_plan.append(f"• **{day_name} ({date_str})**: *Failed to assign*")

    return "\n".join(weekly_plan)

def send_ntfy(message):
    headers_ntfy = {
        "Title": "New Weekly Dinners 🍽️",
        "Tags": "knife_fork_plate,calendar"
    }
    requests.post(NTFY_URL, data=message.encode('utf-8'), headers=headers_ntfy)
    print("Meal plan successfully sent to ntfy!")

if __name__ == "__main__":
    plan = generate_weekly_meals()
    send_ntfy(plan)
