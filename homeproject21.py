empty_list = []

marks = [85, 92, 78, 65, 90]
print("Marks List:", marks)



sample = [50, 60]
repeated = sample * 3
print("Repeated Sample List:", repeated)




print("Number of Marks:", len(marks))




print("First Mark:", marks[0])
print("Last Mark:", marks[-1])




print("First Three Marks:", marks[0:3])
print("Reversed Marks:", marks[::-1])




def check_first_last(mark):
    mark = str(mark)
    if mark[0] == mark[-1]:
        return True
    return False

print("\nChecking First and Last Digits:")

for mark in marks:
    if check_first_last(mark):
        print(mark, "-> First and last digits match")
    else:
        print(mark, "-> First and last digits do not match")



total = 0
for mark in marks:
    total += mark

print("\nTotal Marks:", total)




average = total / len(marks)

sorted_marks = sorted(marks)

smallest = sorted_marks[0]
largest = sorted_marks[-1]

print("Average Marks:", average)
print("Smallest Mark:", smallest)
print("Largest Mark:", largest)



print("\nProgram Complete!")