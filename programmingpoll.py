#! /bin/python3

filename = 'programmingpoll.txt'

print("Enter 'quit' when you are finished. ") 
while True: 
    question = input("\nWhy do you like programming? ") 
    if question == 'quit': 
        break 
    else: 
        with open(filename, 'a') as f: 
            f.write(f"{question}\n") 
        print(f"Your answer {question} has been recorded")

