from logging import exception

from src.jobs import read


def get_unique_job_types(path: str) -> list:
    """Checks all different job types and returns a list of them

    Deve chamar `read`

       Parâmetros
       ----------
       caminho: str
           Deve ser passado para `read`

       Devoluções
       -------
       Lista
           Lista de tipos de trabalho exclusivos
    """
    jobs_data = read(path)
    unique_jobs = set()

    for job in jobs_data:
        unique_jobs.add(job["job_type"])

    return list(unique_jobs)


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    filtered_job = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_job.append(job)

    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    jobs_data = read(path)
    unique_industries = set()

    for job in jobs_data:
        unique_industries.add(job["industry"])
    unique_industries = unique_industries - {""}

    return list(unique_industries)


def filter_by_industry(jobs: dict, industry: str) -> list:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    filtered_industry = []
    for j in jobs:
        if j["industry"] == industry:
            filtered_industry.append(j)

    return filtered_industry


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    max_salaries = []
    jobs_data = read(path)
    for job in jobs_data:
        try:
            max_salaries.append(int(job["max_salary"]))
        except ValueError:
            continue
    return max(max_salaries)


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    min_salaries = []
    jobs_data = read(path)
    for job in jobs_data:
        try:
            min_salaries.append(int(job["min_salary"]))
        except ValueError:
            continue
    return min(min_salaries)


def matches_salary_range(job: dict, salary: int):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

    try:
        salary_max = int(job["max_salary"])
        salary_min = int(job["min_salary"])
        salary = int(salary)
        assert salary_min <= salary_max
    except AssertionError:
        raise ValueError("min_salary is greather than max_salary")
    except ValueError:
        raise ValueError("Invalid salary range")
    except TypeError:
        raise ValueError("Salary or salary range is not an integer")
    except KeyError:
        raise ValueError("Salary is missing")
    else:
        return salary >= salary_min and salary <= salary_max


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []


if __name__ == "__main__":
    # Path to file
    path = "src/jobs.csv"
    print(get_unique_job_types(path))
