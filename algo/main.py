import sys

def main(lines):
    # print('Hello %s !' % lines)

    for i, v in enumerate(lines):
        # print("line[{0}]: {1}".format(i, v))
        print('Hello %s!' % v)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
