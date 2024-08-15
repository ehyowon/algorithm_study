def Z(N, r, c):
    cnt = 0

    while N > 0:
        half = 2**(N-1)

        if r < half and c < half: #0
            cnt += 0
        elif r < half and c >= half: #1
            cnt += half * half
            c -= half
        elif r >= half and c < half: #2
            cnt += half * half * 2
            r -= half
        else: #3
            cnt += half * half * 3
            r -= half
            c -= half
        
        N -= 1

    return cnt

N, r, c = map(int, input().split())
print(Z(N, r, c))
