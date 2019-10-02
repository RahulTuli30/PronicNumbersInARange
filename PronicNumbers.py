import math


def getPronicNumberGeneratorInARange(start, end):
    if not start or not end or end < start:
        return None

    start_index, end_index = getStartAndEndLimits(start, end)
    for i in range(start_index, end_index):
        product = i * (i + 1)
        if isProductInRange(product, start, end):
            yield product


def getStartAndEndLimits(start, end):
    return int_sqrt(start), int_sqrt(end) + 1


def int_sqrt(num):
    return int(math.sqrt(num))


def isProductInRange(product, start, end):
    return start <= product <= end


def getCountOfPronicNumbersInARAnge(start, end):
    return get_count(getPronicNumberGeneratorInARange(start, end))


def get_count(generator):
     s = sum(1 for _ in generator)

     return s if s > 0 else 0

def getMessage(passed, testname):
    if passed:
        return "The test : {} Passed succesfully".format(testname)
    return "The test : {} Failed".format(testname)


def test_counter(start, end, output):
    print(getMessage(getCountOfPronicNumbersInARAnge(start, end) == output,
                     testname="Counter Test"))


def test_generator(start, end, output):
    passed = True

    for i, j in zip(getPronicNumberGeneratorInARange(start, end), output):
        if i is not j:
            print(getMessage(not passed, "Generator Test"))
            return

    print(getMessage(passed, "Generator Test"))


def _getListFromGenerator(generator):
    return [_ for _ in generator]



def main():
    test_generator(start=6, end=21, output=[6, 12, 20])
    test_counter(start=6, end=21, output=3)

    test_generator(start=21, end=29, output=[])
    test_counter(start=21, end=29, output=0)

    test_generator(start=1, end=100,
                   output=[2, 6, 12, 20, 30, 42, 56, 72, 90])
    test_counter(start=1, end=100, output=9)

    #print(_getListFromGenerator(getPronicNumberGeneratorInARange(1, 100)))


if __name__ == '__main__':
    main()
