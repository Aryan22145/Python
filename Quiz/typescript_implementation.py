from Quiz.questions import typescript_questions, typescript_answers

questions = ["one", "two", "three", "four", "five",
             "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]


def typescript_quiz():
    final_score = 0
    for i in questions:
        print(typescript_questions[i])
        a_1 = int(input("Enter your choice: "))
        if a_1 == typescript_answers[i]:
            final_score += 1

    print("-" * 50)
    print(f"Your final score for this session is {final_score}")


if __name__ == "__main__":
    typescript_quiz()
