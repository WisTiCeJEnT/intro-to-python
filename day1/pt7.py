def grade_cal(n):
    if n < 0 or n > 100:
        print('Invalid score')
    else:
        if n >= 80:
            print('A')
        elif n >= 75:
            print('B+')
        elif n >= 70:
            print('B')
        elif n >= 65:
            print('C+')
        elif n >= 60:
            print('C')
        elif n >= 55:
            print('D+')
        elif n >= 50:
            print('D')
        else:
            print('F')

i = 0
n = int(input())
while i < n:
    grade_cal(int(input()))
    i += 1
