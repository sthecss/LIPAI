import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import os
BASE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE, "../datasets/classification_results_trial_0001.csv"))


df["correto"] = df["real_class"] == df["predicted_class"]


fp = df[(df["real_class"] == "benign") & (df["predicted_class"] == "malign")]
fn = df[(df["real_class"] == "malign") & (df["predicted_class"] == "benign")]


#
# FIGURA 1 — Contagens por classe real e predita
#
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
fig.suptitle("Contagem de Classes", fontsize=14)

# Grf 1 — contagem por real_class
contagem_real = df["real_class"].value_counts()
ax1.bar(contagem_real.index, contagem_real.values, color=["steelblue", "tomato"])
ax1.set_title("Contagem por Classe Real")
ax1.set_xlabel("Classe")
ax1.set_ylabel("Contagem")
for i, v in enumerate(contagem_real.values):
    ax1.text(i, v + 0.5, str(v), ha="center", fontsize=11)

# Grf 2 — contagem por predicted_class
contagem_pred = df["predicted_class"].value_counts()
ax2.bar(contagem_pred.index, contagem_pred.values, color=["steelblue", "tomato"])
ax2.set_title("Contagem por Classe Predita")
ax2.set_xlabel("Classe")
ax2.set_ylabel("Contagem")
for i, v in enumerate(contagem_pred.values):
    ax2.text(i, v + 0.5, str(v), ha="center", fontsize=11)

plt.tight_layout()
plt.savefig("fig1_contagens.png", dpi=150)
plt.show()


#
# FIGURA 2 — Histogramas de probabilidade
#
fig, (ax3, ax4) = plt.subplots(1, 2, figsize=(10, 4))
fig.suptitle("Distribuição de Probabilidades", fontsize=14)

ax3.hist(df["prob_benign"], bins=20, color="steelblue", edgecolor="white")
ax3.set_title("Histograma — prob_benign")
ax3.set_xlabel("Probabilidade")
ax3.set_ylabel("Frequência")

ax4.hist(df["prob_malign"], bins=20, color="tomato", edgecolor="white")
ax4.set_title("Histograma — prob_malign")
ax4.set_xlabel("Probabilidade")
ax4.set_ylabel("Frequência")

plt.tight_layout()
plt.savefig("fig2_histogramas.png", dpi=150)
plt.show()


#
# FIGURA 3 — Scatter: prob_benign x prob_malign (acerto vs erro)
#
fig, ax5 = plt.subplots(figsize=(7, 5))

acertos = df[df["correto"]]
erros   = df[~df["correto"]]

ax5.scatter(acertos["prob_benign"], acertos["prob_malign"],
            color="steelblue", label="Acerto", alpha=0.7, edgecolors="white")
ax5.scatter(erros["prob_benign"],   erros["prob_malign"],
            color="tomato",    label="Erro",   alpha=0.9, edgecolors="white", marker="X", s=80)

ax5.set_title("Scatter — prob_benign vs prob_malign")
ax5.set_xlabel("prob_benign")
ax5.set_ylabel("prob_malign")
ax5.legend()
ax5.plot([0, 1], [1, 0], color="gray", linestyle="--", lw=0.8, label="fronteira 0.5")

plt.tight_layout()
plt.savefig("fig3_scatter.png", dpi=150)
plt.show()


#
# FIGURA 4 — FP vs FN: qual erro é mais comum?
#
fig, ax6 = plt.subplots(figsize=(5, 4))

erros_tipo = {"Falso Positivo\n(FP)", "Falso Negativo\n(FN)"}
contagens  = [len(fp), len(fn)]
labels     = ["Falso Positivo\n(FP)\nBenign → Malign", "Falso Negativo\n(FN)\nMalign → Benign"]
cores      = ["orange", "crimson"]

bars = ax6.bar(labels, contagens, color=cores, edgecolor="white")
ax6.set_title("Erros de Classificação: FP vs FN")
ax6.set_ylabel("Quantidade")

for bar, v in zip(bars, contagens):
    ax6.text(bar.get_x() + bar.get_width() / 2, v + 0.2, str(v), ha="center", fontsize=12)


plt.tight_layout()
plt.savefig("fig4_fp_fn.png", dpi=150)
plt.show()


print(f"\nTotal de amostras : {len(df)}")
print(f"Acertos           : {df['correto'].sum()}")
print(f"Erros             : {(~df['correto']).sum()}")
print(f"Falsos Positivos  : {len(fp)}  (benign predito como malign)")
print(f"Falsos Negativos  : {len(fn)}  (malign predito como benign)")
print("\n--- Contexto médico ---")
print("FN é mais preocupante: um paciente com tumor maligno é")
print("classificado como benigno e pode não receber tratamento a tempo.")