#! /bin/python3

def count_words(filename): 
    """Count the approximate number of words in a file."""
    try: 
            with open(filename, encoding='utf-8') as f: 
                contents = f.read()
    except FileNotFoundError: 
        pass
    else: 
        words = contents.split()
        print(words) 
        num_words = len(words) 
        print(f"The file {filename} has about {num_words} words.")

filenames = ['dog.txt', 'cat.txt'] 
for filename in filenames: 
    count_words(filename)
    
