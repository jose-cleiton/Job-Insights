from src.sorting import sort_by


def test_sort_by_criteria():
    MIN_SALARY = "min_salary"
    MAX_SALARY = "max_salary"
    DATE_POSTED = "date_posted"
    criteria = [
        {
            "min_salary": 12000,
            "max_salary": 24000,
            "date_posted": "2022-10-21",
        },
        {
            "min_salary": 28000,
            "max_salary": 38000,
            "date_posted": "2022-12-23",
        },
        {
            "min_salary": 20000,
            "max_salary": 29000,
            "date_posted": "2022-11-22",
        },
    ]
    sort_by(criteria, MIN_SALARY)
    assert criteria[0][MIN_SALARY] == 12000
    sort_by(criteria, MAX_SALARY)
    assert criteria[0][MAX_SALARY] == 38000
    sort_by(criteria, DATE_POSTED)
    assert criteria[0][DATE_POSTED] == "2022-12-23"
