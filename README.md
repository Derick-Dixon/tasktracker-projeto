# TaskTracker

Gerenciador de tarefas simples em **linha de comando (CLI)**, feito em Python 3 e empacotado com **Docker**.
Projeto do **Bootcamp II** — Engenharia de Software, Versionamento Profissional de Código e Desenvolvimento de Sistemas (Fase 3 — Entrega Final).

**Autor:** Dérick Dixon Xavier Rodrigues — Ciência da Computação, CEUB (Brasília)

---

## Descrição funcional

O TaskTracker permite cadastrar tarefas e visualizá-las no terminal por meio de um menu contínuo:

```
1 - Cadastrar nova tarefa
2 - Visualizar tarefas cadastradas
3 - Sair da aplicação
```

Cada tarefa possui:

| Campo       | Regra                                                                                   |
|-------------|-----------------------------------------------------------------------------------------|
| Título      | **Obrigatório.** Entradas vazias ou só com espaços são rejeitadas e o prompt se repete. |
| Descrição   | Texto livre.                                                                            |
| Prioridade  | **Somente** `Alta`, `Média` (ou `Media`) e `Baixa`. Qualquer outro valor gera erro.     |
| Data limite | Texto livre ou `DD/MM/AAAA`.                                                            |
| Status      | Definido automaticamente como `Pendente` no cadastro.                                   |

Se nenhuma tarefa foi cadastrada, a opção 2 informa que não há registros.
Os dados ficam apenas em memória (a lista é perdida ao encerrar o programa).

## Tecnologias

- Python 3.11 (somente biblioteca padrão, sem dependências externas)
- Docker e Docker Compose (empacotamento e execução isolada)
- Git e GitHub para versionamento

## Estrutura do repositório

```
tasktracker-projeto/
├── .gitignore                      # Ignora __pycache__/, *.pyc e .venv/
├── docs/
│   └── planejamento_logico.pdf     # Planejamento lógico e arquitetural (Fase 1)
├── src/
│   └── main.py                     # Código-fonte da aplicação (Fase 2)
├── Dockerfile                      # Receita da imagem Docker (Fase 3)
├── docker-compose.yml              # Orquestração da execução interativa (Fase 3)
└── README.md                       # Este arquivo
```

## Como executar com Docker

**Pré-requisito:** [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado e **aberto** (ícone da baleia ativo). Rode os comandos abaixo no terminal, dentro da pasta do projeto.

Como construir a imagem:

```
docker build -t tasktracker-app .
```

Como rodar o container em modo isolado:

```
docker run -it tasktracker-app
```

Como rodar via orquestração (Recomendado):

```
docker compose run tasktracker-app
```

> O `-it` (no `docker run`) e o `stdin_open` + `tty` (no `docker-compose.yml`) são necessários porque a aplicação usa `input()`: eles mantêm o teclado conectado ao container e simulam um terminal.

### O que cada arquivo faz

| Arquivo              | Papel                                                                                                  |
|----------------------|--------------------------------------------------------------------------------------------------------|
| `Dockerfile`         | A receita: parte de `python:3.11-slim`, define `/app`, copia `src/` e executa `python src/main.py`.    |
| `docker-compose.yml` | O maestro: monta o serviço `tasktracker-app` com `stdin_open: true` e `tty: true` para a CLI interativa. |

## Como executar sem Docker (opcional)

1. Instale o [Python 3](https://www.python.org/downloads/) (marque *Add Python to PATH* no instalador).
2. Clone o repositório:
   ```
   git clone https://github.com/Derick-Dixon/tasktracker-projeto.git
   cd tasktracker-projeto
   ```
3. Execute a aplicação:
   ```
   python src/main.py
   ```
   (em Linux/macOS, use `python3 src/main.py`)

## Exemplo de uso

```
===== TASKTRACKER =====
1 - Cadastrar nova tarefa
2 - Visualizar tarefas cadastradas
3 - Sair da aplicação
Escolha uma opção: 1
Título: 
Erro: o título é obrigatório e não pode ficar vazio.
Título: Estudar para a prova de BD
Descrição: Revisar normalização até a 3FN
Prioridade (Alta/Média/Baixa): urgente
Erro: prioridade inválida. Use Alta, Média ou Baixa.
Prioridade (Alta/Média/Baixa): Alta
Data limite (DD/MM/AAAA): 20/10/2026
Tarefa cadastrada com sucesso!
```

## Evolução do projeto

| Fase | Foco                                                        |
|------|-------------------------------------------------------------|
| 1    | Planejamento lógico, pseudocódigo e arquitetura de dados    |
| 2    | Repositório Git/GitHub, CLI em Python e regras de negócio   |
| 3    | Empacotamento com Docker, orquestração com Compose e deploy |
