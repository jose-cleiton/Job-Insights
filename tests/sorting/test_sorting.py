from src.sorting import sort_by
from tests.sorting.mock_jobs import jobs


def test_sort_by_criteria():
    MIN_SALARY = "min_salary"
    MAX_SALARY = "max_salary"
    DATE_POSTED = "date_posted"

    sort_by(jobs, MIN_SALARY)
    assert jobs[0][MIN_SALARY] == 12000
    sort_by(jobs, MAX_SALARY)
    assert jobs[0][MAX_SALARY] == 38000
    sort_by(jobs, DATE_POSTED)
    assert jobs[0][DATE_POSTED] == "2022-12-23"
