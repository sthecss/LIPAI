"""
03 - Árvore de Decisão
Dataset: Iris (scikit-learn)
Saída: arvore_decisao.png
"""

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import DecisionTreeClassifier, plot_tree

# ----- Setup -----
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name='species')

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Árvore não precisa de normalização
scaler_unused = None

# ----- Modelo -----
dt = DecisionTreeClassifier(max_depth=4, random_state=42)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)

print("=== Árvore de Decisão ===")
print(f"Acurácia: {accuracy_score(y_test, y_pred_dt):.4f}")
print(classification_report(y_test, y_pred_dt,
      target_names=iris.target_names))

# Visualização da árvore
plt.figure(figsize=(14, 6))
plot_tree(dt, feature_names=iris.feature_names,
          class_names=iris.target_names, filled=True)
plt.title("Árvore de Decisão (max_depth=4)")
plt.tight_layout()
plt.savefig("arvore_decisao.png", dpi=120)
plt.show()