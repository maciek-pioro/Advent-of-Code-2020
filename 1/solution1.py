f = open('input.txt', 'r')

t = 2021 * [False]
for l in f:
    n = int(l)
    if t[2020-n]:
        print((2020-n)*n)
        exit()
    t[n] = True