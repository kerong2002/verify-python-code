f=open('random_input.txt','r')
for line in f:
    i,j = map(int,line.split())
    max_length=0
    for run in range(min(i,j),max(i,j)+1):
        cout_time=0
        savechange = run
        while(savechange!=1):
            if(savechange%2==0):
                savechange/=2
                cout_time+=1
            else:
                savechange=3*savechange+1
                cout_time+=1
        if(cout_time>max_length):
            max_length=cout_time
    print("{} {} {}".format(i,j,max_length+1),file = open("test_output.txt", "a"))
f.close()