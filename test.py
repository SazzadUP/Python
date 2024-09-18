
 #Print Welcome Message
#print('Hello World')

#a = (1,2)
#b = (5,6)
#r = a + b
#print(r)

#from collections import deque
#queue = deque()

#queue.append('a')
#queue.append('b')
#queue.append('c')

#print(queue.popleft())

#################################

#class Magic:
#	def ___init___(self, number):
#		self.number = number

#	def ___mul___(self, other):
#		return Magic(self.number * other.number)

#	def ___eq___(self, other):
#	    return self.number == other.number

#print(Magic(5) * Magic(10) == Magic(15))
##################################
#def countdown(n):
#	while n > 0:
#		yield n 
#		n -= 1
#numbers = countdown(3)		
#print(next(numbers))
##################################
import calendar
yy = 2024
mm = 4

print(calendar.month(yy, mm))k