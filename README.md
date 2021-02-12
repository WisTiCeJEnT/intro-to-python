# Intro to Python Programing
#### @IT-ARU
> By: Wattanai Sathuphan


### Topic
- [ ] Print() / Input()
- [ ] Basic Data types (int, float, string, ...)
- [ ] Condition (if, else)
- [ ] While loop
- [ ] For loop
- [ ] Function (def)
- [ ] Scope
- [ ] List
- [ ] Dictionary
- [ ] Module
- [ ] Application (TBA)

### Practice
#### 1. Hello to you
> รับข้อมูลชื่อผู้ใช้ และทักทายผู้ใช้กลับด้วยชื่อนั้น

Input:
```
Nine
```
Output:
```
Hello Nine
```
<br/>
<br/>

#### 2. Introducer
> รับข้อมูลชื่อ, อายุ, ที่อยู่ จากนั้นใช้ข้อมูลนั้นสร้างประโยคในการแนะนำตัวอย่างง่าย
Input:
```
Nine
18
Ayutthaya
```
Output:
```
Hi, My name is Nine. I'm 18 years old. I come from Ayutthaya.
```
<br/>
<br/>

#### 3. Percentage Calculator
> รับข้อมูลเลข a, b และ c จากนั้นคำนวณว่าแต่ละข้อมูลมีค่าเป็นกี่เปอร์เซ็นต์จากข้อมูลทั้งหมด //แสดงทศนิยม 2 ตำแหน่งเสมอ
Input:
```
2
3
5
```
Output:
```
20.00% 30.00% 50.00%
```
<br/>
<br/>

#### 4. What is my type?
> หาว่าข้อมูลต่อไปนี้เป็นชนิดใด
> - 10
> - 10.0
> - "10"
> - "10.0"
> - True

Input:
```
-no input data-
```
Output:
```
-TBA-
```
<br/>
<br/>

#### 5. Grade calculator
> รับข้อมูลคะแนน และแสดงผลเกรดของนิสิตกลับไป โดยใช้ช่วงคะแนนต่อไปนี้ (หากไม่อยู่ในช่วงใดให้แสดงข้อความ 'Invalid score')<br/>
> 80 - 100: A<br/>
> 75 - 79: B+<br/>
> 70 - 74: B<br/>
> 65 - 69: C+<br/>
> 60 - 64: C<br/>
> 55 - 59: D+<br/>
> 50 - 54: D<br/>
> 0 - 49: F

Input1:
```
88
```
Output1:
```
A
```
Input2:
```
64
```
Output2:
```
C
```
Input3:
```
112
```
Output3:
```
Invalid score
```

<br/>
<br/>

#### 6. Grade calculator (AD)
> ประยุกต์โปรแกรมในข้อ 3 ให้ทำงานได้หลายครั้ง โดยระบุจำนวนครั้งใน input ครั้งแรก และคำนวณเกรดไปอีกจำนวนเท่านั้น

Input1:
```
2
88
40
```
Output1:
```
A
F
```
Input2:
```
3
64
77
0
```
Output2:
```
C
B+
F
```
Input3:
```
1
112
```
Output3:
```
Invalid score
```

