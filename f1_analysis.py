# ============================================================
#  Análise de Dados — Fórmula 1 (1950–2023)
#  Autor: Davi de Moraes Bizerra
#  Dataset: Ergast F1 API via Kaggle (kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020)
#  Ferramentas: Python, Pandas, Matplotlib, Seaborn
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import os

# ── Configuração visual global ──────────────────────────────
sns.set_theme(style="darkgrid", palette="muted")
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.titlesize": 14,
    "axes.titleweight": "bold",
    "axes.labelsize": 11,
    "figure.facecolor": "#0f0f0f",
    "axes.facecolor": "#1a1a2e",
    "axes.labelcolor": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "text.color": "white",
    "grid.color": "#333355",
})

os.makedirs("graficos", exist_ok=True)

# ============================================================
#  1. CARREGAMENTO DOS DADOS
# ============================================================
# Ao baixar o dataset do Kaggle, coloque os CSVs na mesma
# pasta deste script. Os arquivos usados são:
#   - results.csv
#   - drivers.csv
#   - constructors.csv
#   - races.csv

print("📦 Carregando dados...")

results      = pd.read_csv("results.csv")
drivers      = pd.read_csv("drivers.csv")
constructors = pd.read_csv("constructors.csv")
races        = pd.read_csv("races.csv")

print(f"   ✅ {len(results):,} resultados de corrida carregados")
print(f"   ✅ {len(drivers):,} pilotos carregados")
print(f"   ✅ {len(constructors):,} construtoras carregadas")
print(f"   ✅ {len(races):,} corridas carregadas\n")

# ============================================================
#  2. LIMPEZA E PREPARAÇÃO
# ============================================================
print("🧹 Limpando e preparando os dados...")

# Substituir '\N' (valor nulo do dataset) por NaN real
results.replace("\\N", pd.NA, inplace=True)
drivers.replace("\\N", pd.NA, inplace=True)

# Converter colunas numéricas
results["points"] = pd.to_numeric(results["points"], errors="coerce")
results["position"] = pd.to_numeric(results["position"], errors="coerce")

# Criar coluna de nome completo do piloto
drivers["nome_completo"] = drivers["forename"] + " " + drivers["surname"]

# Juntar resultados com pilotos e corridas
df = results.merge(drivers[["driverId", "nome_completo", "nationality"]], on="driverId")
df = df.merge(races[["raceId", "year", "name"]], on="raceId")
df = df.merge(constructors[["constructorId", "name"]], on="constructorId", suffixes=("_corrida", "_equipe"))

print("   ✅ Dados prontos!\n")

# ============================================================
#  3. ANÁLISE 1 — Top 10 pilotos com mais pontos na história
# ============================================================
print("📊 Análise 1: Top 10 pilotos com mais pontos...")

