import sys

def cat(args):
    for filename in args:
        with open(filename) as f:
            for line in f:
                print(line, end='')


def head(args):
    if args[0] == '-n':
        numlines = int(args[1])
        args = args[2:]
    else:
        numlines = 100

    for filename in args:
        n = numlines
        with open(filename) as f:
            for line in f:
                if n > 0:
                    print(line, end='')
                    n -= 1
                else:
                    break


def tail(args):
    if args[0] == '-n':
        numlines = int(args[1])
        args = args[2:]
    else:
        numlines = 10

    for filename in args:
        n = numlines
        buffer = []
        with open(filename) as f:
            for line in f:
                buffer.append(line)
                if n > 0:
                    n -= 1
                else:
                    buffer.pop(0)
            for l in buffer:
                print(l, end='')


def wc(args):
    for filename in args:
        with open(filename) as f:
            bytes, words, lines = 0, 0, 0
            for line in f:
                lines += 1
                bytes += len(line)
                words += len(line.split())
            print(f"\t{lines}\t{words}\t{bytes}\t{filename}")



def grep(pattern, args):
    for filename in args:
        with open(filename) as f:
            for line in f:
                if pattern in line:
                    print(line, end='')


def cut(args):
    delim, fieldSpec = "\t", [1]
    while args[0].startswith('-'):
        if args[0].startswith('-d'):
            delim = args[0][2]
        elif args[0].startswith('-f'):
            fieldSpec = sorted(map(lambda i: int(i), args[0][2:].split(',')))
        args.pop(0)
    for filename in args:
        with open(filename) as f:
            for line in f:
                line = line.rstrip()
                fields = line.split(delim)
                for i in fieldSpec:
                    print(fields[i-1], end=delim)
                print("\b ")




if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} TOOL_NAME FILENAME")
    sys.exit(1)

if sys.argv[1] == 'cat':
    cat(sys.argv[2:])

elif sys.argv[1] == 'head':
    head(sys.argv[2:])

elif sys.argv[1] == 'tail':
    tail(sys.argv[2:])

elif sys.argv[1] == 'wc':
    wc(sys.argv[2:])

elif sys.argv[1] == 'grep':
    grep(sys.argv[2], sys.argv[3:])

elif sys.argv[1] == 'cut':
    cut(sys.argv[2:])

else:
    print(f"{sys.argv[1]} is not a recognized command :(")
    sys.exit(2)
