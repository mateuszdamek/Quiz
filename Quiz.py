import os
import time
filepath = "C:\\Users\\loombard\\Documents\\GitHub\\Quiz\\quiz.txt"
f = open(filepath, "r", encoding= "utf-8")

answers = ['c','a','b','a','c','b','c','b','a','b']
your_answers = []
questions = 0
score = 0
good_answer = 0
start = 0

while(questions < 10):
    for steps in range(0, 5):
        lines = f.readline()
        print(lines, end="")
    your_answers.append(input("\nYour answer: "))

    for i in range(start, len(your_answers)):
        if(your_answers[i] == answers[i]):
            good_answer += 1
            score += 1
        i += 1
    
    print(f"Good answers: {good_answer}/10")
    start +=1
    questions += 1

    time.sleep(2)
    os.system("cls")

print("Conglatulations!")
print(f"Your's score: {score}")




    






