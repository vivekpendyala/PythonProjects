for i in range(1042000,702648266):
    _sum=i
    cubic_sum=0
    c=i
    d=0
    while c>0:
        c=c//10
        d+=1
    while i>0:
        last=i%10
        cubic_sum+=last**d
        i=i//10
    if _sum==cubic_sum:
        print('The first armstrong number is-',_sum)
        break
    elif _sum==702648265:
        print('There is armstrong number possible in the given range...!!')
        break
       
    
