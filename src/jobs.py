import csv
from functools import lru_cache


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
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
