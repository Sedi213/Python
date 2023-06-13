import math


def task2(kids, apples):
    foreach = apples // kids
    left = apples - kids * foreach
    print("Left: " + str(left) + " For Each: " + str(foreach))


def task3(hws, hh, mm):
    time = hh * 60 + mm + hws
    H = int(time / 60)
    M = time - H * 60
    print("Hours: " + str(H) + " Minutes: " + str(M))


def task4(k1, k2, k3):
    all = k1 + k2 + k3
    part = all / 2
    if part % 2 != 0:
        part = int(part) + 1
    else:
        part = int(part)
    print("Part: " + str(part))


def task5():
    first = int(input("Input first word: "))
    second = int(input("Input second word: "))
    third = int(input("Input third word: "))

    max = (first + second + abs(first - second)) / 2
    max = (max + third + abs(max- third)) / 2

    min = (first + second - abs(first - second)) / 2
    min = (min + third - abs(min - third)) / 2

    mid = (first + second + third) - max - min

    print(str(int(max)) + "\t" + str(int(min)) + "\t" + str(int(mid)))


def task6(a, b, l, N):
    result = (N * a) + 2 * (b * (N - int(N / 4) - 1)) + l
    print("Result: " + str(result) + "sm")