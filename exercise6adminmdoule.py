class Admin:

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

    def describe_permissions(self, *privileges):
        print(f"\nHello {self.first_name} {self.last_name} your privileges are: ")
        for self.privilege in privileges:
            print(f'{self.privilege}')

welcome_user = Admin('Markel', 'Samuel')
welcome_user2 = Admin('Brandon', 'Grech')
welcome_user3 = Admin('Matthew', 'Saul')
show_privileges = Admin.describe_permissions(welcome_user, 'Can post','Can delete post', 'Can ban user')
show_privileges2 = Admin.describe_permissions(welcome_user2, 'Can post','Can delete post', 'Can ban user')
show_privileges3 = Admin.describe_permissions(welcome_user3, 'Can post','Can delete post', 'Can ban user')
