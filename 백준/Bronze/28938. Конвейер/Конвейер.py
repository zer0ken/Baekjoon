input()
s = sum(map(int, input().split()))
if s == 0:
    print('Stay')
elif s < 0:
    print('Left')
else:
    print('Right')