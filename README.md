# Sistema de Recarga de Celular (POO)

Sistema desenvolvido em Python utilizando Programação Orientada a Objetos para simular um intermediário de recargas de celular. O programa permite realizar recargas, acumular comissão de 1% sobre cada recarga, consultar saldo, visualizar extrato detalhado e sacar o saldo (mínimo de R$ 100,00).

## Funcionalidades

### Menu principal
- **1 - Recarga** – Solicita operadora (TIM, CLARO, VIVO, OI), DDD (2 dígitos), número (8 ou 9 dígitos) e valor (mínimo R$ 10,00). A cada recarga, o intermediário recebe 1% de comissão, que é adicionado ao saldo.
- **2 - Saldo** – Exibe o saldo atual acumulado (total de comissões).
- **3 - Extrato** – Lista todas as recargas realizadas com data, hora, operadora, DDD, número, valor da recarga e comissão ganha.
- **4 - Sacar** – Permite sacar o saldo desde que o saldo seja igual ou superior a R$ 100,00. O valor do saque não pode ser menor que R$ 100,00 nem maior que o saldo disponível.
- **Q - Sair** – Encerra o programa.

## Estrutura do Código

- **Classe `Recarga`** – Representa uma transação de recarga, armazenando operadora, DDD, número, valor, comissão e data/hora.
- **Classe `Intermediario`** – Gerencia saldo e lista de recargas. Métodos:
  - `adicionar_recarga()` – Valida e registra recarga, calcula comissão (1%).
  - `exibir_saldo()` – Mostra saldo atual.
  - `exibir_extrato()` – Exibe todas as recargas realizadas.
  - `sacar()` – Realiza saque com validações de saldo mínimo e valor.
- **Funções auxiliares** – Validação de operadora, DDD, número de telefone, limpeza de tela.
- **Loop principal** – Menu interativo.
