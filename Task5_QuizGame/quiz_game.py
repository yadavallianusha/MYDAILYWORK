# Function to load quiz questions
def load_questions():
    return [
        {
            "question": "What is the capital of India?", # Question text
            "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
            "answer": "B"# Correct answer
        },
        {
            "question": "Which language is used for web development?",
            "options": ["A. Python", "B. HTML", "C. Java", "D. C"],
            "answer": "B" # Correct answer
        },
        {
            "question": "Who is known as the father of computers?",
            "options": ["A. Charles Babbage", "B. Alan Turing", "C. Bill Gates", "D. Steve Jobs"],
            "answer": "A" # Correct answer
        }
    ]

# Function to start and play the quiz
def play_quiz():
    # Display welcome message
    print("Welcome to the Quiz Game ")
    print("Rules:") # Display rules
    print("1. Each correct answer gives you 1 point")
    print("2. No negative marking")
    print("3. Choose A, B, C or D\n")

    questions = load_questions()  # Load questions
    score = 0   # Initialize score
 # Loop through each question
    for q in questions:
        print(q["question"])
         # Print all options
        for option in q["options"]:
            print(option)
         # Take user answer and convert to uppercase
        user_answer = input("Enter your answer (A/B/C/D): ").upper()
          # Check answer
        if user_answer == q["answer"]:
            print(" Correct!\n")
            score += 1  # Increase score
        else:
            print(" Incorrect!")
            print("Correct Answer:", q["answer"], "\n")
    # Display final score
    print(" Quiz Completed!")
    print("Your Final Score:", score, "/", len(questions))
    # Performance message based on score
    if score == len(questions):
        print("Excellent Performance ")
    elif score >= len(questions) // 2:
        print("Good Job ")
    else:
        print("Better Luck Next Time ")

# Main loop to allow replaying the quiz
while True:
    play_quiz() # Start quiz
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thank you for playing the Quiz Game ")
        break
