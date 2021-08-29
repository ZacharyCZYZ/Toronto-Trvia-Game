import random
import json

print("Welcome to Toronto-Pearson (CYYZ) airport trivia!")

# Read questions file
with open('./questions.json', 'r') as file:
    questions = file.read()

questions = json.loads(questions)
num_of_questions = len(questions)
score = 0

# Shuffle questions
random.shuffle(questions)

for question in questions:
    if input(question["question"] + "\n").lower() == question["answer"].lower():
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")

    print("\n")

print(f"Thanks for playing! You got {score} questions correct.")
print(f"Mark: { '{:.1%}'.format(score / num_of_questions) }%")
