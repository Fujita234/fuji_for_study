import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    for i, v in enumerate(lines):
        list_str = v.split()
        print(list_str)
        for s in list_str:
            find_s = s.find(':')
            if find_s:
                print(s[:find_s])
                print(s[find_s+1:])
            

def fizzbuzz(num):
    return ('FizzBuzz' if num % 5 == 0 else 'Fizz') if num % 3 == 0 else ('Buzz' if num % 5 == 0 else num)

            

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
