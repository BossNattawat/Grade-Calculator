subject_list = []
grade_list = []
w_list = []

while True:
    print()
    subject = input("Enter the subject (or 'n' to finish): ")
    
    if subject.lower() == "n":
        break
    
    grade = float(input("Enter the grade: "))
    weight = float(input("Enter the weight: "))
    print()
    
    subject_list.append(subject)
    grade_list.append(grade)
    w_list.append(weight)

# Calculate the GPA
sum_temp = [grade_list[i] * w_list[i] for i in range(len(grade_list))]
sum_grades = sum(sum_temp)
w_sum = sum(w_list)

result = sum_grades / w_sum

# Display the results
print("\n_________________ Result _________________\n")

for i in range(len(subject_list)):
    print(f"\t{i + 1}. {subject_list[i]} : {grade_list[i]}")
    
print("\n__________________________________________\n")
print(f"\tGPA : {result:.2f}")
print()
