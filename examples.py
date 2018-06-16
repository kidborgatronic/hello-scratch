#find out which one of the given numbers differs from the others
# modulo, multi index 
def iq_test(numbers):
    evens = []
    odds = []
    list = numbers.split()
    for i in xrange(len(list)):
        #print i, list[i]
        if int(list[i]) % 2 == 0:
            evens.append([list[i], i])
        else:
            odds.append([list[i], i])
    if len(evens) == 1:
        id = evens[0][1] + 1
    else:
        id = odds[0][1] + 1       
    return id

#solutions
def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1
    
#tax tax tax - find number of years until principle interest reaches desired goal
# while
def calculate_years(principal, interest, tax, desired):
    p = principal
    i = interest
    t = tax
    d = desired
    y = 0
    while (p < d):
        p = (p * i) - ((p * i) * t) + p
        y = y + 1
    return y
    #raise NotImplementedError("TODO: calculate_years")\
    
#solution
def calculate_years(principal, interest, tax, desired):
    years = 0
    
    while principal < desired:
        principal += (interest * principal) * (1 - tax)
        years += 1
        
    return years

#shortest word - given a string of words, return the length of the shortest word(s)
# filter min
def find_short(s):
    a = s.split()
    word = min(filter(None, a), key=len)
    l = len(word)
    return l # l: shortest word length
    
# solution
def find_short(s):
    return min(len(x) for x in s.split())
