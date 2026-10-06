import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("analysis_data.csv")

# ---------------------------------
# RAW ROOT CAUSE × SYMPTOM TABLE
# ---------------------------------

raw = pd.crosstab(
    df["Root_Cause"],
    df["Symptom"]
)

raw["Total"] = raw.sum(axis=1)
raw = raw.sort_index()

print("\n===== ROOT CAUSE × SYMPTOM — RAW COUNTS =====")
print(raw)

raw.to_csv("rq3_rootcause_symptom_raw.csv")


# ---------------------------------
# NORMALIZED BY ROOT CAUSE
# ---------------------------------

symptom_cols = [c for c in raw.columns if c != "Total"]

normalized = (
    raw[symptom_cols]
    .div(raw["Total"], axis=0)
    * 100
)

normalized["Total"] = 100.0

normalized = normalized.round(2)

print("\n===== ROOT CAUSE × SYMPTOM — NORMALIZED (%) =====")
print(normalized)

normalized.to_csv(
    "rq3_rootcause_symptom_normalized.csv"
)


# ---------------------------------
# RAW HEATMAP
# ---------------------------------

fig, ax = plt.subplots(figsize=(11, 7))

ax.imshow(raw.values, aspect="auto")

ax.set_xticks(range(len(raw.columns)))
ax.set_xticklabels(
    raw.columns,
    rotation=30,
    ha="right"
)

ax.set_yticks(range(len(raw.index)))
ax.set_yticklabels(raw.index)

ax.set_title(
    "Root Cause–Symptom Relationship — Raw Counts"
)

ax.set_xlabel("Symptom")
ax.set_ylabel("Root Cause")

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
    "rq3_rootcause_symptom_raw.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ---------------------------------
# NORMALIZED HEATMAP
# ---------------------------------

fig, ax = plt.subplots(figsize=(11, 7))

ax.imshow(normalized.values, aspect="auto")

ax.set_xticks(range(len(normalized.columns)))
ax.set_xticklabels(
    normalized.columns,
    rotation=30,
    ha="right"
)

ax.set_yticks(range(len(normalized.index)))
ax.set_yticklabels(normalized.index)

ax.set_title(
    "Root Cause–Symptom Relationship — Normalized (%)"
)

ax.set_xlabel("Symptom")
ax.set_ylabel("Root Cause")

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
    "rq3_rootcause_symptom_normalized.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ---------------------------------
# SANKEYMATIC TEXT
# ---------------------------------

with open(
    "rq3_sankeymatic.txt",
    "w",
    encoding="utf-8"
) as f:

    for root_cause in raw.index:

        for symptom in symptom_cols:

            count = raw.loc[root_cause, symptom]

            if count > 0:
                f.write(
                    f"{root_cause} [{count}] {symptom}\n"
                )

print("\nGenerated:")
print("rq3_rootcause_symptom_raw.csv")
print("rq3_rootcause_symptom_normalized.csv")
print("rq3_rootcause_symptom_raw.png")
print("rq3_rootcause_symptom_normalized.png")
print("rq3_sankeymatic.txt")
