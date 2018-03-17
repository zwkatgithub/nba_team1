import random
task =[1,2,3,4]
list = []
for i in range(10):
    tmp = task.copy()
    random.shuffle(tmp)
    print(tmp)
    list.append(tmp)
print(list)