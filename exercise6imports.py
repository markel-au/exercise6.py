from exercise6 import IceCreamShop
from exercise6adminmdoule import Admin
from exercise6usermodule import User

welcome_to_shop = IceCreamShop('Spill the Beans', 'Ice Cream', 'Vanilla, Strawberry, and Chocolate')
print(welcome_to_shop.describe_restaurant())
print(welcome_to_shop.open_restaurant())
print(welcome_to_shop.guest_options())

welcome_user = Admin('Markel', 'Samuel')
welcome_user2 = Admin('Brandon', 'Grech')
welcome_user3 = Admin('Matthew', 'Saul')
show_privileges = Admin.describe_permissions(welcome_user, 'Can post','Can delete post', 'Can ban user')
show_privileges2 = Admin.describe_permissions(welcome_user2, 'Can post','Can delete post', 'Can ban user')
show_privileges3 = Admin.describe_permissions(welcome_user3, 'Can post','Can delete post', 'Can ban user')


welcome_user = User('Markel', 'Samuel')
welcome_user2 = User('Brandon', 'Grech')
welcome_user3 = User('Matthew', 'Saul')
print(welcome_user.describe_user())
print(welcome_user.greet_user())
print(welcome_user2.describe_user())
print(welcome_user2.greet_user())
print(welcome_user3.describe_user())
print(welcome_user3.greet_user())
