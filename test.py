###########

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "¿A qué corresponde el acrónimo 'mg'?\n(a) muy gracioso\n(b) más gaseosa\n(c) muchas gracias\n",
    "¿A qué corresponde el acrónimo 'atp'?\n(a) a todas partes\n(b) ante todo paciencia\n(c) aunque te pese\n",
    "¿A qué corresponde el acrónimo 'caqns'?\n(a) cuéntame algo que no sepa\n(b) castiga a quien no sude\n(c) cachopo a quincenas nunca sobra\n"

]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Has acertado " + str(score) + " de " + str(len(questions)) + ".")

run_test(questions)

###########
