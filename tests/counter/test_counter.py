from src.counter import count_ocurrences


def test_counter():
    path = "src/jobs.csv"
    word = "Python".lower()
    assert count_ocurrences(path, word) == 3
