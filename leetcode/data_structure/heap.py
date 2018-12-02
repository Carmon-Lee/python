import random

class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.pos = 0

    def __repr__(self) -> str:
        return str(self.arr)

    def tranverse(self):
        pass


if __name__ == '__main__':
    arr = [1]


    def heappush(arr, number):
        arr.append(number)
        siftup(arr, len(arr) - 1)


    def siftup(arr, pos):
        while pos > 0:
            up_pos = (pos - 1) // 2
            if arr[pos] < arr[up_pos]:
                arr[pos], arr[up_pos] = arr[up_pos], arr[pos]
                pos=up_pos
            else:
                break

    for i in range(10):
        heappush(arr,random.randint(0,20))
        print(arr)

