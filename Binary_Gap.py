

def solution(N):

    r=[]
    while N/2 !=0:

        r.append(N%2)
        N=int(N/2)
        
    r = r[::-1]
    #print(r)
    index = []
    
    for i in range(len(r)):
        if r[i] == 1:
            index.append(i)
    #print(index)
    big = 0  
    if len(index) != 1:
        for i in range(len(index)-1, -1, -1):
            if i == 0:
                big = big
            else:
                # print(index[i] - index[i-1])
                if index[i] - index[i-1] > big:
                    big = index[i] - index[i-1]
        return (big - 1)
    else:
        return 0
