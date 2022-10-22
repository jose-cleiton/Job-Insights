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


def filter_by_job_type(jobs: list, job_type: str) -> list:
    """Filtrar lista de trabalhos por tipo de trabalho

    Parâmetros
    ----------
    jobs: list
        Lista de trabalhos
    job_type: str
        Tipo de trabalho

    Devoluções
    -------
    Lista
        Lista de trabalhos filtrada
    """
    filtered_jobs = []

    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs
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


def get_unique_industries(path: str) -> list:
    jobs_data = read(path)
    unique_industries = set()

    for job in jobs_data:
        unique_industries.add(job["industry"])
    unique_industries = unique_industries - {""}

    return list(unique_industries)


def filter_by_industry(jobs: dict, industry: str) -> list:

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


def get_min_salary(path: str) -> int:
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

    try:
        salary_max = int(job["max_salary"])
        salary_min = int(job["min_salary"])
        salary = int(salary)
        assert salary_min <= salary_max
    except (AssertionError, ValueError, TypeError, KeyError):
        raise ValueError("min_salary is greather than max_salary")
    else:
        return salary >= salary_min and salary <= salary_max


def filter_by_salary_range(jobs: dict, salary: int) -> list:
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
    job_in_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                job_in_range.append(job)
        except ValueError:
            continue
    return job_in_range


if __name__ == "__main__":
    # Path to file
    path = "src/jobs.csv"
    print(get_unique_job_types(path))
