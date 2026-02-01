num=int(input("Enter your number:"))
ognum=num
rev_num=0
while num>0:
    digit=num%10
    rev_num=rev_num*10 +digit
    num//=10
if ognum==rev_num:
    print("This is a palindrome number")
else:
    print("This is not a palindrome number")