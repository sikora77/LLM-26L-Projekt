import json
import pandas as pd
from pathlib import Path

NOTEBOOK = "LLM_Projekt.ipynb"

with open(NOTEBOOK, "r", encoding="utf-8") as f:
    nb = json.load(f)

tables = []
table_idx = 0

for cell in nb["cells"]:
    for output in cell.get("outputs", []):
        data = output.get("data", {})

        html_content = data.get("text/html")
        if not html_content:
            continue

        html = "".join(html_content)
        try:
            dfs = pd.read_html(html)
            for df in dfs:
                if {
                    "Step",
                    "Training Loss",
                    "Validation Loss",
                    "Accuracy",
                    "F1",
                }.issubset(df.columns):

                    table_idx += 1

                    csv_name = f"training_metrics_{table_idx}.csv"
                    df.to_csv(csv_name, index=False)

                    tables.append((csv_name, len(df)))

        except Exception as e:
            pass

print("\nExtracted tables:")
for name, rows in tables:
    print(f"{name}: {rows} rows")
