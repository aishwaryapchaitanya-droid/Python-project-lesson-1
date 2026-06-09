#take marks as input from user
print("Enter marks obtained in each subject: ")
math = int(input("maths: "))
science = int(input("science: "))
english = int(input("english: "))
hindi = int(input("hindi: "))

#Calculating the percentage of marks
sum = math+science+english+hindi
print("sum of math, science, english and hindi = ", sum)

perc = (sum/400) *100
print("percentage = ", perc)