student_xinxibiao=['玛卡巴卡']
student_chengjibiao={'玛卡巴卡':'数学:99'}
class Student:
	def __init__(self,student_name,student_number,exam_number):
		self.name=student_name
		self.student_number=student_number
		self.exam_number=exam_number
	def student_xinxi(self):
		student_xinxibiao.append(self.student_name)
	def chengji_1(self):
		student_chengjibiao[self.name]=self.exam_number
print("1.增加")
print("2.删除")
i=int(input("你要的功能"))
if i==1:
	count=True
	while count:
		t1=Student(input("姓名"),int(input("学号")),input("课程成绩："))
		t1.chengji_1()
		t1.student_xinxi()
		continue_1=input("你是否要继续输入 yes or no")
		if continue_1=="no":
			count=False
			print(f"学生{student_xinxibiao}")
			print(f"成绩{student_chengjibiao}")
if i==2:
	print(f"现在这里有这些学生{student_xinxibiao}")
	print(f"各个学生对应的成绩{student_chengjibiao}")
	del_student_1=input("你要删除的学生信息以及成绩输入名字即可")
	for del_student_2 in student_xinxibiao:
		if (del_student_2==del_student_1):
			print(f"{del_student_1}存在")
			student_xinxibiao.remove(del_student_1)
			del student_chengjibiao[del_student_1]
			print(f"现在这里有这些学生{student_xinxibiao}")
			print(f"各个学生对应的成绩{student_chengjibiao}")
		if(del_student_2!=del_student_1):
			print(f"{del_student_1}不存在")
			
		
			
	
	
	