question = open("questions.txt", "r")
ques = [line.strip() for line in question.readlines()]
question.close()
score = 0
total = len(ques)

for line in ques:
    q, a = line.split('=')  # split equation with `=` into question and answer
    ans = input(f"Enter ans: {q}=")    # print question and wait for user to input their answer
    if a == ans:    # if user input matches answer
        score += 1  # increase sc

result = open("result.txt", "w")
result.write(f"Your final score is {score}/{total} ")
