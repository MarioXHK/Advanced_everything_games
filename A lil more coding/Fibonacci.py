

def nachi(n: int, two: list[int] = [0,1]) -> int:
    if n <= 1:
        return two[0]
    else:
        no = [two[1]]
        no.append((two[0]+two[1]))
        return nachi(n-1,no)

cases = int(input())

for i in range(cases):
    fiber = int(input())
    plus = nachi(fiber)

    print(plus) 