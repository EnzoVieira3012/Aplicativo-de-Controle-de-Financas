class FinanceManager:
    def __init__(self):
        self.transactions = []

    def add_income(self, description, amount):
        self.transactions.append({"type": "income", "description": description, "amount": amount})
        print(f"Receita de {amount} adicionada com sucesso: {description}")

    def add_expense(self, description, amount):
        self.transactions.append({"type": "expense", "description": description, "amount": amount})
        print(f"Despesa de {amount} adicionada com sucesso: {description}")

    def get_summary(self):
        total_income = sum(t["amount"] for t in self.transactions if t["type"] == "income")
        total_expense = sum(t["amount"] for t in self.transactions if t["type"] == "expense")
        balance = total_income - total_expense

        print("\nResumo Financeiro:")
        print(f"Total de Receitas: {total_income}")
        print(f"Total de Despesas: {total_expense}")
        print(f"Saldo: {balance}")

    def show_transactions(self):
        if not self.transactions:
            print("Nenhuma transação registrada.")
        else:
            print("\nTransações:")
            for index, transaction in enumerate(self.transactions):
                t_type = "Receita" if transaction["type"] == "income" else "Despesa"
                print(f"{index + 1}. {t_type} - {transaction['description']}: {transaction['amount']}")

def main():
    manager = FinanceManager()

    while True:
        print("\n1. Adicionar Receita")
        print("2. Adicionar Despesa")
        print("3. Ver Resumo Financeiro")
        print("4. Ver Transações")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            description = input("Digite a descrição da receita: ")
            amount = float(input("Digite o valor da receita: "))
            manager.add_income(description, amount)
        elif choice == '2':
            description = input("Digite a descrição da despesa: ")
            amount = float(input("Digite o valor da despesa: "))
            manager.add_expense(description, amount)
        elif choice == '3':
            manager.get_summary()
        elif choice == '4':
            manager.show_transactions()
        elif choice == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
