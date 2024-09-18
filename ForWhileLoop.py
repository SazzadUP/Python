### Break, Continue

nums = [1, 2, 3, 4, 5]
 
#for num in nums:
#   if num == 3:
#      print('Found!')
#      continue                     ##break or continue keywords
#   print(num)  

#### Loop within a loop

#for num in nums:
#	for letter in 'abc':
#		print(num, letter)

#### go through a loop in certain number of time, we use range function.

#for i in range(10):
#for i in range(1,11):                #if we want to start from 1 and end in 10, last number doesn't include	
#	print(i)

### While loop, it will run until it meets certain condition

#x = 0
#while x < 10:
#	print(x)
#	x +=1

###while loop with if statement

#while x < 10:
#	if x == 5:
#		break
#	print(x)
#	x += 1	


### Create an infinite loop
#x = 0
#while True:
#	print(x)
#	x += 1