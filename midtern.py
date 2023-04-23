# -*- coding:utf-8 -*
import random
import time
import matplotlib.pyplot as plt

def create_arr(n):
    """arr = []
    for i in range(n):
        arr.append(i+1)
    return arr"""
    start = 1
    end = n*10
    arr = random.sample(range(start, end + 1), n)
    return sorted(arr)#fibonacci和二元搜尋都需要排序好，但這樣就會導致需要額外的排序時間，我擔心會造成結果與事實不符所以讓他們先排序好

def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
def binary_search(arr,x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def fibonacci_search(arr,x):
    n = len(arr)
    fib2 = 0
    fib1 = 1
    fib = fib2 + fib1

    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1
    offset = -1

    while fib > 1:
        i = min(offset + fib2, n - 1)

        if arr[i] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > x:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i
    return -1
def test_run():
    arr_length = 10
    list_a = []
    list_b = []
    list_c = []
    for j in range(100):
        arr = create_arr(arr_length)
        times = []
        for i in range(5):
            start_time = time.perf_counter()
            fibonacci_search(arr, random.randint(0,arr_length*10))
            end_time = time.perf_counter()
            times.append(end_time- start_time)
        list_b.append(sum(times)/5)
        times = []
        for i in range(5):
            start_time = time.perf_counter()
            binary_search(arr, random.randint(0,arr_length*10))
            end_time = time.perf_counter()
            times.append(end_time- start_time)
        list_c.append(sum(times)/5)
        times = []
        for i in range(5):
            start_time = time.perf_counter()
            linear_search(arr, random.randint(0,arr_length*10))
            end_time = time.perf_counter()
            times.append(end_time- start_time)
        list_a.append(sum(times)/5)
        arr_length += 10
    print("linear:",list_a)
    print("fibonacci:",list_b)
    print("binary:",list_c)
    plot(list_a, list_b, list_c)
def plot(linear,fibonacci,binary):
    y=[]
    for i in range(100):
        y.append((i+1)*10)
    plt.plot(y,linear, 'o-', label='linear')  # 绘制第一条折线，设置标签为X1轴
    plt.plot(y,fibonacci, 'x-', label='fibonacci')  # 绘制第二条折线，设置标签为X2轴
    plt.plot(y,binary, 's-', label='binary')  # 绘制第三条折线，设置标签为X3轴
    plt.xlabel('frequency')  # 设置X轴标签
    plt.ylabel('time')  # 设置Y轴标签
    plt.title('')  # 设置图表标题
    plt.legend()  # 显示图例
    plt.show()  # 显示图表

test_run()
