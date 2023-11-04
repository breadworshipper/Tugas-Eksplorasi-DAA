import random
import time
import tracemalloc

class RandomizedShellSort:
    def __init__(self, filepath):
        self._dataset = []
        self._C = 4
        self.filepath = filepath

        self._init_dataset()

    def _init_dataset(self):
        with open(self.filepath, 'r') as f:
            for line in f:
                self._dataset.append(int(line))
    def exchange(self, a, i, j):
        a[i], a[j] = a[j], a[i]

    def compare_exchange(self, a, i, j):
        if (i < j and a[i] > a[j]) or (i > j and a[i] < a[j]):
            self.exchange(a, i, j)

    def permute_random(self, a):
        for i in range(len(a)):
            self.exchange(a, i, random.randint(i, len(a)-1))

    def compare_regions(self, a, s, t, offset):
        for count in range(4):
            mate = list(range(offset))
            # self.permute_random(mate)
            for i in range(offset):
                self.compare_exchange(a, s + i, t + mate[i])
    def randomized_shell_sort(self):
        a = self._dataset
        n = len(self._dataset)
        offset = n//2
        while offset > 0:
            for i in range(0, n - offset, offset):
                self.compare_regions(a, i, i + offset, offset)
            for i in range(n - offset, offset - 1, -offset):
                self.compare_regions(a, i - offset, i, offset)
            for i in range(0, n - 3 * offset, offset):
                self.compare_regions(a, i, i + 3 * offset, offset)
            for i in range(0, n - 2 * offset, offset):
                self.compare_regions(a, i, i + 2 * offset, offset)
            for i in range(0, n, 2 * offset):
                self.compare_regions(a, i, i + offset, offset)
            for i in range(offset, n - offset, 2 * offset):
                self.compare_regions(a, i, i + offset, offset)

            offset = offset // 2

if __name__ == "__main__":
    filepaths = ['dataset/small/small_random.txt', 'dataset/small/small_sorted.txt',
                 'dataset/small/small_reverse_sorted.txt',
                 'dataset/medium/medium_random.txt', 'dataset/medium/medium_sorted.txt',
                 'dataset/medium/medium_reverse_sorted.txt',
                 'dataset/large/large_random.txt', 'dataset/large/large_sorted.txt',
                 'dataset/large/large_reverse_sorted.txt']

    print("RANDOMIZED SHELL SORT")
    for filepath in filepaths:
        tracemalloc.start()
        start_time = time.time()
        max_heap_sort = RandomizedShellSort(filepath)
        max_heap_sort.randomized_shell_sort()
        end_time = time.time()
        snapshot = tracemalloc.take_snapshot()
        tracemalloc.stop()
        runtime = (end_time - start_time) * 1000
        print('------' * 20)
        print(f'Runtime of {filepath.split("/")[-1]}: '.ljust(45), str(round(runtime)).ljust(5), " ms")

        top_stats = snapshot.statistics('lineno')
        total = sum(stat.size for stat in top_stats)
        print(f"Total allocated size: {total / 1024} KiB")
