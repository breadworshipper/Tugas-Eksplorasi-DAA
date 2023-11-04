import time
import tracemalloc

class MaxHeapSort:
    def __init__(self, filepath):
        self._dataset = []
        self.filepath = filepath

        self._init_dataset()

    def _init_dataset(self):
        with open(self.filepath, 'r') as f:
            for line in f:
                self._dataset.append(int(line))

    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            (arr[i], arr[largest]) = (arr[largest], arr[i])

            self.heapify(arr, n, largest)


    def heapSort(self, arr):
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            (arr[i], arr[0]) = (arr[0], arr[i])
            self.heapify(arr, i, 0)

        return arr

if __name__ == '__main__':
    filepaths = ['dataset/small/small_random.txt', 'dataset/small/small_sorted.txt', 'dataset/small/small_reverse_sorted.txt',
                 'dataset/medium/medium_random.txt', 'dataset/medium/medium_sorted.txt', 'dataset/medium/medium_reverse_sorted.txt',
                 'dataset/large/large_random.txt', 'dataset/large/large_sorted.txt', 'dataset/large/large_reverse_sorted.txt']

    print("MAX HEAP SORT")
    for filepath in filepaths:
        tracemalloc.start()
        start_time = time.time()
        max_heap_sort = MaxHeapSort(filepath)
        max_heap_sort.heapSort(max_heap_sort._dataset)
        end_time = time.time()
        snapshot = tracemalloc.take_snapshot()
        tracemalloc.stop()
        runtime = (end_time - start_time) * 1000
        print('------' * 20)
        print(f'Runtime of {filepath.split("/")[-1]}: '.ljust(45), str(round(runtime)).ljust(5), " ms")

        top_stats = snapshot.statistics('lineno')
        total = sum(stat.size for stat in top_stats)
        print(f"Total allocated size: {total / 1024} KiB")



