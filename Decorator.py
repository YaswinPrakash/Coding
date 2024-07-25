import time, math, os

def ExecTime(Func):
    def InnerFunc(*args, **kwrds):
        StartTime = time.time()
        A = Func(*args, **kwrds)
        EndTime = time.time()
        print(f"Execution time: {EndTime - StartTime} seconds")
        return A
    return InnerFunc

def FuncName(Func):
    def InnerFunc(*args, **kwrds):
        B = Func(*args, **kwrds)
        with open(os.environ['USERPROFILE'] + '\Documents\FuncName.txt', 'w') as file:
            file.write(f'Function Name : {Func.__name__}')
        return B
    return InnerFunc

@ExecTime
@FuncName
def Factorial(N):
    return math.factorial(N)
    
Factorial(100000)
