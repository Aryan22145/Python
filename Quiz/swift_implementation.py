from Quiz.questions import swift_questions, swift_answers

questions = ["one", "two", "three", "four", "five",
             "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]


def swift_quiz():
    final_score = 0
    for i in questions:
        print(swift_questions[i])
        a_1 = int(input("Enter your choice: "))
        if a_1 == swift_answers[i]:
            final_score += 1

    print("-" * 50)
    print(f"Your final score for this session is {final_score}")


if __name__ == "__main__":
    swift_quiz()
