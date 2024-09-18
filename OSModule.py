
import os

#print(dir(os)) #all of the attributes and methods that we have access to within this module
#print(os.getcwd())    #will print current directory

#os.chdir('/home/sazzad/')  #to change in another directory
#print(os.getcwd())
#print(os.listdir())        #to see what file and folders in the directory

###create a new folder in the desktop
#os.mkdir('pythonfolder3')                      #create only main directory
#os.makedirs('pythonfolders2/bacchafolder')      #create main and sub directory together
#print(os.listdir())

###remove directory
#os.rmdir('pythonfolder')
#os.removedirs('pythonfolders2/bacchafolder')
#print(os.listdir())

#rename a file or folder
#os.rename('file2', 'file')
#print(os.listdir())

#print(os.stat('file'))   #print the information of the file
#print(os.stat('file').st_size)   #print size of the file
#print(os.stat('file').st_mtime)           #print the last modification time      

#from datetime import datetime
#mod_time = os.stat('file').st_mtime
#print(datetime.fromtimestamp(mod_time))

###see entire directory tree and file that inside
#for dirpath, dirnames, filenames in os.walk('/home/sazzad/'):
#	print('Current Path:', dirpath)
#	print('Directories:', dirnames)
#	print('Files:', filenames)
#	print()


####get environment 
#print(os.environ.get('HOME'))

#file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
#print(file_path)

#print(os.path.basename('/tmp/test.txt'))   #will show just only thi file name
#print(os.path.dirname('/tmp/text.txt'))    #will show just directory name
#print(os.path.split('/tmp/test.txt'))      #will show both directory and file
#print(os.path.exists('/tmp/test.txt'))     #will show if a path exist
#print(os.path.isdir('/tmp/test.txt'))      #will show if it is a directory or not
#print(os.path.isfile('/tmp/test.txt'))     #will show if it is a file or not
#print(os.path.splitext('/tmp/test.txt'))   #will split the file root and the extension

#print(dir(os.path))      #will show everything that is available in os.path
#print(dir(os))
















