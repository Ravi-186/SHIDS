import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/KDDTrain+.txt", header=None)

# Select important columns
df = df[[0, 4, 5, 41]]

# Rename columns
df.columns = ["duration", "src_bytes", "dst_bytes", "label"]

# Convert labels
df["label"] = df["label"].apply(lambda x: "normal" if x == "normal" else "attack")

# Save new dataset
df.to_csv("data/raw/data.csv", index=False)

print("Dataset converted successfully!")