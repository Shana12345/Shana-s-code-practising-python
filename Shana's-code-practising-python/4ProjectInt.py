#odd number between 1 and input
def odds():
    u = []
    usr = int(input('Enter a num: '))
    for w in range(2, usr):
        if w % 2 ==0:
            pass
        else:
            u.append(w)
    return u
print(odds())

#print all odd number between 1 with user's input
def odd():
    u=[]
    user_input = int(input("Please enter num: "))
    for d in range(1, user_input + 1):
        if d % 2 ==0:
            pass
        else:
            u.append(d)
    return u
print(odd())


#boolean make word in input1 with the letters in input2
def checkwords(input1, input2):
    i = ''
    for k in range(len(input1)):
        if input1[k] in input2:
            i += input1[k]

    while i == input1:
        return True
    return False
            
print(checkwords('cat', 'jdcsjsakjk'))


# prime numbers
def is_prime(n):
    h = []
    for q in range(2, n + 1):
        if q % 2==0 and q != 2:
            pass   
        else:
            h.append(q)
    return h
print(is_prime(13))  

# fizzbuzz
def fb(n):
    options = {
        3 : 'Fizz',
        5 : 'Buzz',
        35 : 'FizzBuzz',
        '-' : 'Sorry, you are not part of the fizzbuzz family'
    }

    if n % 3 == 0 and n % 5 == 0:
        return options[35]

    elif n % 3 == 0:
        return options[3]

    elif n % 5 == 0:
        return options[5]

    else:
        return options['-']
print(fb(11))

# count average 
def Mean(lista):
    num_sum = 0
    for d in lista:
        num_sum = num_sum + d

    avg = num_sum / len(lista)
    return round(avg, 2)
    
print('The mean average is', Mean([2,4,54,63,1,3]))

# reversing input
def rev(input):
    p = str(input)
    return p[::-1] #string slicing 
      
print(rev(321))

# playing with string slicing
def notrev(input):
    p = str(input)
    return p[::3]  # -1 represents 543(reverse), -2 removes the middle value but still in reverse order, -3 removes the first 2 values in reverse order
print(notrev(345))    # positives works in the same way as negative, except the order isnt reversed

#Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
#Examples:

#solution('abc') # should return ['ab', 'c_']
#solution('abcdef') # should return ['ab', 'cd', 'ef']
def solution(s): 
    if len(s) % 2 != 0: s = s + "_"
    cadena = []
    for (x, y) in zip(s[0::2], s[1::2]):
       cadena.append(x + y)
    return cadena
print(rev(321))

#playing around with string slicing
#solution('abc') # should return ['ab', 'c_']
#solution('abcdef') # should return ['ab', 'cd', 'ef']
def solution(s): 
    if len(s) % 2 != 0: s = s + "_"
    cadena = []
    for (x, y) in zip(s[0::2], s[1::2]): #changing the first 0 to 1, it replaces the first character, and replaces it with the second one
       cadena.append(x + y)              #changing the second 1 to 0, switches the positions around of the 2 characters
    return cadena

print(solution('holatodos'))

# Answer to Human Readable Time (research data-time)
def make_readable(sec):
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    return f'{h:02d}:{m:02d}:{s:02d}'
print(make_readable(55000))
        





