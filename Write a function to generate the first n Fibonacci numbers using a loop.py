#Write a function to generate the first n Fibonacci numbers using a loop. For example, if n = 5, the output should be [0, 1, 1, 2, 2].
def fab(n):
    if n <= 1:
        return n
    return fab(n-2)+fab(n-1)
def get_fab(n,a):
    for i in range(n):
        a.append(fab(i))
    return a
a  = []
n = int(input())
print(get_fab(n,a))
