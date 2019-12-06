import sys
#sys.stdout.write('*')
#3줄의 경우
#2 " "  1 "*"
#1 3
#0 5
# 1 3 5
# range(1 ,2) range(1,4)

[1,2,3]
a = int(input())
b = a
for i in range(1, a+1):
    for j in range(b,1,-1):
        sys.stdout.write(' ')
    b-=1
    for j in range(1, 2*i):
        sys.stdout.write('*')
    print()
