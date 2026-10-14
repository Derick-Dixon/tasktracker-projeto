"""TaskTracker - gerenciador de tarefas em linha de comando.

Bootcamp II - Fase 2 (Entrega Intermediária).
"""

# Aceita só estas prioridades (sem diferenciar maiúsculas/minúsculas).
# A chave é o que o usuário digita; o valor é como fica salvo.
PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "média": "Média",
    "media": "Média",
    "baixa": "Baixa",
}


def exibir_menu():
    print()
    print("===== TASKTRACKER =====")
    print("1 - Cadastrar nova tarefa")
    print("2 - Visualizar tarefas cadastradas")
    print("3 - Sair da aplicação")


def ler_titulo():
    """Pede o título até receber um que não seja vazio nem só espaços."""
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            return titulo
        print("Erro: o título é obrigatório e não pode ficar vazio.")


def ler_prioridade():
    """Pede a prioridade até receber Alta, Média/Media ou Baixa."""
    while True:
        entrada = input("Prioridade (Alta/Média/Baixa): ").strip().lower()
        if entrada in PRIORIDADES_VALIDAS:
            return PRIORIDADES_VALIDAS[entrada]
        print("Erro: prioridade inválida. Use Alta, Média ou Baixa.")


def cadastrar_tarefa(tarefas):
    """Lê os dados (com validação) e guarda a tarefa na lista."""
    titulo = ler_titulo()
    descricao = input("Descrição: ").strip() or "Sem descrição"
    prioridade = ler_prioridade()
    data_limite = input("Data limite (DD/MM/AAAA): ").strip() or "Não informada"

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",  # sempre Pendente no cadastro
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

    try:
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
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C / Ctrl+D: sai sem mostrar erro feio no terminal
        print("\nEncerrando o TaskTracker. Até logo!")


if __name__ == "__main__":
    main()
