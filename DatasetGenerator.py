import random

class DatasetGenerator:
    def __init__(self, size):
        self._dataset = []
        self._size = size

    def generate_random(self, filename):
        with open(filename, 'w') as f:
            for i in range(self._size):
                num = random.randint(0, self._size)
                f.write(str(num) + '\n')

    def generate_sorted(self, filename):
        with open(filename, 'w') as f:
            for i in range(self._size):
                f.write(str(i) + '\n')

    def generate_reverse_sorted(self, filename):
        with open(filename, 'w') as f:
            for i in range(self._size):
                f.write(str(self._size - i) + '\n')

if __name__ == '__main__':
    small_dataset_generator = DatasetGenerator(2**9)
    medium_dataset_generator = DatasetGenerator(2**13)
    large_dataset_generator = DatasetGenerator(2**16)

    small_dataset_generator.generate_random('small_random.txt')
    medium_dataset_generator.generate_random('medium_random.txt')
    large_dataset_generator.generate_random('large_random.txt')
    
    small_dataset_generator.generate_sorted('small_sorted.txt')
    medium_dataset_generator.generate_sorted('medium_sorted.txt')
    large_dataset_generator.generate_sorted('large_sorted.txt')

    small_dataset_generator.generate_reverse_sorted('small_reverse_sorted.txt')
    medium_dataset_generator.generate_reverse_sorted('medium_reverse_sorted.txt')
    large_dataset_generator.generate_reverse_sorted('large_reverse_sorted.txt')

        