# for loop
fruits = ["apple", "mango", "orange"]
for fruit in fruits:
    print(fruit)
    print(fruit+"Pie")

# Average height
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)

total_height = 0
count = 0
for height in student_heights:
    total_height += height
    count += 1

avg_height = total_height/count
print(avg_height)

# higest score
student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(highest_score)
