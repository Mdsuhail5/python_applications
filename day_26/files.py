with open(r"day_26\file1.txt") as f1:
    f1_content = f1.readlines()

with open(r"day_26\file2.txt") as f2:
    f2_content = f2.readlines()

# Convert the content to integers and strip newlines
l1 = [int(n.strip()) for n in f1_content]
l2 = [int(n.strip()) for n in f2_content]

# Find common elements
result = [x for x in l1 if x in l2]
print(result)
