#! /bin/python3

import json 

def fav_number(): 
    filename = 'favnumber.json' 
    try: 
        with open(filename) as f: 
            favnumber = json.load(f)
    except FileNotFoundError: 
        favnumber = input("Input your favorite number: ") 
        with open(filename, 'w') as f: 
            json.dump(favnumber, f) 
            print(f"Come back later to see if we remember.") 
    else: 
        print(f"We remember your favorite number is {favnumber}.") 

fav_number()
