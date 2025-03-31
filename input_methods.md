Input methods for competitive programming in python!

### taking integer as input

```
n = int(input())
print (type (n))
```

### taking string as input

```
n = input()
print (type(n))
```

### taking multiple inputs

```
'''
a b c
1 2 3
'''

a, b, c = map(int, input().split())
print(a, b, c)
```

### taking infinite inputs

```
'''
a b c d e f ...
1 2 3 4 5 6 ...
'''

all = [int(i) for i in input().split()]
print(all)
```

### taking finite/infinite inputs for single test but multiple inputs

```
'''
2  ---> no. of elements in single test case
1 2
'''

n = int(input()) # no. of elements
all = [int(i) for i in input().split()] # multiple elements in each line
print(all)
```

### taking finite/infinite for multiple tests and multiple inputs

```
'''
2  ---> no. of test cases
1
3
'''

t = int(input()) # no. of test cases
for _ in range(n):
    x = int(input()) # single element in each line
    print(x)
```

### taking inputs for multi tests, multi no. of elements, multi inputs

```
'''
2
3
1 2 3
4
5 6 7 8
'''

t = int(input()) # no. of test cases
for _ in range(n):
    n = int(input()) # no. of elements in each line
    all = [int(i) for i input().split()]
    print(all)
```

### taking inputs for multi tests, multi elements

```
'''
4
1 2 3 4
2 3 4 5
3 4 4 5
5 4 3 2
'''

t = int(input()) # no. of test cases
for _ in range(t):
    all = [int(i) for i in input().split()]
    print(all)
```

### special case

```
'''
4
4 3
5 3 1 2
3 2
1 3 4
4 2
2 1 2 4
5 6
1 2 3 4 5
'''

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    all = list(map(int, input().split()))
    print(all)
```