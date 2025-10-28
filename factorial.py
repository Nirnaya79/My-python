def fac(num):
    result=1;
    for index in range(1,num+1):
        result=result*index;
    return result

print(fac(5))