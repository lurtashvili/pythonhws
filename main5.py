
dictionary = {} 

def add_word():
    word = input("Enter a word: ").lower() 
    if word in dictionary:
        print("This word already exists in the dictionary.")
    else:
        definition = input("Enter the definition: ") 
        dictionary[word] = definition 
        print(f"{word} has been added to the dictionary.")


def search_word():
    word = input("Enter a word: ").lower() 
    if word in dictionary: 
        definition = dictionary[word]
        print(f"The definition of {word} is: {definition}")
    else:
        print("This word is not in the dictionary.")


def show_dict():
    if dictionary:
        print("The dictionary contains the following words and definitions:")
        for word, definition in dictionary.items(): 
            print(f"{word}: {definition}")
    else:
        print("The dictionary is empty.")

def remove_word():
    word = input("Enter a word: ").lower() 
    if word in dictionary:
        dictionary.pop(word)
        print(f"{word} has been removed from the dictionary.")
    else:
        print("This word is not in the dictionary.")

quiz_questions = {
    "What is the capital of France?": ["Berlin", "Paris", "Madrid", "Rome"],
    "How many continents are there?": [5, 6, 7, 8],
    "What is the square root of 81?": [8, 9, 10, 11],

}


def take_quiz():
    score = 0 
    for question, options in quiz_questions.items(): 
        print(question) 
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}") 
        answer = int(input("Enter your answer: "))
        if answer > 0 and answer <= len(options):
            if options[answer - 1] == options[1]: 
                print("Correct!")
                score += 1 
            else:
                print("Wrong!")
        else:
            print("Invalid answer.")
    print(f"Your score is {score} out of {len(quiz_questions)}.")


while True:
    print("Welcome to the dict app. Choose an option from the menu:")
    print("1. Add a word and its definition")
    print("2. Search for the definition of a word")
    print("3. Show the entire dictionary")
    print("4. Remove a word and its definition")
    print("5. Take the quiz")
    print("6. Exit the program")
    choice = int(input("Enter your choice: "))
    if choice == 1: 
        add_word()
    elif choice == 2:
        search_word()
    elif choice == 3: 
        show_dict()
    elif choice == 4: 
        remove_word()
    elif choice == 5:
        take_quiz()
    elif choice == 6: 
        print("Thank you for using this app")
        break
    else: 
        print("Invalid choice. Please try again.")
