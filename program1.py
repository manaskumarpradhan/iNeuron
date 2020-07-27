def div7mult5(lowernum=2000,uppernum=3201):
    for i in range(lowernum,uppernum):
        #check if i is multiplicative of 5
        n = i
        while (n>0):
            n=n-5
        #check if i is divisiable by 7 and not multiplicative of 5
        if (i%7==0) & (n!=0):
            print(i,end=',')

if __name__ == "__main__":
    div7mult5()