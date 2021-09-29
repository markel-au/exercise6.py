import json

def greet_user():
    """Greet the user by name."""
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"Is {username} the correct username?")
    else:
        print(f"Welcome back, {username}!")

