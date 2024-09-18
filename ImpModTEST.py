
#import ImportModules
#import ImportModules as mm            #To import file with short name
#courses = ['HIstory', 'Math', 'Physics', 'CompSci']

#index = ImportModules.find_index(courses, 'Math')
#index = mm.find_index(courses, 'Math')
#print(index)

########## Find directly index from the imported file, it only give access in find_index part not the test part from imported file
#from ImportModules import find_index, test
#from ImportModules import find_index as fi, test
#from ImportModules import *
#courses = ['HIstory', 'Math','Physics','CompSci']

#index = fi(courses, 'Social')
#index =find_index(courses, 'Math')
#print(index)
#print(test)
 


#from ImportModules import find_index, test
#import sys
#courses = ['History', 'Math', 'Physics', 'CompSci']

#index = find_index(courses, 'Math')

#print(sys.path)

############Common Standard Libraries
#import random
#import math
#courses = ['History','Math','Physics','CompSci']
#random_course = random.choice(courses)
#rads = math.radians(90)
#print(random_course)
#print(math.sin(rads))



import datetime
import calendar

courses = ['History','Math','Physics','CompSci']

today = datetime.date.today()
print(today)
print(calendar.isleap(2020))


import os 

print(os.getcwd())
print(os.__file__)

import antigravity
















