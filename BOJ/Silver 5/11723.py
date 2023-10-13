'''
https://www.acmicpc.net/problem/11723
'''

import sys

S=set()
for _ in range(int(input())):
    opt = sys.stdin.readline().rstrip()
    if opt == 'all':
        S = set([i for i in range(1, 21)])
    elif opt == "empty":
        S= set()
    else:
        opt = opt.split()
        opt, num = opt[0], int(opt[1])
        if opt == 'add':
            S.add(num)
        elif opt == 'remove':
            S.discard(num)
        elif opt == 'toggle':
            if num in S:
                S.remove(num)
            else:
                S.add(num)
        else:
            print(int(num in S))
