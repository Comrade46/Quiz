class QuizGame:
    def __init__(self):
        # Initialize quiz questions, options, and answers
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
                "answer": "C"
            },
            {
                "question": "What is 2 * 5?",
                "options": ["A) 13", "B) 10", "C) 5", "D) 6"],
                "answer": "B"
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "options": ["A) Charles Dickens", "B) J.K. Rowling", "C) William Shakespeare", "D) Mark Twain"],
                "answer": "C"
            },
            {
                "question": "What is the smallest planet in our solar system?",
                "options": ["A) Venus", "B) Earth", "C) Mars", "D) Mercury"],
                "answer": "D"
            }
        ]
        self.score = 0

    def play(self):
        # Start the quiz game
        print("Welcome to the Quiz Game! Let's start.")
        for i, q in enumerate(self.questions):
            print(f"\nQuestion {i + 1}: {q['question']}")
            for option in q["options"]:
                print(option)

            user_answer = input("Your answer (A, B, C, or D): ").strip().upper()

            if user_answer == q["answer"]:
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {q['answer']}.")

        # Show the final score
        print(f"\nQuiz Over! Your final score is: {self.score} out of {len(self.questions)}")

# Initialize and start the quiz
quiz = QuizGame()
quiz.play()

