"""
07 - Comparação de Desempenho entre Algoritmos
Dataset: Iris (scikit-learn)
Saídas: comparacao_algoritmos.png, matrizes_confusao.png
"""

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (accuracy_score, confusion_matrix,
                             ConfusionMatrixDisplay)
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# ----- Setup -----
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name='species')

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc  = scaler.transform(X_test)

# ----- Treinar todos os modelos -----
lr  = LogisticRegression(max_iter=200, random_state=42).fit(X_train_sc, y_train)
dt  = DecisionTreeClassifier(max_depth=4, random_state=42).fit(X_train, y_train)
rf  = RandomForestClassifier(n_estimators=100, random_state=42).fit(X_train, y_train)
svm = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42).fit(X_train_sc, y_train)
knn = KNeighborsClassifier(n_neighbors=5).fit(X_train_sc, y_train)

y_pred_lr  = lr.predict(X_test_sc)
y_pred_dt  = dt.predict(X_test)
y_pred_rf  = rf.predict(X_test)
y_pred_svm = svm.predict(X_test_sc)
y_pred_knn = knn.predict(X_test_sc)

# ----- Tabela de comparação -----
modelos = {
    'Regressão Logística' : accuracy_score(y_test, y_pred_lr),
    'Árvore de Decisão'   : accuracy_score(y_test, y_pred_dt),
    'Random Forest'       : accuracy_score(y_test, y_pred_rf),
    'SVM'                 : accuracy_score(y_test, y_pred_svm),
    'kNN'                 : accuracy_score(y_test, y_pred_knn),
}

df_result = pd.DataFrame(modelos.items(), columns=['Algoritmo', 'Acurácia'])
df_result = df_result.sort_values('Acurácia', ascending=False)
print(df_result.to_string(index=False))

# ----- Gráfico de barras -----
plt.figure(figsize=(9, 5))
plt.barh(df_result['Algoritmo'], df_result['Acurácia'],
         color='steelblue', edgecolor='white')
plt.xlim(0.9, 1.01)
plt.xlabel('Acurácia')
plt.title('Comparação de Algoritmos — Dataset Iris')
plt.tight_layout()
plt.savefig("comparacao_algoritmos.png", dpi=120)
plt.show()

# ----- Matrizes de Confusão lado a lado -----
fig, axes = plt.subplots(1, 5, figsize=(22, 4))
pares = [
    ('Log. Reg.',    y_pred_lr),
    ('Dec. Tree',    y_pred_dt),
    ('Rand. Forest', y_pred_rf),
    ('SVM',          y_pred_svm),
    ('kNN',          y_pred_knn),
]
for ax, (nome, pred) in zip(axes, pares):
    cm = confusion_matrix(y_test, pred)
    ConfusionMatrixDisplay(cm, display_labels=iris.target_names).plot(
        ax=ax, colorbar=False)
    ax.set_title(nome)
plt.tight_layout()
plt.savefig("matrizes_confusao.png", dpi=120)
plt.show()