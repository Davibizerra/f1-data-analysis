# 🏎️ Análise de Dados — Fórmula 1 (1950–2023)

> Projeto de análise exploratória de dados utilizando Python, Pandas, Matplotlib e Seaborn sobre o histórico completo da Fórmula 1.

---

## 📌 Sobre o Projeto

Este projeto tem como objetivo explorar o dataset histórico da Fórmula 1 para extrair insights sobre pilotos, equipes e temporadas. Foram aplicadas técnicas de **limpeza de dados, análise exploratória (EDA) e visualização de dados** para responder perguntas reais sobre o esporte.

---

## ❓ Perguntas que o projeto responde

- Quais são os 10 pilotos com mais pontos na história da F1?
- Quais equipes dominaram o esporte em número de vitórias?
- Como evoluiu a rivalidade entre **Lewis Hamilton e Max Verstappen** ao longo das temporadas?
- Quais países produziram mais pilotos na história da categoria?

---

## 📊 Visualizações Geradas

| Gráfico | Descrição |
|--------|-----------|
| `01_top10_pilotos_pontos.png` | Ranking dos pilotos com mais pontos acumulados |
| `02_top10_equipes_vitorias.png` | Equipes com mais vitórias na história |
| `03_hamilton_vs_verstappen.png` | Evolução de pontos por temporada — Hamilton vs Verstappen |
| `04_nacionalidades_pilotos.png` | Países com mais pilotos na história da F1 |

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Pandas** — manipulação e limpeza de dados
- **Matplotlib** — visualizações personalizadas
- **Seaborn** — estilização de gráficos

---

## 📁 Estrutura do Projeto

```
f1-data-analysis/
│
├── f1_analysis.py        # Script principal de análise
├── requirements.txt      # Dependências do projeto
├── README.md             # Este arquivo
│
├── graficos/             # Gráficos gerados automaticamente
│   ├── 01_top10_pilotos_pontos.png
│   ├── 02_top10_equipes_vitorias.png
│   ├── 03_hamilton_vs_verstappen.png
│   └── 04_nacionalidades_pilotos.png
│
└── data/                 # CSVs do dataset (baixar do Kaggle)
    ├── results.csv
    ├── drivers.csv
    ├── constructors.csv
    └── races.csv
```

---

## ▶️ Como Executar

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/f1-data-analysis.git
cd f1-data-analysis
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Baixe o dataset**

Acesse o link abaixo e faça o download dos CSVs:  
🔗 [Formula 1 World Championship — Kaggle](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020)

Coloque os arquivos `results.csv`, `drivers.csv`, `constructors.csv` e `races.csv` na pasta raiz do projeto.

**4. Execute a análise**
```bash
python f1_analysis.py
```

Os gráficos serão salvos automaticamente na pasta `/graficos`.

---

## 🔍 Principais Insights

- **Lewis Hamilton** lidera o ranking histórico de pontos, reflexo de sua longevidade e consistência na era híbrida da F1.
- **Ferrari e McLaren** dominam o ranking de vitórias por equipe ao longo de toda a história do esporte.
- A rivalidade **Hamilton vs Verstappen** ficou mais acirrada a partir de 2021, com Verstappen assumindo protagonismo crescente.
- **Grã-Bretanha, EUA e Itália** são os países com mais pilotos representados na história da categoria.

---

## 👤 Autor

**Davi de Moraes Bizerra**  
📧 davibizerra02@gmail.com  
🎓 Sistemas de Informação — Faculdade Impacta  
🔗 [LinkedIn](https://linkedin.com/in/seu-perfil) | [GitHub](https://github.com/seu-usuario)

---

## 📄 Licença

Este projeto é de uso livre para fins educacionais.  
Dataset original disponível em: [Kaggle — Ergast F1](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020)
