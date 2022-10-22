from src.sorting import sort_by


def test_sort_by_criteria():
    MIN_SALARY = "min_salary"
    MAX_SALARY = "max_salary"
    DATE_POSTED = "date_posted"
    criteria = [
        {
            MIN_SALARY: 12000,
            MAX_SALARY: 24000,
            DATE_POSTED: "2022-10-21",
        },
        {
            MIN_SALARY: 28000,
            MAX_SALARY: 38000,
            DATE_POSTED: "2022-12-23",
        },
        {
            MIN_SALARY: 20000,
            MAX_SALARY: 29000,
            DATE_POSTED: "2022-11-22",
        },
    ]
    sort_by(criteria, MIN_SALARY)
    assert criteria[0][MIN_SALARY] == 12000
    sort_by(criteria, MAX_SALARY)
    assert criteria[0][MAX_SALARY] == 38000
    sort_by(criteria, DATE_POSTED)
    assert criteria[0][DATE_POSTED] == "2022-12-23"
