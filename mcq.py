from question import Question
question_prompts=[
    "what color are apples?\n(a) Red/Green\n (b) Purple\n(c) Orange\n\n",
    "what color are Bananas?\n(a) Teal\n (b) Green\n(c) Yellow\n\n",
    "what color are strawberries?\n(a) Yellow\n (b) Red\n(c) Blue\n\n"
]

#list of qns objects
questions=[
    Question(question_prompts[0],"a"),#qns object
    Question(question_prompts[1],"c"),#qns object
    Question(question_prompts[2],"b")#qns object

]
def run_test(questions):
    score= 0
    for question in questions:
        answer= input(question.prompt)
        if answer== question.answer:
            score+= 1
    print("You got"+ str(score))

run_test(questions)