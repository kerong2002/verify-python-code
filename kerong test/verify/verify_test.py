x=0
with open('right_output.txt','r') as answer:
    with open('test_output.txt','r') as test:
        for answer,test in zip(answer.readlines(),test.readlines()):
##            print(answer)
##            print(test)
            answer=answer.strip("\n")#將換行符號刪除再存回
            test=test.strip("\n")#將換行符號刪除再存回
            if (answer!=test):#verify the test output
                print(test,', This output not correct.')
                x=1
            else:
                print('pass')
        if(x==1):
            print('The output have some problem.')
        else:
            print('All output is correct')
