# 🏦 Sistema Bancário - Documentação das Funções

Este projeto é um sistema bancário simples em Python, com operações de saque, depósito, extrato, cadastro de usuários e contas.

---

## ✍️ Funções com Parâmetros Nomeados Obrigatórios

### `saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques)`
- **Parâmetros:** Todos obrigatórios e nomeados.
- **Validações:**
  - ❌ Valor do saque maior que o saldo → operação falha.
  - ❌ Valor do saque maior que o limite permitido → operação falha.
  - ❌ Número de saques diário excedido → operação falha.
  - ❌ Valor negativo → operação falha.
- **Retorno:** Tupla com saldo, extrato e número de saques atualizados.

---

### `imprimir_extrato(saldo, /, *, extrato)`
- **Parâmetros:** `saldo` posicional, `extrato` nomeado obrigatório.
- **Validações:** Não realiza validações, apenas exibe o extrato e saldo formatados.

---

## 🔢 Funções com Parâmetros de Posição Obrigatórios

### `deposito(saldo, valor, extrato, /)`
- **Parâmetros:** Todos obrigatórios e posicionais.
- **Validações:**
  - ❌ Valor negativo → operação falha.
- **Retorno:** Tupla com saldo e extrato atualizados.

---

## 🛡️ Observações Gerais

- As funções usam parâmetros nomeados e posicionais para garantir clareza e evitar erros de chamada.
- As principais validações garantem integridade dos dados (valores negativos, limites de saque, existência de saldo).
- O sistema imprime mensagens de erro quando alguma validação falha, sem alterar os dados.

---

Para mais detalhes, consulte o código-fonte em `app.py`. 🚀