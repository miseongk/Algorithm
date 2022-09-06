# [참고...]
import sys
input = sys.stdin.readline

init, fin = map(int, input().split())

if init >= fin:
    print(init - fin)
    print(1)
else:
    time = 0
    visited = [0] * 100001
    starts = [fin]
    while True:
        # visited를 맨 위에서 더해주는 이유는 init에 도달하는 방법의 수를 구해야 하기 때문.
        # 밑에 for문에서는 아직 visited된 상태가 아니여서 new_starts 배열에 init이 여러번 들어갈 수 있고
        # 그게 visited에 +1 하는 이유이다.
        for start in starts:
            visited[start] += 1
        if visited[init]:
            break
        new_starts = []
        time += 1
        for start in starts:
            if start % 2 == 0 and not visited[start // 2]:
                new_starts.append(start // 2)
            if start > 0 and not visited[start - 1]:
                new_starts.append(start - 1)
            if start < 100000 and not visited[start + 1]:
                new_starts.append(start + 1)
        starts = new_starts
    print(time)
    print(visited[init])