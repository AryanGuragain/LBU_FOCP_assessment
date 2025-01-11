'''A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
 first count the sweets and then divide them according to how many pupils attend that
 day. Write a program that will tell the teacher how many sweets to give to each pupil,
 and how many she will have left over
'''

sweets=int(input("Number of sweets in the tub? "))
students=int(input("Total number of students? "))
sweets_per_student=sweets//students
left=sweets%students
print(f"Each student will get {sweets_per_student} sweets and there will be {left} sweets left over")