def FizzBuzz(n):
    if n%3==0 and n%5==0:
        return "FizzBuzz"
    elif n%3==0 and n%5!=0:
        return "Fizz"
    elif n%3!=0 and n%5==0:
        return "Buzz"
    else:
        return str(n)
    
n1 = input()
n2 = input()
n3 = input()

answer = ""
if n1.isdigit():
    answer = FizzBuzz(int(n1)+3)
elif n2.isdigit():
    answer = FizzBuzz(int(n2)+2)
elif n3.isdigit():
    answer = FizzBuzz(int(n3)+1)
print(answer)