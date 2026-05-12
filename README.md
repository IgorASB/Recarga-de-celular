# 📱 Sistema de Recarga de Celular (POO)

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Paradigma](https://img.shields.io/badge/Paradigma-POO-6A0DAD?style=for-the-badge)]()
[![Interface](https://img.shields.io/badge/Interface-CLI-black?style=for-the-badge)]()
[![Status](https://img.shields.io/badge/Status-Concluído-28a745?style=for-the-badge)]()

</div>

> Sistema em Python com POO que simula um intermediário de recargas de celular. Realiza recargas para as principais operadoras, acumula comissão de 1% por recarga, exibe extrato detalhado e permite saque do saldo acumulado.

---

## ⚙️ Funcionalidades

| Opção | Ação | Detalhe |
|---|---|---|
| `1` | Recarga | Operadora (TIM/CLARO/VIVO/OI), DDD, número e valor (mín. R$ 10,00). Gera 1% de comissão |
| `2` | Saldo | Exibe o saldo atual acumulado de comissões |
| `3` | Extrato | Lista todas as recargas com data, hora, operadora, número, valor e comissão |
| `4` | Saque | Saca o saldo se ≥ R$ 100,00. Valor mín. de saque: R$ 100,00 |
| `Q` | Sair | Encerra o programa |

---

## 💼 Regras de Negócio

- **Comissão:** 1% do valor de cada recarga é adicionado ao saldo do intermediário
- **Valor mínimo de recarga:** R$ 10,00
- **Saque mínimo:** R$ 100,00 (não pode exceder o saldo)
- **DDD:** Deve ter exatamente 2 dígitos
- **Número:** 8 ou 9 dígitos
- **Operadoras aceitas:** TIM, CLARO, VIVO, OI

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.10 ou superior — verifique com `python --version`

### Passos

```bash
# 1. Clone o repositório
git clone https://github.com/IgorASB/Recarga-de-celular.git
cd Recarga-de-celular

# 2. Execute
python recarga_celular.py
```

---

## 🧠 Conceitos de Python Aplicados

| Conceito | Aplicação no Projeto |
|---|---|
| Classes e Objetos | `Recarga` e `Intermediario` representam as entidades do domínio |
| Encapsulamento | Lógica de validação e cálculo de comissão dentro dos métodos da classe |
| Listas | `Intermediario` mantém lista de objetos `Recarga` para o extrato |
| `datetime` | Registro de data e hora de cada transação de recarga |
| Funções auxiliares | Validação de operadora, DDD e número de telefone |
| `f-strings` | Formatação dinâmica dos valores monetários no extrato |

---

## 📁 Estrutura do Projeto

```
Recarga-de-celular/
├── recarga_celular.py   # Código-fonte principal
└── README.md
```

---

## 👤 Autor

Feito por **Igor Amaral** — Estudante de Ciência da Computação

[![GitHub](https://img.shields.io/badge/GitHub-IgorASB-181717?style=flat&logo=github)](https://github.com/IgorASB)
