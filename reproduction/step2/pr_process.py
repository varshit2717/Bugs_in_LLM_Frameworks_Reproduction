# import json
# import pandas as pd

# def remove_illegal_chars(value):
#     if isinstance(value, str):
#         return ''.join(c for c in value if ord(c) > 31 or ord(c) == 9)
#     return value

# with open("pr_llamaindex.json", "r", encoding="utf-8") as json_file:
#     prs = json.load(json_file)

# rows = []
# for pr in prs:
#     row = []
#     row.append(pr['number'])
#     row.append(pr['title'])
#     row.append(pr['html_url'])

#     rows.append(row)

# df = pd.DataFrame(rows, columns=['ID', 'Title', 'Page_URL'])
# df.to_excel('pr_llamaindex.xlsx', index=False, engine='openpyxl')

import json
import pandas as pd


def remove_illegal_chars(value):
    if isinstance(value, str):
        return ''.join(c for c in value if ord(c) > 31 or ord(c) == 9)
    return value


datasets = [
    {
        "framework": "LlamaIndex",
        "input": "pr_llamaindex.json",
        "output": "pr_llamaindex.xlsx"
    },
    {
        "framework": "Haystack",
        "input": "pr_haystack.json",
        "output": "pr_haystack.xlsx"
    },
    {
        "framework": "LangChain",
        "input": "pr_langchain.json",
        "output": "pr_langchain.xlsx"
    }
]


for dataset in datasets:

    print(f"\nProcessing {dataset['framework']}...")

    with open(dataset["input"], "r", encoding="utf-8") as json_file:
        prs = json.load(json_file)

    rows = []

    for pr in prs:

        pr_id = pr["number"]
        title = remove_illegal_chars(pr["title"])
        page_url = pr["html_url"]

        rows.append([
            pr_id,
            title,
            page_url
        ])

    df = pd.DataFrame(
        rows,
        columns=[
            "ID",
            "Title",
            "Page_URL"
        ]
    )

    df.to_excel(
        dataset["output"],
        index=False,
        engine="openpyxl"
    )

    print(f"Rows processed: {len(df)}")
    print(f"Saved to: {dataset['output']}")


print("\nAll datasets processed successfully.")