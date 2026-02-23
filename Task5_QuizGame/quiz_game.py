def load_questions():
    return [
        {
            "question": "What is the capital of India?",
            "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
            "answer": "B"
        },
        {
            "question": "Which language is used for web development?",
            "options": ["A. Python", "B. HTML", "C. Java", "D. C"],
            "answer": "B"
        },
        {
            "question": "Who is known as the father of computers?",
            "options": ["A. Charles Babbage", "B. Alan Turing", "C. Bill Gates", "D. Steve Jobs"],
            "answer": "A"
        }
    ]


def play_quiz():
    print("Welcome to the Quiz Game ")
    print("Rules:")
    print("1. Each correct answer gives you 1 point")
    print("2. No negative marking")
    print("3. Choose A, B, C or D\n")

    questions = load_questions()
    score = 0

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print(" Correct!\n")
            score += 1
        else:
            print(" Incorrect!")
            print("Correct Answer:", q["answer"], "\n")

    print(" Quiz Completed!")
    print("Your Final Score:", score, "/", len(questions))

    if score == len(questions):
        print("Excellent Performance ")
    elif score >= len(questions) // 2:
        print("Good Job ")
    else:
        print("Better Luck Next Time ")


while True:
    play_quiz()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thank you for playing the Quiz Game ")
        break
