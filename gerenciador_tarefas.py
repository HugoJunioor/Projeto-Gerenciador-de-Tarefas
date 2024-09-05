import sqlite3

# Função para criar a tabela de tarefas no banco de dados
def criar_tabela():
    conn = sqlite3.connect('tarefas.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tarefas
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 titulo TEXT,
                 descricao TEXT,
                 status TEXT)''')
    conn.commit()
    conn.close()

# Função para adicionar uma nova tarefa
def adicionar_tarefa(titulo, descricao=''):
    conn = sqlite3.connect('tarefas.db')
    c = conn.cursor()
    c.execute("INSERT INTO tarefas (titulo, descricao, status) VALUES (?, ?, ?)", (titulo, descricao, 'Pendente'))
    conn.commit()
    conn.close()

# Função para visualizar todas as tarefas
def visualizar_tarefas():
    conn = sqlite3.connect('tarefas.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tarefas")
    tarefas = c.fetchall()
    conn.close()
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for tarefa in tarefas:
            print("ID:", tarefa[0])
            print("Título:", tarefa[1])
            print("Descrição:", tarefa[2])
            print("Status:", tarefa[3])
            print()

# Função para atualizar os status, título e descrição de uma tarefa
def atualizar_tarefa(id, novo_titulo=None, nova_descricao=None, novo_status=None):
    conn = sqlite3.connect('tarefas.db')
    c = conn.cursor()

    if novo_status:
        c.execute("UPDATE tarefas SET status=? WHERE id=?", (novo_status, id))
    if novo_titulo:
        c.execute("UPDATE tarefas SET titulo=? WHERE id=?", (novo_titulo, id))
    if nova_descricao:
        c.execute("UPDATE tarefas SET descricao=? WHERE id=?", (nova_descricao, id))

    conn.commit()
    conn.close()

# Função para excluir uma tarefa
def excluir_tarefa(id):
    conn = sqlite3.connect('tarefas.db')
    c = conn.cursor()
    c.execute("DELETE FROM tarefas WHERE id=?", (id,))
    conn.commit()
    conn.close()

# Interface de linha de comando simples
def main():
    criar_tabela()
    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Atualizar Tarefa")
        print("4. Excluir Tarefa")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Digite o título da tarefa: ")
            descricao = input("Digite a descrição da tarefa (opcional): ")
            adicionar_tarefa(titulo, descricao)
        elif opcao == '2':
            visualizar_tarefas()
        elif opcao == '3':
            id = input("Digite o ID da tarefa que deseja atualizar: ")
            novo_titulo = input("Digite o novo título da tarefa (deixe em branco para manter o mesmo): ")
            nova_descricao = input("Digite a nova descrição da tarefa (deixe em branco para manter a mesma): ")
            novo_status = input("Digite o novo status da tarefa (deixe em branco para manter o mesmo): ")
            atualizar_tarefa(id, novo_titulo, nova_descricao, novo_status)
        elif opcao == '4':
            id = input("Digite o ID da tarefa que deseja excluir: ")
            excluir_tarefa(id)
        elif opcao == '5':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
