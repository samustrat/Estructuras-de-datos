#Samuel Alzate Morales

def res(s, tab):
    size = len(tab)
    return s % size
    
def cad(s):
    sum = 0
    for p in s:
        sum += ord(p)
    return sum

def pond(s):
    sum = 0
    for i in range (len(s)):
        sum += (i + 1) * ord(s[i])
    return sum

def h_str(s): 
    return cad(s)%11

def cuad(s, tab):
    tam = len(tab)
    cua = s**2
    cua2 = str(cua)
    lis = []

    for a in cua2:
        lis += [int(a)]

    tam = len(lis)
    num1 = lis[tam//2]
    num2 = lis[(tam//2)-1]

    str1= str(num1)
    str2= str(num2)
    jun = int(str1 + str2)

    return jun % tab
    


    
    
