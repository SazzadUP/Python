########Dictionaries: allow us to work with key-value pairs

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}   #name/age/courses are KEYS and John/25/[] are values here
#print(student)                                                          #Print all keys and values
#print(student['courses'])                                                  #print a value of one key
#print(student['phone'])                                                  #if key doesn't exists and we want value then gives error
#print(student.get('name'))
#print(student.get('phone'))                                              #if key doesn't exists and we want value then we can use get function, which gives buit in value NONE
#print(student.get('phone', 'Not found'))                                 #the key phone doesn't found but return the value NOT FOUND,as it is defined

################### include a new key in the dictionary
#student['phone'] ='555-5555'
#print(student.get('phone'))

############update values
#student['name'] = 'Jane'                                   #update the key NAME here
#print(student)

################## update value with update method
#student = {'name': 'John', 'age': 28, 'courses': ['Math', 'CompSci']}
#student.update({'name': 'Jane', 'age': 26, 'phone': '5464-5889'})
#print(student)

################### delete a value
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
#del student['age']                                             #delete the kye age
#print(student)

#age = student.pop('age')                                       #delete the age key but show the value
#print(student)
#print(age)


###############
#print(len(student))
#print(student.keys())
#print(student.values())
#print(student.items())     #shows the keys and values together

###########################
for key in student:
	print(key)


#for key,value in student.items():
#	print(key, value)
