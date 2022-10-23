from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    PATH = "tests/mocks/brazilians_jobs.csv"
    expected = [
        {"title": "Maquinista", "salary": "2000", "type": "trainee"},
        {"title": "Motorista", "salary": "3000", "type": "full time"},
    ]
    assert read_brazilian_file(PATH)[0:2] == expected
