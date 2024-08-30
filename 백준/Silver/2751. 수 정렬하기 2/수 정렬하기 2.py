import sys
input = sys.stdin.read
data = input().split()
numbers = sorted(map(int, data[1:]))

sys.stdout.write('\n'.join(map(str, numbers)) + '\n')