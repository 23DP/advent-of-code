def fact_fraction(n: int) -> list:
    retVal = []
    i = 1

    while n:
        retVal.append(n % i)
        n = n//i    #integer division
        i += 1

    return retVal[::-1]    #reversing the list    

def resize(arr: list, new_length: int) -> list:
    for _ in range( new_length - len(arr) ): 
        arr.insert(0, 0)  #criminal, will replace this with deque
    return arr

def nth_lex_permutation(arr: list, k: int) -> list:
    fact = resize(fact_fraction(k), len(arr))
    retVal = []

    while(len(fact)):
        position = fact.pop(0)  #deque was made for this..
        retVal.append( arr.pop(position) )

    return retVal
