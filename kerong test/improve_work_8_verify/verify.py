x=0
print(end='',file = open("verify_result.txt", "w"))
with open('right_output.txt','r') as answer:
    with open('test_output.txt','r') as test:
        for answer,test in zip(answer.readlines(),test.readlines()):
            answer=answer.strip("\n")#將換行符號刪除再存回
            test=test.strip("\n")#將換行符號刪除再存回
            if (answer!=test):#verify the test output
                print(test,', This output not correct. Correct output is: ',answer,file = open("verify_result.txt", "a"))
                x=1
            else:
                print('pass',file = open("verify_result.txt", "a"))
        if(x==1):
            print('The output have some problem.',file = open("verify_result.txt", "a"))
        else:
            print('All output is correct',file = open("verify_result.txt", "a"))
