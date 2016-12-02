



def getprim(n):
    i = 3

    while(i < n):
        is_prime = True
        j = 2
        for j in range(2, i-1):
            if(i % j == 0):
                is_prime = False
                break

        if(is_prime == True):
            print(i)
            i += 2
        else:
            i += 1



getprim(20)