class User:

    def __init__(self, first_name, last_name):
        """Ask the user for their first and last name"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        prompt_user = f"\nYour name first name is {self.first_name} and your last name is {self.last_name}."
        return prompt_user

    def greet_user(self):
        prompt_greeting = f"Hello {self.first_name} {self.last_name} welcome to your OS."
        return prompt_greeting

welcome_user = User('Markel', 'Samuel')
welcome_user2 = User('Brandon', 'Grech')
welcome_user3 = User('Matthew', 'Saul')
print(welcome_user.describe_user())
print(welcome_user.greet_user())
print(welcome_user2.describe_user())
print(welcome_user2.greet_user())
print(welcome_user3.describe_user())
print(welcome_user3.greet_user())
