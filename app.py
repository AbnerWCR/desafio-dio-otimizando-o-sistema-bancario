from re import I


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        return

    if valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
        return

    if numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        return

    if valor < 0:
        print("Operação falhou! O valor informado é inválido.")
        return

    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}\n"
    numero_saques += 1

    return saldo, extrato, numero_saques

def deposito(saldo, valor, extrato, /):
    if valor < 0:
        print("Operação falhou! O valor informado é inválido.")
        return
    
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"

    return saldo, extrato

def imprimir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(nome, data_nasc, cpf, endereco):

    if len(cpf) <= 0:
        print("O CPF Informado é inválido")
        return 


    return {
        "nome": nome,
        "data_nascimento": data_nasc,
        "cpf": str(cpf).replace(".", "").replace("-", "").strip(),
        "endereco": endereco
    }

def buscar_usuario_por_cpf(cpf: str, lista_usuarios: list[dict]):
    if len(cpf) <= 0:
        print("O CPF Informado é inválido")
        return 
    
    usuarios = [user for user in lista_usuarios if user.get("cpf") == str(cpf).replace(".", "").replace("-", "").strip()]

    return usuarios[0] if len(usuarios) > 0 else None

def usuario_existe(cpf: str, lista_usuarios: list[dict]):

    if len(cpf) <= 0:
        print("O CPF Informado é inválido")
        return 

    return buscar_usuario_por_cpf(cpf, lista_usuarios) is not None

def criar_conta(cpf_usuario, numero_conta, lista_usuarios):
    if not usuario_existe(cpf_usuario, lista_usuarios):
        print("Usuário não existe. Crie um novo usuário")
        return
    
    return {
        "agencia": "0001",
        "numero_conta": str(numero_conta).zfill(5),
        "cpf_usuario": str(cpf_usuario).replace(".", "").replace("-", "").strip(),
        "saldo": 0,
        "limite": 500,
        "extrato": "",
        "numero_saques": 0,
        "limite_saques": 3
    }

def buscar_conta_por_numero(numero_conta: str, lista_contas: list[dict]):
    contas = [conta for conta in lista_contas if conta.get("numero_conta") == numero_conta]

    return contas[0] if len(contas) > 0 else None

def listar_contas_por_cpf(cpf: str, lista_contas: list[dict]):

    if len(cpf) <= 0:
        print("O CPF Informado é inválido")
        return 
    
    contas = [conta for conta in lista_contas 
              if conta.get("cpf_usuario") == str(cpf).replace(".", "").replace("-", "").strip()]
    
    if len(contas) <= 0:
        print("O CPF não possui contras vinculadas. Crie uma conta para prosseguir")
        return
    
    return contas

def imprimir_contas(lista_contas: list[dict]):
    for conta in lista_contas:
        print(f"Agência: {conta.get('agencia')} - Número da conta: {conta.get("numero_conta")}")

def menu(saldo, limite, extrato, numero_saques, limite_saques):
    texto_menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    while True:
        opcao = input(texto_menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            result = deposito(saldo, valor, extrato)
            
            if result is not None:
                saldo, extrato = result

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            result = saque(saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques)
            
            if result is not None:
                saldo, extrato, numero_saques = result

        elif opcao == "e":
            imprimir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
    return saldo, extrato, numero_saques

def main():
    lista_usuarios = []
    lista_contas = []
    seq_numero_conta = 1

    texto_menu = """
    =========================================
    ===== Bem vindo ao sistema bancário =====
    =========================================

    Opções:

    [c] Cadastrar Usuário
    [a] Criar Conta
    [e] Entrar
    [q] Sair

    => """
    while True:

        opcao = str(input(texto_menu)).strip().lower()

        if opcao == "c":
            nome = input("Informe o nome: ") 
            data_nasc = input("Informe a data de nascimento (ex.: dd/mm/yyyy): ")
            cpf = input("Informe o CPF (ex.: 000.000.000-00): ")
            endereco = input("Informe o endereço no formato (logradouro, numero - bairro - cidade/UF): ")

            novo_usuario = criar_usuario(nome, data_nasc, cpf, endereco)
            
            if novo_usuario is not None:
                lista_usuarios.append(novo_usuario)

            print("Usuário criado com sucesso")

        elif opcao == "a":
            cpf = input("Informe o CPF (ex.: 000.000.000-00): ")

            nova_conta = criar_conta(cpf, seq_numero_conta, lista_usuarios)

            if nova_conta is not None:
                lista_contas.append(nova_conta)
                seq_numero_conta += 1

            print("Conta criada com sucesso")

        elif opcao == "e":
            cpf = input("Informe o CPF (ex.: 000.000.000-00): ")

            if not usuario_existe(cpf, lista_usuarios):
                print("Usuário não existe. Crie um novo usuário")
                continue
            
            user = buscar_usuario_por_cpf(cpf, lista_usuarios)
            contas = listar_contas_por_cpf(cpf, lista_contas)

            print("Contas do usuário: ")
            imprimir_contas(contas)

            numero_conta = input("Informe o número da conta desejada: ")

            conta = buscar_conta_por_numero(numero_conta, lista_contas)

            if conta is None:
                print("O número da conta informado não existe")
                continue

            for conta_banco in [conta for conta in lista_contas if conta.get("numero_conta") == numero_conta]:
                saldo = conta_banco.get("saldo")
                limite = conta_banco.get("limite")
                extrato = conta_banco.get("extrato")
                numero_saques = conta_banco.get("numero_saques")
                limite_saques = conta_banco.get("limite_saques")

                saldo, extrato, numero_saques = menu(saldo, limite, extrato, numero_saques, limite_saques)

                conta_banco["saldo"] = saldo
                conta_banco["extrato"] = extrato
                conta_banco["numero_saques"] = numero_saques
                    
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()

            
