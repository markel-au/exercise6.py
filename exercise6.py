import random
import time
from random import randint
from typing import Any


class Restaurant:
    """Restaurant items and name"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """Print both the restaurant name and cuisine type"""
        greeting = f"Welcome to {self.restaurant_name} one of our signature cuisines is {self.cuisine_type}"
        return greeting

    def open_restaurant(self):
        """State the the restaurant is open and give hours"""
        open_during =  f"{self.restaurant_name} is currently open and our store hours are Monday through Saturday from 8:00am to 12am. "
        return open_during


restaurant_details = Restaurant('Spill the Beans', 'Ice Cream')
print(restaurant_details.describe_restaurant())
print(restaurant_details.open_restaurant())


class IceCreamShop:
    """Restaurant items and name"""

    def __init__(self, shop_name, dish_type, options):
        """Initialize attributes to describe restaurant"""
        self.shop_name = shop_name
        self.dish_type = dish_type
        self.options = options

    def describe_restaurant(self):
        """Print both the restaurant name and cuisine type"""
        greeting = f"\nWelcome to {self.shop_name} one of our signature cuisines is {self.dish_type}"
        return greeting

    def open_restaurant(self):
        """State the the restaurant is open and give hours"""
        open_during =  f"{self.shop_name} is currently open and our store hours are Monday through Saturday from 8:00am to 12am. "
        return open_during
    def guest_options(self):
        """Give the guest their options of choices for Ice Cream"""
        flavor_options = f"Here at {self.shop_name} we have a three options of ice cream including {self.options}"
        return flavor_options

welcome_to_shop = IceCreamShop('Spill the Beans', 'Ice Cream', 'Vanilla, Strawberry, and Chocolate')
print(welcome_to_shop.describe_restaurant())
print(welcome_to_shop.open_restaurant())
print(welcome_to_shop.guest_options())


class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

    def describe_flavors(self,*flavors):
        print(f'{self.restaurant_name} has the following flavors:')
        for self.flavor in flavors:
            print(f'-{self.flavor}')

restaurant = IceCreamStand('DQ','ice cream')
restaurant.describe_restaurant()
restaurant.describe_flavors('Chocolate','Mango', 'Raspberry', 'Coffee', 'Vanilla')

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





