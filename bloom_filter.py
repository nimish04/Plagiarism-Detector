from bitarray import *


class ff_bloom_filter:
    def __init__(self, size):
        self.size = size
        self.first_filter, self.second_filter = bitarray(size), bitarray(size)
        self.first_filter.setall(0)
        self.second_filter.setall(0)

    def set_bit(self, filter_no, indices):
        for idx in indices:
            if filter_no == 1:
                self.first_filter[int(idx)] = 1
            else:
                self.second_filter[int(idx)] = 1

    def look_up(self, filter_no, indices):
        for idx in indices:
            if filter_no == 1 and not self.first_filter[int(idx)]:
                return False
            if filter_no == 2 and not self.second_filter[int(idx)]:
                return False
        return True

    def display(self):
        print (self.b_filter)


if __name__ == "__main__":
    bf = ff_bloom_filter(20)
    bf.display()
    bf.roll_hash([], [1, 2, 3, 4, 5, 6, 7])
