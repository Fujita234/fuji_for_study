def main(num):
  for i in range(num):
    print(FizzBuzz(i+1))

def FizzBuzz(num):
  return ('FizzBuzz' if num % 5 == 0 else 'Fizz') if num % 3 == 0 else ('Buzz' if num % 5 == 0 else num)

main(15)