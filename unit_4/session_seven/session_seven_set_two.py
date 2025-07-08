'''Problem Set 2'''


# Problem 1
def is_perfect_number(n):
    accum = 0
    if n == 1:
        return False
    for i in range (1,n):
        if n % i == 0:
            accum += i
    if n == accum:
        return True
    return False

print(is_perfect_number(17))
print(is_perfect_number(28))


# Problem 2
def is_palindrome(s):

    beginning = 0
    end = len(s) - 1
    
    while beginning < end:
        if s[beginning] == s[end]:
            beginning += 1
            end -= 1
        else:
            return False
    return True

s = "amanaplanacanalpanama"
s2 = "helloworld"

print(is_palindrome(s))
print(is_palindrome(s2))


# Problem 3
def is_palindrome(s):
    reverse = s[::-1]
    return reverse ==s


#Problem 4
def make_palindrome(s):
    beginning = 0
    end = len(s) - 1
    
    while beginning < end:
        if s[beginning] == s[end]:
            beginning += 1
            end -= 1
        else: 
            if s[beginning] < s[end]:
                s = s.replace(s[end], s[beginning], end)
            else:
                s = s.replace(s[beginning], s[end], beginning)
            beginning += 1
            end -= 1
    return s

s = "egcfe"
print(make_palindrome(s)) 

another_string = "banana"
# Replaces only the first 'a' with 'e'
modified_string = another_string.replace("a", "e", 1)


s = "abcd"
print(make_palindrome(s))

s = "seven"
print(make_palindrome(s))



