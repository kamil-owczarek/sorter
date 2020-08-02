import datetime
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

quickSortElements = int(config['quicksort']['elements'])
quickSortStep = int(config['quicksort']['step'])
quickSortIteration = int(config['quicksort']['iter'])

bubbleSortElements = int(config['bubblesort']['elements'])
bubbleSortStep = int(config['bubblesort']['step'])
bubbleSortIteration = int(config['bubblesort']['iter'])

times = []


def open_input_file(input_file):
    f = open(input_file, "r")
    data = eval(f.readline())
    f.close()
    return data


def bubble_sort_algorithm(element_list, n):
    for i in range(n):
        for j in range(n - i - 1):
            if element_list[j] > element_list[j + 1]:
                element_list[j], element_list[j + 1] = element_list[j + 1], element_list[j]


def quick_sort_algorithm(element_list, l=0, r=None):
    if r is None:
        r = len(element_list) - 1
    i, j = l, r
    if (l + r) % 2 == 0:
        mid = (l + r) / 2
    else:
        mid = (l + r + 1) / 2
    pivot = element_list[int(mid)]
    while i <= j:
        while element_list[i] < pivot: i += 1
        while element_list[j] > pivot: j -= 1
        if i <= j:
            element_list[i], element_list[j] = element_list[j], element_list[i]
            i += 1
            j -= 1
    if l < j: quick_sort_algorithm(element_list, l, j)
    if r > i: quick_sort_algorithm(element_list, i, r)


def main():
    data = open_input_file("input.txt")
    ans = True
    while ans:
        print("""
              Choose option:
          1. Bubble Sort
          2. Quick Sort
          w. Exit
          """)
        ans = input()

        if ans == "1":
            print("Sorting")
            start = datetime.datetime.now()
            for i in range(0, bubbleSortElements + bubbleSortStep, bubbleSortStep):
                for x in range(bubbleSortElements):
                    bubble_sort_algorithm(data, i)
            end = (datetime.datetime.now() - start)
            print(data)
            print("Sorted in " + str(end.seconds) + " seconds.")
            times.clear()

        elif ans == "2":
            print("Sorting")
            start = datetime.datetime.now()
            for j in range(0, quickSortElements + quickSortStep, quickSortStep):
                for i in range(quickSortIteration):
                    quick_sort_algorithm(data, 0, j - 1)
            end = (datetime.datetime.now() - start)
            print(data)
            print("Sorted in " + str(end.seconds) + " seconds.")
            times.clear()

        elif ans == "w":
            print("Bye Bye")
            break

        elif ans != "":
            print("Unknown option")


if __name__ == '__main__':
    main()
