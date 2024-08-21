subject_list = []
grade_list = []
w_list = []
sum_temp = []
w_sum = 0
sum = 0
result = 0

while True:
    print()
    print()
    subject = input("Subject : ")
    
    if subject == "n":
        break
    
    grade = float(input("Grade : "))
    weight = float(input("Weight : "))
    print()
    
    subject_list.append(subject)
    grade_list.append(grade)
    w_list.append(weight)
    

for i in range(len(grade_list)):
    sum_temp.append(grade_list[i] * w_list[i])
    
for k in range(len(sum_temp)):
    sum += sum_temp[k]
    
for j in range(len(w_list)):
    w_sum += w_list[j]
    
result = float(sum / w_sum)

print("_________________ Result _________________")
print()

for i in range(len(subject_list)):
    print("\t")
    print(f"\t{i + 1}. {subject_list[i]} : {grade_list[i]}")
    print("\t")
    
print("__________________________________________")

print()
print(f"\tGPA : {result}")
print()
