def merge_and_count(a: list, b: list) -> (list, int):
    left = len(a)
    right = len(b)
    il = ir = count = 0
    result = []
    while il < left and ir < right:
        if a[il] > b[ir]:
            count += left - il
            result.append(b[ir])
            ir += 1
        else:
            result.append(a[il])
            il += 1
    result = result + a[il:left] + b[ir:right]
    return result, count


n = int(input())
A = [[int(i)] for i in input().split()]
counter = 0
while n > 1:
    if n % 2 == 1:
        answer = merge_and_count(A[n - 2], A[n - 1])
        A[n - 2] = answer[0]
        counter += answer[1]
        n -= 1
    for i in range(0, n, 2):
        answer = merge_and_count(A[i], A[i + 1])
        A[i // 2] = answer[0]
        counter += answer[1]
    n = n // 2
print(counter)

