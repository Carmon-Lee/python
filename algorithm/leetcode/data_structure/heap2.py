import random

class Heap:
    def __init__(self, data) -> None:
        self.arr = [0]
        self.arr.extend(data)
        print(self.arr[1:])

    def __len__(self):
        return len(self.arr) - 1

    def max_heapify(self, data, index):
        l = index * 2
        r = index * 2 + 1
        if l <= self.__len__() and self.arr[l] > self.arr[index]:
            largest = l
        else:
            largest = index
        if r <= self.__len__() and self.arr[r] > self.arr[largest]:
            largest = r

        if largest != index:
            self.arr[largest], self.arr[index] = self.arr[index], self.arr[largest]
            self.max_heapify(self.arr, largest)
        print('largest:', largest)

    def heapify(self):
        for i in range((self.__len__() + 1) // 2, 0, -1):
            self.max_heapify(self.arr, i)
        print(self.arr)


if __name__ == '__main__':

    a = Heap([random.randint(1,100) for i in range(10)])
    print(len(a))
    a.heapify()
