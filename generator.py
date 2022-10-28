import itertools


def flat_generator(nested_list):
    for i in itertools.chain(*nested_list):
        yield i


nested_list = [['a', 'b', 'c'],
               ['d', 'e', 'f'],
               [1, 2, None]]

if __name__ == '__main__':
    for item in flat_generator(nested_list):
        print(item)
