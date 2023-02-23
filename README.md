# Job Insights

O Job Insights é um aplicativo de linha de comando que permite buscar vagas de emprego e obter informações sobre elas.

## Estrutura de pastas

O projeto é dividido em duas pastas principais:

- "src/": uma pasta que contém os arquivos de código-fonte Python do projeto.
- "tests/": uma pasta que contém os arquivos de teste do projeto.

## Pré-requisitos

Para usar o Job Insights, você precisará ter instalado os seguintes pré-requisitos em seu sistema:

- Python 3.6 ou superior
- Bibliotecas Python "requests", "beautifulsoup4" e "pandas"

## Instalação

Para instalar as dependências do projeto, execute o seguinte comando:

```bash
pip install -r requirements.txt

```

## Execução

Para executar o aplicativo, execute o seguinte comando:

```bash
python -m src.app

```
## Docker

Para executar o aplicativo em um container Docker, execute o seguinte comando:

```bash
docker commpose up -d
  
  ```

  URL:

  ```bash	
http://localhost:5000/jobs
  
  ```

## Testes

Para executar os testes do projeto, execute o seguinte comando:

```bash
python -m unittest discover -s tests

```

## Contribuição

Se você deseja contribuir para o projeto, por favor siga as seguintes etapas:

1. Faça um fork do projeto.
2. Crie uma branch para suas alterações.
3. Faça as alterações e commit suas mudanças.
4. Envie um pull request para que suas alterações possam ser revisadas.

## Licença

O Job Insights está licenciado sob a licença MIT. Consulte o arquivo %%%"LICENSE"%%% para obter mais detalhes.

