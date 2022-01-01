from random import randint
test=open('random_input.txt','w')
for i in range(100):
    print(randint(1,2147483647),randint(2,10),file=test)
test.close()
