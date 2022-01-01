from random import randint
test=open('right_output.txt','w')
for i in range(20):
    N=randint(1,2147483647)
    B=randint(2,10)
    N,B = int(N),int(B)
    
    def covert(N ,B):
        convertstring="0123456789"
        if N < B:
            return convertstring[N]
        else:
            return covert(N//B,B) + convertstring[N%B]
        
    if(N>0 and(B>1 and B<=10)):
        result = covert(N,B)
        print(N,B,result,file=test)

    else:
        break
test.close()
