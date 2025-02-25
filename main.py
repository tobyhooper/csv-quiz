import csv
import random

def quiz(csv_file_path, quiz_name):
    # Read the CSV file
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        approaches = list(csv.DictReader(csvfile))
    
    # Extract all approach names and determine the number of questions
    all_approaches = [item["Term"] for item in approaches]
    num_questions = len(approaches)
    
    # Handle empty CSV case
    if num_questions == 0:
        print("No questions found in the CSV file.")
        return 0
    
    # Determine the number of options per question (up to 4)
    num_options = min(4, len(all_approaches))
    
    # Shuffle the questions
    random.shuffle(approaches)
    score = 0
    
    # Display welcome message
    print(f"\nWelcome to the {quiz_name} Quiz!")
    print(f"There are {num_questions} questions.")
    print(f"For each question, choose the correct approach from {num_options} options.")
    print("Let’s begin!\n")
    
    # Run the quiz
    for item in approaches:
        correct_answer = item["Term"]
        
        # Prepare options
        if num_options == 1:
            options = [correct_answer]
        else:
            incorrect_options = random.sample(
                [a for a in all_approaches if a != correct_answer], num_options - 1
            )
            options = [correct_answer] + incorrect_options
            random.shuffle(options)
        
        # Display the question and options
        print("Definition:", item["Definition"])
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        # Get user input with validation
        while True:
            try:
                user_choice = int(input(f"Choose the correct approach (1-{num_options}): "))
                if 1 <= user_choice <= num_options:
                    break
                else:
                    print(f"Please enter a number between 1 and {num_options}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Check the answer
        selected_option = options[user_choice - 1]
        if selected_option == correct_answer:
            score += 1
            print("Correct! + 1 point.")
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}. - 1 points.")
            score -= 1
        print()
    
    # Display final score
    print(f"Quiz complete! Your score is {score} out of {num_questions}.")
    return score

file = input("Enter the csv file name (e.g., data.csv)\n: ")
name = input("Enter the quiz name (e.g., Data)\n: ")
quiz(file, name)
