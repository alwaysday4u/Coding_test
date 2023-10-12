'''
https://www.acmicpc.net/problem/1676
'''

import sys

n = int(sys.stdin.readline().rstrip())
print(n//5+n//25+n//125)
