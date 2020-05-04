# numberLines.py                                  
import fileinput                                  
                                                   
def doNumLi(fileName):
    fileList = fileinput.input(fileName,inplace=True)
    for line in fileList:        
        line = line.rstrip()                           
        num = fileinput.lineno()                       
        print('{:<50} # {:2d}'.format(line, num))  

doNumLi('hello.py')