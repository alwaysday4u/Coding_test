'''
https://www.acmicpc.net/problem/13241
'''

import math

x,y = map(int,input().split())
print(x*y//math.gcd(x,y))
