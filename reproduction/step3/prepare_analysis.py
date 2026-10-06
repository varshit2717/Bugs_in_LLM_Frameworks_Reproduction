import pandas as pd

INPUT_FILE = "labeling_dataset.xlsx"
OUTPUT_FILE = "analysis_data.csv"

ROUNDS = ["Round1", "Round2", "Round3", "Round4"]

frames = []

for round_name in ROUNDS:

    df = pd.read_excel(
        INPUT_FILE,
        sheet_name=round_name
    )

    print(f"{round_name}: {df.shape[0]} rows")

    df["Round"] = round_name

    frames.append(df)

# Combine all rounds
combined = pd.concat(
    frames,
    ignore_index=True
)

print("\nTotal rows before filtering:", len(combined))

# Keep only actual bugs
analysis = combined[
    combined["Final_Bug_Status"]
    .astype(str)
    .str.strip()
    .str.lower()
    .eq("include")
].copy()

print("Included bugs:", len(analysis))

# Create simpler analysis column names
analysis["Root_Cause"] = analysis["Final_Root_Cause"]
analysis["Symptom"] = analysis["Final_Symptom"]
analysis["Component"] = analysis["Final_Component"]
analysis["Notes"] = analysis["Final_Notes"]

# Keep useful analysis columns
analysis = analysis[
    [
        "Round",
        "Framework",
        "ID",
        "Title",
        "Page_URL",
        "Root_Cause",
        "Symptom",
        "Component",
        "Notes",
    ]
]

# Remove rows missing taxonomy labels
analysis = analysis.dropna(
    subset=[
        "Root_Cause",
        "Symptom",
        "Component"
    ]
)

# Clean whitespace
for column in [
    "Framework",
    "Root_Cause",
    "Symptom",
    "Component"
]:
    analysis[column] = (
        analysis[column]
        .astype(str)
        .str.strip()
    )

# Save
analysis.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nFinal analysis shape:", analysis.shape)

print("\n===== ROUNDS =====")
print(analysis["Round"].value_counts())

print("\n===== FRAMEWORKS =====")
print(analysis["Framework"].value_counts())

print("\n===== ROOT CAUSES =====")
print(analysis["Root_Cause"].value_counts())

print("\n===== SYMPTOMS =====")
print(analysis["Symptom"].value_counts())

print("\n===== COMPONENTS =====")
print(analysis["Component"].value_counts())

print("\nSaved:", OUTPUT_FILE)