import time
import math
import os

def ExecTime(Func):
    def InnerFunc(*args, **kwrds):
        start_time = time.time()
        Func(*args, **kwrds)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
    return InnerFunc

def FuncName(Func):
    def InnerFunc(*args, **kwrds):
        Func(*args, **kwrds)
        FilePath = os.environ['USERPROFILE'] + '\Documents\FuncName.txt'
        with open(FilePath, 'w') as file:
            file.write(f'Function Name : {Func.__name__}')
    return InnerFunc

@ExecTime
@FuncName
def PrintFunc():
    math.factorial(100000)
    return
    
PrintFunc()
