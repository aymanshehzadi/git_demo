salary=input("enter salary  ")
gender=raw_input("enter gender  ")
if salary<10000:
	if gender=='male':
		salary=salary+0.07*salary
	elif gender=='female':
		salary=salary+0.12*salary

else:
	if gender=='male' :
	 	salary= salary+0.05*salary
 	elif gender=='female' :
		salary= salary+0.10*salary
print "salary of employee is : ",salary
	




