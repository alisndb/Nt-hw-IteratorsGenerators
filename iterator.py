import itertools


class FlatIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list

    def __iter__(self):
        self._values = iter(self.nested_list)
        return self

    def __next__(self):
        next_value = next(self._values)
        if isinstance(next_value, list):
            self._values = itertools.chain(self._values, next_value)
            return next(self)
        return next_value


nested_list = [['a', 'b', 'c'],
               ['d', 'e', 'f', 'h', False],
               [1, 2, None]]

if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
