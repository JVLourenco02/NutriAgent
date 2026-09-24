# 🥗 NutriAgent

O **NutriAgent** é um assistente nutricional inteligente integrado ao Telegram, desenvolvido como projeto acadêmico de Machine Learning e Desenvolvimento de Sistemas. O sistema automatiza o cálculo de parâmetros antropométricos e gera planejamentos alimentares estruturados por porções e gramas, acompanhados de relatórios em PDF.

---

## 🚀 Funcionalidades Principais
* **Coleta Automatizada:** Interação via Telegram (`python-telegram-bot`) para recolher dados físicos e restrições alimentares.
* **Motor Matemático Determinístico:** Cálculos 100% seguros em Python puro (sem alucinações de IA) para:
  * Índice de Massa Corporal (IMC) e classificação.
  * Gasto Energético Basal (TMB / GEB) via fórmula de *Mifflin-St Jeor*.
  * Gasto Energético Total (GET) baseado no nível de atividade física.
  * Metas de macronutrientes (proteínas, carboidratos e gorduras) para *Cutting* ou *Bulking*.
* **Estrutura de Cardápio por Porções:** Organização de refeições por gramas e medidas exatas.
* **Exportação em PDF:** Geração de um laudo físico completo no estilo "bioimpedância" enviado diretamente no chat.
* **Gestão de Histórico:** Acompanhamento da evolução de peso ao longo das semanas.

---

## 🛠️ Arquitetura Tecnológica
O projeto adota uma **arquitetura híbrida**:
* **Front-end / Chat:** Telegram Bot (Python)
* **Banco de Dados:** MySQL (Modelagem relacional para usuários, avaliações, restrições e histórico)
* **Motor Lógico:** Python Puro (Fórmulas científicas e manipulação de dados)
* **Inteligência (LLM):** API do Google Gemini (utilizada estritamente para conversação amigável e formatação de texto)
* **Relatórios:** Bibliotecas de geração de PDF em Python

---

## 📂 Estrutura do Projeto
```text
NutriAgent/
│
├── .env                  # Variáveis de ambiente sensíveis (Tokens e Chaves)
├── requirements.txt      # Dependências do projeto Python
├── database.py           # Conexão e comandos de persistência no MySQL
├── formulas.py           # Algoritmos determinísticos de saúde e nutrição
├── pdf_generator.py      # Lógica de criação do laudo em PDF
└── bot.py                # Máquina de estados principal do Telegram Bot