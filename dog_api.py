"""
Assignment Overview:

You are building a Dog Image Browser using the Dog CEO REST API.

The app should allow users to:
- View a list of all available dog breeds
- Get a random image of a breed
- Get a random image of a sub-breed

You will be using the Dog CEO API: https://dog.ceo/dog-api/

Your app should display a main menu with the following options:
1. Show all breeds
2. Get a random image from a breed
3. Get a random image from a sub-breed
4. Exit

The system should handle the following errors:
- Handling errors when a user enters an invalid menu option
- Handling errors when a user enters a breed that does not exist
- Handling errors when a user enters a sub-breed that does not exist
- Handling connection errors when calling the API

If there is an error you should print your own custom error message to the user and allow them to try again.
- Hint: you can use a while loop + try / except blocks to handle this

You should use try / except blocks to handle these errors.

You can either use the should use the requests library or the http.client library to make your requests

"""
# 1. Show all breeds
# 2. Get a random image from a breed
# 3. Get a random image from a sub-breed
# 4. Exit

# The system should handle the following errors:
# - Handling errors when a user enters an invalid menu option
# - Handling errors when a user enters a breed that does not exist
# - Handling errors when a user enters a sub-breed that does not exist
# - Handling connection errors when calling the API

# If there is an error you should print your own custom error message to the user and allow them to try again.
# - Hint: you can use a while loop + try / except blocks to handle this


import requests

def get_all_breeds():
    """GET request to fetch all dog breeds."""
    try:
    #- Handling connection errors when calling the API
        response = requests.get("https://dog.ceo/api/breeds/list/all")
        response.raise_for_status()
        data = response.json()
        return response.json()["message"]
    except requests.exceptions.RequestException:
        print("Error: Could not fetch breed list from API")
        return None

def get_random_image(breed):
    # 2. Get a random image from a breed
    """GET request to fetch a random image from a breed."""
    try:
        response = requests.get("https://dog.ceo/api/breed/{breed}/images/random")
    # Handling connection errors when calling the API
    # TODO: Make a request to https://dog.ceo/api/breed/{breed}/images/random
        response.raise_for_status()
        data = response.json()
        return data["message"]
    except requests.exceptions.RequestException:
        print("Error: Could not fetch image for that breed.")
        return None
    # TODO: Return the image URL or handle errors
    pass

def get_random_sub_breed_image(breed, sub_breed):
    # 3. Get a random image from a sub-breed
    #Handling connection errors when calling the API
    """GET request to fetch a random image from a sub-breed."""
    try:
        response = requests.get("https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random")
        response.raise_for_status()
        data = response.json()
        if data["status"] == "success":
            return data["message"]
        else:
            print(f"API error: {response}")
            return None
    except requests.exceptions.RequestException as e:
        print("could not fetch images for that sub-breed: {e}")
        return None
    # TODO: Make a request to https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random
    # TODO: Return the image URL or handle errors
    pass

def show_breeds(breeds_dict):
    """Prints all available breeds 5 per line."""
    # TODO: Print all breeds (sorted), 5 per line
    #Building logic to loop through all breeds
    #build conditional statments 
    breeds = sorted(breeds_dict.keys())

    for i in range(0, len(breeds), 5):
        print(", ".join(breeds[i:i+5]))
    pass

def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Show all breeds")
        print("2. Get a random image from a breed")
        print("3. Get a random image from a sub-breed")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            breeds = get_all_breeds()
            show_breeds(breeds)

        elif choice == "2":    
            breeds = get_random_sub_breed_image()
            breed = input("Enter breed name: ").strip().lower()
            if breed in breeds:
                image_url = get_random_sub_breed_image(breed)
                if image_url:
                    print(f'\nRandom image of a {breed}: {image_url}')
            # TODO: Check if breed exists and fetch image
            # TODO: Print image URL or error message
        elif choice == "3":
            get_all_breeds()
            breed = input("Enter breed name: ").strip().lower()
            # TODO: Check if breed has sub-breeds
            # TODO: Ask for sub-breed, check if valid, then fetch image
            # TODO: Print image URL or error message

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
