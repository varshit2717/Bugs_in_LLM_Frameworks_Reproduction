import json
import pandas as pd

def remove_illegal_chars(value):
    if isinstance(value, str):
        return ''.join(c for c in value if ord(c) > 31 or ord(c) == 9)
    return value

with open("pr_llamaindex.json", "r", encoding="utf-8") as json_file:
    prs = json.load(json_file)

rows = []
for pr in prs:
    row = []
    row.append(pr['number'])
    row.append(pr['title'])
    row.append(pr['html_url'])

    rows.append(row)

df = pd.DataFrame(rows, columns=['ID', 'Title', 'Page_URL'])
df.to_excel('pr_llamaindex.xlsx', index=False, engine='openpyxl')