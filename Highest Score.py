# Take the list as string and make a list using split function
student_scores = input("Input a list of student score ").split()
for score in range(0,len(student_scores)): #Convert string list to int list
    student_scores[score] = int(student_scores[score])

max =0
for score in student_scores: #find the maximum number
    if score>max:
        max = score
print(f"The height score in the class is: {max}")
