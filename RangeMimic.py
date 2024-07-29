def RangeMimic(Start, Stop = None, Step = 1):
    if Stop is None:
        Stop = Start
        Start = 0
    if Step == 0:
        raise ValueError("Step cannot be zero.")
    Current = Start
    if Step > 0:
        while Current < Stop:
            yield Current
            Current += Step
    else:
        while Current > Stop:
            yield Current
            Current += Step

# In-built python function
for i in range(10, 2, -2):
    print(i)

# Range mimic function
for i in RangeMimic(10, 2, -2):
    print(i)
