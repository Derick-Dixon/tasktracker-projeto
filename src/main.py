"""TaskTracker - gerenciador de tarefas em linha de comando.

Bootcamp II - Fase 2 (Entrega Intermediária).
"""


def exibir_menu():
    print()
    print("===== TASKTRACKER =====")
    print("1 - Cadastrar nova tarefa")
    print("2 - Visualizar tarefas cadastradas")
    print("3 - Sair da aplicação")


def cadastrar_tarefa(tarefas):
    """Lê os dados da tarefa e guarda na lista (ainda sem validações)."""
    tarefa = {
        "titulo": input("Título: "),
        "descricao": input("Descrição: "),
        "prioridade": input("Prioridade (Alta/Média/Baixa): "),
        "data_limite": input("Data limite (DD/MM/AAAA): "),
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso!")


def listar_tarefas(tarefas):
    """Mostra todas as tarefas ou avisa que a lista está vazia."""
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    print(f"\n===== TAREFAS CADASTRADAS ({len(tarefas)}) =====")
    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"Tarefa {numero}")
        print(f"  Título:      {tarefa['titulo']}")
        print(f"  Descrição:   {tarefa['descricao']}")
        print(f"  Prioridade:  {tarefa['prioridade']}")
        print(f"  Data limite: {tarefa['data_limite']}")
        print(f"  Status:      {tarefa['status']}")
        print("-" * 40)


def main():
    tarefas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            print("Encerrando o TaskTracker. Até logo!")
            break
        else:
            print("Opção inválida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    main()
