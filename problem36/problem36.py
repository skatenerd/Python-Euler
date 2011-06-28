def isPalindrome(x):
        s=str(x)
        r=s[::-1]
        return r==s
def isBinPalindrome(x):
        s=str(bin(x))
        s=s[2:]
        r=s[::-1]
        return r==s
s=0
for x in range(1000000):
        if isPalindrome(x) and isBinPalindrome(x):
                print x
                s+=x
print s