pontos_piloto = (
    df.groupby("nome_completo")["points"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
pontos_piloto.columns = ["Piloto", "Pontos Totais"]

fig, ax = plt.subplots(figsize=(12, 6))
cores = sns.color_palette("rocket", 10)[::-1]
bars = ax.barh(pontos_piloto["Piloto"][::-1], pontos_piloto["Pontos Totais"][::-1], color=cores)

for bar, val in zip(bars, pontos_piloto["Pontos Totais"][::-1]):
    ax.text(bar.get_width() + 20, bar.get_y() + bar.get_height()/2,
            f"{int(val):,}", va="center", fontsize=9, color="white")

ax.set_title("🏆 Top 10 Pilotos com Mais Pontos na História da F1")
ax.set_xlabel("Pontos Totais")
ax.set_ylabel("")
plt.tight_layout()
plt.savefig("graficos/01_top10_pilotos_pontos.png", dpi=150, bbox_inches="tight")
plt.close()
print("   ✅ Gráfico salvo em graficos/01_top10_pilotos_pontos.png\n")

# ============================================================
#  4. ANÁLISE 2 — Vitórias por equipe (Top 10)
# ============================================================
print("📊 Análise 2: Top 10 equipes com mais vitórias...")

vitorias_equipe = (
    df[df["position"] == 1]
    .groupby("name_equipe")
    .size()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
vitorias_equipe.columns = ["Equipe", "Vitórias"]

fig, ax = plt.subplots(figsize=(12, 6))
cores_eq = sns.color_palette("flare", 10)[::-1]
bars2 = ax.barh(vitorias_equipe["Equipe"][::-1], vitorias_equipe["Vitórias"][::-1], color=cores_eq)

for bar, val in zip(bars2, vitorias_equipe["Vitórias"][::-1]):
    ax.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2,
            str(int(val)), va="center", fontsize=9, color="white")

ax.set_title("🏎️ Top 10 Equipes com Mais Vitórias na História da F1")
ax.set_xlabel("Número de Vitórias")
ax.set_ylabel("")
plt.tight_layout()
plt.savefig("graficos/02_top10_equipes_vitorias.png", dpi=150, bbox_inches="tight")
plt.close()
print("   ✅ Gráfico salvo em graficos/02_top10_equipes_vitorias.png\n")

# ============================================================
#  5. ANÁLISE 3 — Evolução de pontos de Hamilton vs Verstappen
# ============================================================
print("📊 Análise 3: Hamilton vs Verstappen — evolução de pontos por temporada...")

pilotos_foco = ["Lewis Hamilton", "Max Verstappen"]
df_foco = df[df["nome_completo"].isin(pilotos_foco)]

evolucao = (
    df_foco.groupby(["year", "nome_completo"])["points"]
    .sum()
    .reset_index()
)
# Focar na era moderna (2007 em diante, quando Hamilton estreou)
evolucao = evolucao[evolucao["year"] >= 2007]

fig, ax = plt.subplots(figsize=(14, 6))
cores_pilotos = {"Lewis Hamilton": "#e8c200", "Max Verstappen": "#1e90ff"}

for piloto, grupo in evolucao.groupby("nome_completo"):
    ax.plot(grupo["year"], grupo["points"], marker="o", linewidth=2.5,
            label=piloto, color=cores_pilotos[piloto])
    # Anotar o último ponto
    ultimo = grupo.iloc[-1]
    ax.annotate(f"{int(ultimo['points'])} pts",
                xy=(ultimo["year"], ultimo["points"]),
                xytext=(8, 4), textcoords="offset points",
                fontsize=8, color=cores_pilotos[piloto])

ax.set_title("⚡ Hamilton vs Verstappen — Pontos por Temporada")
ax.set_xlabel("Temporada")
ax.set_ylabel("Pontos")
ax.legend(facecolor="#1a1a2e", edgecolor="gray")
ax.xaxis.set_major_locator(mticker.MultipleLocator(1))
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graficos/03_hamilton_vs_verstappen.png", dpi=150, bbox_inches="tight")
plt.close()
print("   ✅ Gráfico salvo em graficos/03_hamilton_vs_verstappen.png\n")

# ============================================================
#  6. ANÁLISE 4 — Nacionalidades com mais pilotos na F1
# ============================================================
print("📊 Análise 4: Países com mais pilotos na história da F1...")

nacionalidades = (
    drivers["nationality"]
    .value_counts()
    .head(12)
    .reset_index()
)
nacionalidades.columns = ["País", "Pilotos"]

fig, ax = plt.subplots(figsize=(12, 6))
cores_nac = sns.color_palette("crest", 12)[::-1]
bars3 = ax.barh(nacionalidades["País"][::-1], nacionalidades["Pilotos"][::-1], color=cores_nac)

for bar, val in zip(bars3, nacionalidades["Pilotos"][::-1]):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
            str(int(val)), va="center", fontsize=9, color="white")

ax.set_title("🌍 Países com Mais Pilotos na História da F1")
ax.set_xlabel("Número de Pilotos")
ax.set_ylabel("")
plt.tight_layout()
plt.savefig("graficos/04_nacionalidades_pilotos.png", dpi=150, bbox_inches="tight")
plt.close()
print("   ✅ Gráfico salvo em graficos/04_nacionalidades_pilotos.png\n")

# ============================================================
#  7. RESUMO ESTATÍSTICO
# ============================================================
print("=" * 55)
print("  📋 RESUMO ESTATÍSTICO DO DATASET")
print("=" * 55)
print(f"  Temporadas analisadas : {races['year'].min()} – {races['year'].max()}")
print(f"  Total de corridas     : {races['raceId'].nunique():,}")
print(f"  Total de pilotos      : {drivers['driverId'].nunique():,}")
print(f"  Total de equipes      : {constructors['constructorId'].nunique():,}")
print(f"  País com mais pilotos : {nacionalidades.iloc[0]['País']} ({int(nacionalidades.iloc[0]['Pilotos'])})")
print(f"  Piloto com mais pts   : {pontos_piloto.iloc[0]['Piloto']} ({int(pontos_piloto.iloc[0]['Pontos Totais']):,} pts)")
print(f"  Equipe com mais vit.  : {vitorias_equipe.iloc[0]['Equipe']} ({int(vitorias_equipe.iloc[0]['Vitórias'])} vitórias)")
print("=" * 55)
print("\n✅ Análise concluída! Gráficos salvos na pasta /graficos")
