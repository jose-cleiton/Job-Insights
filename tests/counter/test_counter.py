from src.counter import count_ocurrences


def test_counter():
    path = "src/jobs.csv"
    word = "Python".lower()
    assert count_ocurrences(path, "React") == 141, "Should be 141"
    assert count_ocurrences(path, word) == 1639, "Should be 1639"
    assert count_ocurrences(path, "Java") == 676, "Should be 676"
