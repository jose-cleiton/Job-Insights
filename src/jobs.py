import csv
from functools import lru_cache


@lru_cache
def read(path: str) -> list:
    """Read a CSV file and return a list of dictionaries."""
    dados = []
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for linha in reader:
            dados.append(linha)
    return dados


if __name__ == "__main__":
    # Path to file
    path = "src/jobs.csv"

    # Read the file
    jobs = read(path)

    # Print the first 5 rows
    print(jobs[:5])
