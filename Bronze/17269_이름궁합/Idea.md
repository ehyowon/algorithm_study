나는 if문 써서 작성했는데 
```py
if alp == 'E':
		num = 4
	elif alp == 'A' or alp == 'F' or alp == 'H' or alp == 'K' or alp == 'M':
		num = 3
	elif alp == 'B' or alp == 'D' or alp == 'N' or alp == 'P' or alp == 'Q' or alp == 'R' or alp == 'T' or alp == 'X' or alp == 'Y':
		num = 2
	else:
		num = 1
```
민채랑 수빈이는 dictionary 써서 작성함
```py
dic = {'A': 3, 
       'B':2,
       'C':1,
       'D':2,
       'E':4,
       'F':3,
       'G':1,
       'H':3,
       'I':1,
       'J':1,
       'K':3,
       'L':1,
       'M':3,
       'N':2,
       'O':1,
       'P':2,
       'Q':2,
       'R':2,
       'S':1,
       'T':2,
       'U':1,
       'V':1,
       'W':1,
       'X':2,
       'Y':2,
       'Z':1}
```
원하는 값을 찾을 때 나처럼 if문을 사용하면 한 문자를 찾을 때마다 시간복잡도가 `O(n)`만큼 걸리지만

딕셔너리를 사용하여 값을 찾을 때는 `O(1)` 시간이 걸린다고 한다.

-> 딕셔너리를 쓰는 것이 훨씬 효율적!
