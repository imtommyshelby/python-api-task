import requests

def fetch_users_table():
    url = "https://jsonplaceholder.typicode.com/users"

    # Toggle For Filteration 
    FILTER_CITY = True

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error: Failed to fetch data (Status Code: {response.status_code})")
            return

        users = response.json()

        if not users:
            print("No user data found.")
            return

        # Table Header
        print("+--------------------------------------------------------------------------------+")
        print("| {:<20} | {:<15} | {:<25} | {:<15} |".format("Name", "Username", "Email", "City"))
        print("+--------------------------------------------------------------------------------+")

        # Rows
        for user in users:
            name = user.get("name", "")
            username = user.get("username", "")
            email = user.get("email", "")
            city = user.get("address", {}).get("city", "")

            # Apply bonus filter
            if FILTER_CITY and not city.lower().startswith("s"):
                continue

            print("| {:<20} | {:<15} | {:<25} | {:<15} |".format(
                name[:20],
                username[:15],
                email[:25],
                city[:15]
            ))

        print("+--------------------------------------------------------------------------------+")

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to API: {e}")


fetch_users_table()
