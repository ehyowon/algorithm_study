민채가 쓴 코드인데 대각선 한 줄을 line으로 생각해서 규칙 찾아서 품!

```py
num = int(input())
line = 1

while num > line:
        num -= line
        line += 1
i = 1
if line % 2 == 1:
        a = line - num + 1
        b = num
elif line % 2 == 0: 
        a = num
        b = line - num + 1
        
print(f'{a}/{b}')
```
