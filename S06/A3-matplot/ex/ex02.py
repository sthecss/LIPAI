import os
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use("default")


BASE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE, "../datasets/metrics.csv"))
epochs = range(1, len(df) + 1)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

#
# Accuracy
#
ax1.plot(epochs, df["train_acc"], label="train")
ax1.plot(epochs, df["val_acc"],   label="valid")
ax1.set_title("model accuracy")
ax1.set_xlabel("epoch")
ax1.set_ylabel("accuracy")
ax1.legend(loc="lower right")

#
# Loss
#
ax2.plot(epochs, df["train_loss"], label="train")
ax2.plot(epochs, df["val_loss"],   label="valid")
ax2.set_title("model loss")
ax2.set_xlabel("epoch")
ax2.set_ylabel("loss")
ax2.legend(loc="upper right")

plt.tight_layout()
plt.show()