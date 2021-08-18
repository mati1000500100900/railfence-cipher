import math  
import time

lorem = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'''

def encode(input, size):
    result=""
    for j in range(size):
        for i in range(len(input)):
            if round((math.acos(math.cos(i*math.pi/(size-1)))/math.pi)*(size-1)) == j:
                result+=input[i]
    return result


def encode2(input, size):
    result=""
    for j in range(size):
        for i in range(len(input)):
            if (-abs((i%((size-1)*2))-size+1)+size-1) == j:
                result+=input[i]
    return result

def getMillis():
    return int(round(time.time() * 1000))

start = getMillis()
for i in range(2,100):
    encode(lorem,i)
print(getMillis()-start)

start = getMillis()
for i in range(2,100):
    encode2(lorem,i)
print(getMillis()-start)    
