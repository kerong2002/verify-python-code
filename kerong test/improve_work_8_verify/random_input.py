from random import randint
test=open('random_input.txt','w')
range_1=int(input('請輸入測資數量:'))
first_samll=int(input('請輸入輸入的第一項數值的最小範圍值:'))
first_big=int(input('請輸入輸入的第一項數值的最大範圍值:'))
second_samll=int(input('請輸入輸入的第二項數值的最小範圍值:'))
second_big=int(input('請輸入輸入的第二項數值的最大範圍值:'))
for i in range(range_1):
    print(randint(first_samll,first_big),randint(second_samll,second_big),file=test)
test.close()
