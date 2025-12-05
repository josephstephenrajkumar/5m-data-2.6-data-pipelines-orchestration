import os
import pandas as pd
import re

# -------------------------------------------------------
# CONFIG
# -------------------------------------------------------
INPUT_DIR = "kaggle_dataset"
OUTPUT_DIR = "cleaned_kaggle_dataset"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# BigQuery-compatible column renamer
def clean_column(col):
    """
    Cleans a column name to be BigQuery compatible:
    - Lowercase
    - Replace spaces and hyphens with underscores
    - Remove invalid chars
    - Ensure starts with letter or underscore
    """
    original_col = col

    # Lowercase for consistency
    col = col.lower()

    # Replace spaces, hyphens with underscore
    col = re.sub(r"[ -]+", "_", col)

    # Remove all invalid characters
    col = re.sub(r"[^a-zA-Z0-9_]", "", col)

    # BigQuery requires column not start with number
    if re.match(r"^[0-9]", col):
        col = "_" + col

    return col


# -------------------------------------------------------
# PROCESS FILES
# -------------------------------------------------------

def process_csv_file(file_path):
    df = pd.read_csv(file_path)

    print(f"\nProcessing: {file_path}")

    new_cols = {}
    for col in df.columns:
        cleaned = clean_column(col)
        if cleaned != col:
            new_cols[col] = cleaned

    if new_cols:
        print("  ❗ Columns renamed:")
        for old, new in new_cols.items():
            print(f"     - '{old}' → '{new}'")
        df.rename(columns=new_cols, inplace=True)
    else:
        print("  ✓ Columns already valid.")

    # Save cleaned file
    filename = os.path.basename(file_path)
    output_path = os.path.join(OUTPUT_DIR, filename)
    df.to_csv(output_path, index=False)

    print(f"  ✔ Saved cleaned dataset to: {output_path}")

# -------------------------------------------------------
# EXECUTE
# -------------------------------------------------------

csv_files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".csv")]

print("Found CSV files:", csv_files)

for csv in csv_files:
    process_csv_file(os.path.join(INPUT_DIR, csv))

print("\n🎉 Completed! Cleaned files are in:", OUTPUT_DIR)
