def is_7_valid(x):
    return not (x%7==0 or '7' in str(x))
    # ถ้ามี 7 หรือหาร 7 ลงตัว ตอบ False
    # ถ้าไม่ใช่ตอบ True

n = int(input())
while(is_7_valid(n)):
    n = int(input())

print('You lose')
