
#3의배수, 5의배수 -> FizzBuzz
#3의배수 -> Fizz
#5의배수 -> Buzz
#모두 아니면 -> i

for i in [3,2,1]:
    temp=input()
    if temp not in ['Fizz','Buzz','FizzBuzz']: #입력받은 값이 숫자일 경우에만
        answer=int(temp)+i #첫번째가 숫자이면 3, 두번째가 숫자이면 2, 세번째가 숫자이면 1을 더함


if answer%5==0 and answer%3==0:
    print('FizzBuzz')
elif answer%3==0:
    print('Fizz')
elif answer%5==0:
    print('Buzz')
else:
    print(answer)