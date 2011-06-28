import palindrome

maxPalindrome = 0
firstNum, secondNum = 999,999
counter = 0
while firstNum > 1:
    while secondNum > 1:
        counter = counter +1
        if isPalindrome(firstNum * secondNum):
            if firstNum * secondNum > maxPalindrome:
                maxPalindrome = firstNum * secondNum
        secondNum = secondNum - 1
    firstNum = firstNum -1
    secondNum = firstNum

print maxPalindrome
print counter
