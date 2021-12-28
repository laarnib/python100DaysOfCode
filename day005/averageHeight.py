#You are going to write a program that calculates the average student height from a List of heights.

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum = 0
height_count = 0
average = 0

for height in student_heights:
    sum += height
    height_count += 1

average = round(sum / height_count)
print(average)