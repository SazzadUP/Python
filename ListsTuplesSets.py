#########################Lists, Tuples allow us to work with sequential data. Sets are unordered colletion of values with no duplictaes.

#courses = ['History', 'Math','Physics','CompSci']
#print(len(courses))                                          #find the values in list
#print(courses)
#print(courses[0])                                             #find the index in a list/index
#print(courses[-1])                                             #find always the last value of the index/list
#print(courses[0:2])                                            #return the value 2 value

#########################################Add a value in list
#courses = ['History', 'Math', 'Physics', 'CompSci']
#courses.append('Bio')                                            #append always add at the end
#courses.insert(0, 'Art')                                         #insert takes 2 arguments.First takes index and then the value itself.
#print(courses)
###############################################################
#courses = ['History', 'Math', 'Physics', 'CompSci']
#courses_2 = ['Art', 'Education']
#courses.extend(courses_2)                                                      #extend is used to add multiple values
#print(courses)
###############################################################
#courses = ['History', 'Math', 'Physics', 'CompSci']
#courses.remove('Math')
#print(courses)

#courses.pop()
#print(courses)                                                                    #pop normally remove the last value of the list

#popped = courses.pop()
#print(courses)
#print(popped)
#################################################################
courses = ['History', 'Math', 'Physics', 'CompSci']
#courses.reverse()                                                             #to reverse th value
#print(courses)

#courses.sort()                                                                #to sort the values in alphabetical order
#print(courses)

#nums = [1,5,2,4,3]
#nums.sort()
#print(nums)

#courses.sort(reverse=True)                                                     #to sort the values in alphabetical order but from reverse
#nums.sort(reverse=True)
#print(courses)
#print(nums)


#sorted_courses = sorted(courses)                                                #without altering the original version it will created the sorted version
#print(sorted_courses)
#nums = [5,11,2,25,10]
#nums.sort()                                                                   #numbers are sorted in ascending order
#nums.sort(reverse=True)                                                        #numbers are sorted in descending order
#print(courses)
#print(nums)

#nums = [5,11,2,25,10]
#print(min(nums))   #print the minimum value of the list
#print(max(nums))   #print the maximum value of the list
#print(sum(nums))   #print the sum of the list

#courses =['History', 'Math', 'Physics', 'CompSci']
#print(courses.index('Math'))   #find the index of value int the list
#print ('Math' in courses)        #find if the value in in the list

#for item in courses:                   #only show the value in ne wline
#	print (item)


#for index, item in enumerate(courses):                        #idex and the value
#	print(index, item)

#for index, item in enumerate(courses, start=1):                #idex and value but start from 1
#	print (index, item)

#course_str = ', '.join(courses)           #list to string with join function
#new_list = course_str.split(' - ')        #string into list with split function
#print(course_str)
#print(new_list)               



#Tuples :we can't modify. immutable
#List   :we can modify, mutable

################################Mutable
#list_1 = ['HIstory', 'Math', 'Physics', 'CompSci']     #In list we use third bracket
#list_2 =list_1

#print(list_1)
#print(list_2)

#list_1[0]='Art'
#print(list_1)
#print(list_2)

######################Immutable
#tuple_1 = ('HIstory', 'Math', 'Physics', 'CompSci')    # In tuple we use first bracket
#tuple_2 = tuple_1

#print(tuple_1)
#print(tuple_2)

#tuple_1[0] = 'Art'    #Not possible, because immutable

#print(tuple_1)
#print(tuple_2)



################Sets: are values that are un-ordered and have no duplicates
#cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}  #Sets use second bracet, mostly uses to remove the duplicate
#print(cs_courses)
#print('Math' in cs_courses)                        #will show whether a value is in the sets

#cs_courses = {'History', 'Math', 'Physics', 'CompSci'}              
#art_courses = {'History', 'Math', 'Art', 'Design'}
#print(cs_courses.intersection(art_courses))                   #show the common value with intersection function
#print(cs_courses.difference(art_courses))                     #show the values that are in cs_courses but not in art_courses with difference function
#print(cs_courses.union(art_courses))                          #show all the values with union function

######################################CReate Empty lists,tuples or Sets

##Empty Lists
empty_list =[]
empty_list = list()

##Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

##Empty Sets
empty_set = {}            #This isn't right! It's a dictionary
empty_set = set()













































































