
#def hello_func():        #empty braces where the parameters will go
#	pass                 #if we want to fill th function later then we can use pass keywords
#print(hello_func())

### Function allow us to reuse code without repeating ourselves

#def hello_func():
#	print ('Hello Function')
#hello_func()	

# Keeping your code DRY! (Don't Repeat Yourself!)
#def hello_func():
#	return 'Hello Function'

#print(hello_func())
#print(len('Test'))
#print(hello_func().upper())

#############Pass Arguments to our function

#def hello_func(greeting):
#	return '{} Function'.format(greeting)
#print(hello_func('Hi'))

#def hello_func(greeting, name = 'You'):
#    return '{}, {}'.format(greeting, name)
#print(hello_func('Hi', name = 'Sazzad'))  

#def student_info(*args, **kwargs):
#	print(args)
#	print(kwargs)
#student_info('Math', 'Art', name= 'John', age= 22)

#courses = ['Math', 'Art']
#info = {'name' : 'John', 'age' : 22}
#student_info(*courses, **info)


#############NUmber of days per month. First value place hokder for indexing purposes.

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
	"""Return TRue for leap year, False fpr non-leap year."""    #"""" called DOC STRING
	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month (year, month):
    #"""Return number of days in that month in the year.""""                                                                  

    if not 1 <= month <= 12:
    	return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29

    return month_days[month]    	


#print(is_leap(2020))    
print (days_in_month(2017,2))





























