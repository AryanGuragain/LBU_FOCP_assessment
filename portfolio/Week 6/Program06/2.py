def factors(num):
    factors_list=[]
    for i in range(1,num+1):
        if num % i == 0:
            factors_list.append(i)

    return factors_list

f=factors(16)
print("The factors of number 16 are",f)