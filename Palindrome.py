original = str(input("Enter Text to see if it is Palindrome "))
def isPalindrome(s):
    end = len(s) -1
    start = 0
    while start < end:
        if(s[start] != s[end]):
            return False
        start +=1
        end -=1
        return True 


ans = isPalindrome(original)

if ans:
    print("Yes")
else:
    print("No")
