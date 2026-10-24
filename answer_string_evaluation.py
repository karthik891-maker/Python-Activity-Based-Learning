key = ["A", "C", "B", "D", "A"]
answers = []
for i in range(len(key)):
    answers.append(input("Answer for question " + str(i + 1) + ": ").strip().upper())
correct = incorrect = blank = 0
score = 0
for i in range(len(key)):
    if answers[i] == "":
        blank += 1
    elif answers[i] == key[i]:
        correct += 1
        score += 1
    else:
        incorrect += 1
        score -= 0.25
print("Correct:", correct)
print("Incorrect:", incorrect)
print("Unanswered:", blank)
print("Final score: {:.2f} out of {}".format(score, len(key)))
