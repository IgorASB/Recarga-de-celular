from datetime import datetime
import os

class Recarga:
    """Representa uma recarga realizada."""
    def __init__(self, operadora: str, ddd: str, numero: str, valor: float, comissao: float):
        self.operadora = operadora.upper()
        self.ddd = ddd
        self.numero = numero
        self.valor = valor
        self.comissao = comissao
        self.data_hora = datetime.now()

    def __str__(self):
        return (f"{self.data_hora.strftime('%d/%m/%Y %H:%M:%S')} | "
                f"{self.operadora} | {self.ddd} {self.numero} | "
                f"Recarga: R$ {self.valor:.2f} | Comissão: R$ {self.comissao:.2f}")

class Intermediario:
    """Gerencia saldo, extrato e operações do intermediário."""
    COMISSAO_PERCENTUAL = 0.01  # 1%
    SAQUE_MINIMO = 100.0

    def __init__(self):
        self.saldo = 0.0
        self.extrato = []  # lista de objetos Recarga

    def adicionar_recarga(self, operadora: str, ddd: str, numero: str, valor: float) -> bool:
        """Registra uma recarga, calcula comissão e atualiza saldo. Retorna True se sucesso."""
        if valor < 10.0:
            print("Erro: O valor mínimo da recarga é R$ 10,00.")
            return False
        comissao = valor * self.COMISSAO_PERCENTUAL
        self.saldo += comissao
        recarga = Recarga(operadora, ddd, numero, valor, comissao)
        self.extrato.append(recarga)
        print(f"Recarga efetuada com sucesso! Comissão de R$ {comissao:.2f} adicionada ao saldo.")
        return True

    def exibir_saldo(self):
        print(f"Seu saldo atual (comissões acumuladas): R$ {self.saldo:.2f}")

    def exibir_extrato(self):
        print("\n--- EXTRATO DE RECARGAS ---")
        if not self.extrato:
            print("Nenhuma recarga realizada ainda.")
        else:
            for recarga in self.extrato:
                print(recarga)
        print("----------------------------")

    def sacar(self, valor: float) -> bool:
        """Realiza saque se saldo >= 100 e valor válido. Retorna True se sucesso."""
        if self.saldo < self.SAQUE_MINIMO:
            print(f"Erro: Saldo insuficiente para saque. Mínimo necessário: R$ {self.SAQUE_MINIMO:.2f}")
            return False
        if valor < self.SAQUE_MINIMO:
            print(f"Erro: O valor mínimo de saque é R$ {self.SAQUE_MINIMO:.2f}.")
            return False
        if valor > self.saldo:
            print(f"Erro: Valor solicitado excede o saldo disponível (R$ {self.saldo:.2f}).")
            return False
        self.saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso! Novo saldo: R$ {self.saldo:.2f}")
        return True

def validar_operadora(operadora: str) -> bool:
    """Valida se a operadora é uma das permitidas."""
    return operadora.upper() in ["TIM", "CLARO", "VIVO", "OI"]

def validar_ddd(ddd: str) -> bool:
    """Valida se DDD tem 2 dígitos numéricos."""
    return ddd.isdigit() and len(ddd) == 2

def validar_numero(numero: str) -> bool:
    """Valida se número de telefone tem entre 8 e 9 dígitos (celular) e é numérico."""
    return numero.isdigit() and 8 <= len(numero) <= 9

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    intermediario = Intermediario()
    while True:
        print("\n" + "=" * 30)
        print("   SISTEMA DE RECARGAS")
        print("=" * 30)
        print("[1] Recarga")
        print("[2] Saldo")
        print("[3] Extrato")
        print("[4] Sacar")
        print("[Q] Sair")
        print("=" * 30)

        opcao = input("Escolha a opção: ").strip().upper()

        if opcao == "1":
            # Recarga
            while True:
                operadora = input("Informe a operadora (TIM, CLARO, VIVO, OI): ").strip()
                if validar_operadora(operadora):
                    break
                print("Operadora inválida! Escolha entre TIM, CLARO, VIVO ou OI.")
            while True:
                ddd = input("Informe o DDD (2 dígitos): ").strip()
                if validar_ddd(ddd):
                    break
                print("DDD inválido! Deve conter 2 dígitos numéricos.")
            while True:
                numero = input("Informe o número de telefone (8 ou 9 dígitos): ").strip()
                if validar_numero(numero):
                    break
                print("Número inválido! Deve conter 8 ou 9 dígitos numéricos.")
            while True:
                try:
                    valor = float(input("Informe o valor da recarga (mínimo R$ 10,00): R$ "))
                    if valor >= 10.0:
                        break
                    print("Valor mínimo é R$ 10,00.")
                except ValueError:
                    print("Valor inválido. Digite um número.")
            intermediario.adicionar_recarga(operadora, ddd, numero, valor)

        elif opcao == "2":
            intermediario.exibir_saldo()

        elif opcao == "3":
            intermediario.exibir_extrato()

        elif opcao == "4":
            if intermediario.saldo < Intermediario.SAQUE_MINIMO:
                print(f"Saldo insuficiente para saque. Mínimo necessário: R$ {Intermediario.SAQUE_MINIMO:.2f}")
            else:
                while True:
                    try:
                        valor = float(input("Quanto você deseja sacar? R$ "))
                        if intermediario.sacar(valor):
                            break
                    except ValueError:
                        print("Valor inválido. Digite um número.")

        elif opcao == "Q":
            print("Encerrando o sistema de recargas. Obrigado!")
            break

        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")
        limpar_tela()

if __name__ == "__main__":
    main()