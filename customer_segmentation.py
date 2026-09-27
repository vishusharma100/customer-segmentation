import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df = pd.read_csv("dataset/customer_data.csv")
features = ["AnnualIncome_k", "SpendingScore", "PurchaseFrequency", "AvgOrderValue"]
X = StandardScaler().fit_transform(df[features])

inertias, silhouettes = [], []
for k in range(2, 9):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = model.fit_predict(X)
    inertias.append(model.inertia_)
    silhouettes.append(silhouette_score(X, labels))

best_k = range(2, 9)[silhouettes.index(max(silhouettes))]
model = KMeans(n_clusters=best_k, random_state=42, n_init=10)
df["Cluster"] = model.fit_predict(X)

profiles = df.groupby("Cluster")[features].mean()
score = ((profiles["AnnualIncome_k"] - profiles["AnnualIncome_k"].mean()) / profiles["AnnualIncome_k"].std()
         + (profiles["SpendingScore"] - profiles["SpendingScore"].mean()) / profiles["SpendingScore"].std())
ordered = score.sort_values().index.tolist()
names = ["Low Value", "Developing", "Potential High Value", "Premium"]
mapping = {cl: names[i] if i < len(names) else f"Segment {i+1}" for i, cl in enumerate(ordered)}
df["Segment"] = df["Cluster"].map(mapping)

df.to_csv("dataset/customer_segments.csv", index=False)

plt.plot(range(2,9), inertias, marker="o")
plt.xlabel("K"); plt.ylabel("Inertia"); plt.title("Elbow Method")
plt.savefig("graphs/elbow_method.png", dpi=180, bbox_inches="tight"); plt.close()

for seg, g in df.groupby("Segment"):
    plt.scatter(g["AnnualIncome_k"], g["SpendingScore"], label=seg, alpha=.7)
plt.xlabel("Annual Income (₹ lakh)"); plt.ylabel("Spending Score")
plt.title("Customer Segmentation"); plt.legend()
plt.savefig("graphs/customer_clusters.png", dpi=180, bbox_inches="tight"); plt.close()

print("Best K:", best_k)
print(df.groupby("Segment")[features].mean().round(2))
