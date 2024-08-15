# Z

https://www.acmicpc.net/problem/1074

## 문제
한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.

<img width="101" alt="image" src="https://github.com/user-attachments/assets/a19f8603-caa2-4bb5-ac95-bdf9c9640bdb">

N > 1인 경우, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.

다음 예는 22 × 22 크기의 배열을 방문한 순서이다.

<img width="247" alt="image" src="https://github.com/user-attachments/assets/1c96f7ea-c682-424b-9d20-a0108deca72a">

N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

다음은 N=3일 때의 예이다.

<img width="527" alt="image" src="https://github.com/user-attachments/assets/18501807-741e-4095-bc05-9856e5bcd7ea">

## 입력
첫째 줄에 정수 N, r, c가 주어진다.
- 1 ≤ N ≤ 15
- 0 ≤ r, c < 2N

## 출력
r행 c열을 몇 번째로 방문했는지 출력한다.

---
### 예제입력1
> 2 3 1

### 예제출력1
> 11

### 예제입력2
> 3 7 7

### 예제출력2
> 63

### 예제입력3
>1 0 0

### 예제출력3
>0

### 예제입력4
> 4 7 7

### 예제출력4
> 63

### 예제입력5
> 10 511 511

### 예제출력5
>262143

### 예제입력6
> 10 512 512

### 예제출력6
>786432
