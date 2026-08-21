
student_1 = {"name":"Aishwarya", "score": 95}
student_2 = {"name":"Arjun", "score": 85}
student_3 = {"name": "Ashvik", "score": 75}
student_4 = {"name": "John", "score": 65}
student_5 = {"name": "Annie", "score": 55}


score_1 =  student_1.get("score")
score_2 = student_2.get("score")
score_3 = student_3.get("score")
score_4 = student_4.get("score")
score_5 = student_5.get("score")

print ("Class average:", ((score_1 + score_2 + score_3 +  score_4 + score_5)/5))

print()
print("Below are the studnet details:")
print(student_1)

print(student_2)

print(student_3)

print(student_4)

print(student_5)



