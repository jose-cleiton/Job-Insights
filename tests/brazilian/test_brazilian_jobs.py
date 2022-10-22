from unittest.mock import patch

from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    """
    Teste se a função retorna os dados esperados"""
    expected_of_returned = [
        {
            "title": "Analista de Sistemas",
            "salary": "R$ 3.000,00",
            "type": "CLT",
        },
        {
            "title": "Analista de Sistemas",
            "salary": "R$ 3.000,00",
            "type": "CLT",
        },
    ]
    with patch("src.brazilian_jobs.jobs.read") as mock:
        mock.return_value = [
            {
                "titulo": "Analista de Sistemas",
                "salario": "R$ 3.000,00",
                "tipo": "CLT",
            },
            {
                "titulo": "Analista de Sistemas",
                "salario": "R$ 3.000,00",
                "tipo": "CLT",
            },
        ]
        assert (
            read_brazilian_file("path") == expected_of_returned
        ), "Deveria retornar os dados esperados"
