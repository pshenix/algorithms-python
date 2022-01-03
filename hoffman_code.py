s = input()
dictionary = {}
result = {}
count = 0
for elem in s:
    count = count + 1 if elem not in dictionary else count
    dictionary.setdefault(elem, 0)
    result.setdefault(elem, '')
    dictionary[elem] += 1

tree = [elem for elem in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)]
last = tree[0]
n = count
weight = 0
while count != 1:
    for elem in tree[-1][0]:
        result[elem] = '0' + result[elem]
        weight += dictionary[elem]
    for elem in tree[-2][0]:
        result[elem] = '1' + result[elem]
        weight += dictionary[elem]
    new = (tree[-1][0] + tree[-2][0], tree[-1][1] + tree[-2][1])
    count -= 1
    tree.pop()
    tree.pop()
    tree.append(new)
    tree.sort(key=lambda x: x[1], reverse=True)

if n == 1:
    weight = len(s)
    result[s[0]] = '0'

print(n, weight)
[print('{}: {}'.format(k, result[k])) for k in result]
[print(result[elem], end='') for elem in s]
