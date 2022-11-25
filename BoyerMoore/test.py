import time
from BoyerMoore.boyer_moore import main


def test_algo_average():
    with open("text.txt", "r") as file:
        text = str(file.read())
    search_pattern = "cowboy"

    start = time.time()
    main(text, search_pattern)
    end = time.time()

    print("AVG case")
    print(f"The time of execution of above program is : {(end-start) * 10**3:.03f}ms")


def test_algo_worst():
    with open("other_cases.txt", "r") as file:
        text = str(file.read())
    search_pattern = "afffff"

    start = time.time()
    main(text, search_pattern)
    end = time.time()

    print("WORST case")
    print(f"The time of execution of above program is : {(end-start) * 10**3:.03f}ms")


def test_algo_best():
    with open("other_cases.txt", "r") as file:
        text = str(file.read())
    search_pattern = "gggggg"

    start = time.time()
    main(text, search_pattern)
    end = time.time()

    print("BEST case")
    print(f"The time of execution of above program is : {(end-start) * 10**3:.03f}ms")


if __name__ == '__main__':
    test_algo_average()
    test_algo_worst()
    test_algo_best()

