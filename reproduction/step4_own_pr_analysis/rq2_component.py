import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("analysis_data.csv")

# -----------------------------
# RAW COUNTS
# -----------------------------
raw = pd.crosstab(
    df["Symptom"],
    df["Component"]
)

raw["Total"] = raw.sum(axis=1)
raw = raw.sort_index()

print("\n===== SYMPTOM × COMPONENT — RAW COUNTS =====")
print(raw)

raw.to_csv("rq2_symptom_component_raw.csv")

# -----------------------------
# NORMALIZED %
# Normalize within each component
# -----------------------------
component_cols = [c for c in raw.columns if c != "Total"]

normalized = (
    raw[component_cols]
    .div(raw[component_cols].sum(axis=0), axis=1)
    * 100
)

normalized["Total"] = (
    raw["Total"] / raw["Total"].sum() * 100
)

normalized = normalized.round(2)

print("\n===== SYMPTOM × COMPONENT — NORMALIZED (%) =====")
print(normalized)

normalized.to_csv("rq2_symptom_component_normalized.csv")

# -----------------------------
# RAW HEATMAP
# -----------------------------
fig, ax = plt.subplots(figsize=(11, 6))

ax.imshow(raw.values, aspect="auto")

ax.set_xticks(range(len(raw.columns)))
ax.set_xticklabels(raw.columns, rotation=20, ha="right")

ax.set_yticks(range(len(raw.index)))
ax.set_yticklabels(raw.index)

ax.set_title("Symptom Distribution Across Components — Raw Counts")
ax.set_xlabel("Component")
ax.set_ylabel("Symptom")

for i in range(len(raw.index)):
    for j in range(len(raw.columns)):
        ax.text(
            j,
            i,
            raw.iloc[i, j],
            ha="center",
            va="center"
        )

plt.tight_layout()

plt.savefig(
    "rq2_symptom_component_raw.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# -----------------------------
# NORMALIZED HEATMAP
# -----------------------------
fig, ax = plt.subplots(figsize=(11, 6))

ax.imshow(normalized.values, aspect="auto")

ax.set_xticks(range(len(normalized.columns)))
ax.set_xticklabels(normalized.columns, rotation=20, ha="right")

ax.set_yticks(range(len(normalized.index)))
ax.set_yticklabels(normalized.index)

ax.set_title("Symptom Distribution Across Components — Normalized (%)")
ax.set_xlabel("Component")
ax.set_ylabel("Symptom")

for i in range(len(normalized.index)):
    for j in range(len(normalized.columns)):
        ax.text(
            j,
            i,
            f"{normalized.iloc[i, j]:.1f}",
            ha="center",
            va="center"
        )

plt.tight_layout()

plt.savefig(
    "rq2_symptom_component_normalized.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nGenerated:")
print("rq2_symptom_component_raw.csv")
print("rq2_symptom_component_normalized.csv")
print("rq2_symptom_component_raw.png")
print("rq2_symptom_component_normalized.png")
