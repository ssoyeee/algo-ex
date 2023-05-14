import itertools #미해결

s = raw_input()
t = raw_input()

def solution(s, t):
    # ans = ''.join(map(''.join, zip(s, t)))
    # return ans
    out1 = ''
    for i, c in enumerate(s):
        out1 += c + t[i]

print(solution)