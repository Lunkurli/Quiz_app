from Question import Question

question_prompts = ["Which of these is a Machine Learning Algorithm?\n(a)Linear Regression\n(b) Pandas\n(c) Javascript\n\n",
                   "Which of these is a web development framework written in python?\n(a) Electron\n(b) Angular\n(c) Django\n\n",
                   "Which of these is a programming language?\n(a) Django\n(b) Python\n(c) Scikit-learn\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            print("You got " + str(score) + "/" + str(len(questions)) + "Correct")



run_test(questions)
