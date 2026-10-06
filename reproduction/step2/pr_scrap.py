# import requests
# import json

# url_base = 'https://api.github.com/search/issues?q=type:pr+is:merged+repo:run-llama/llama_index+fix%20in:title+status:success+state:closed&sort=newest&per_page=100&page='
# #url_base = 'https://api.github.com/search/issues?q=type:pr+is:merged+repo:deepset-ai/haystack+fix%20in:title+status:success+state:closed&sort=newest&per_page=100&page='
# #url_base = 'https://api.github.com/search/issues?q=type:pr+is:merged+repo:langchain-ai/langchain+label:%F0%9F%A4%96:bug+fix%20in:title+status:success+state:closed&sort=newest&per_page=100&page='

# prs = []
# for page in range(1,10):
#     url = url_base+str(page)
#     response = requests.get(url)
#     content = json.loads(response.text)
#     items = content['items']
#     prs = prs + items
#     print(page)

# #print(len(prs))


# with open("pr_llamaindex.json", "w", encoding="utf-8") as json_file:
#     json.dump(prs, json_file, indent=4, ensure_ascii=False)

import requests
import json
import time

url_base = (
    "https://api.github.com/search/issues"
    "?q=type:pr+is:merged+repo:langchain-ai/langchain"
    "+label:bug"
    "+fix%20in:title"
    "+status:success"
    "+state:closed"
    "&sort=newest"
    "&per_page=100"
    "&page="
)

output_file = "pr_langchain.json"

prs = []

for page in range(1, 11):

    url = url_base + str(page)

    response = requests.get(url)

    print(
        f"Page {page} | "
        f"HTTP {response.status_code} | "
        f"Rate remaining: {response.headers.get('x-ratelimit-remaining')}"
    )

    if response.status_code != 200:
        print("GitHub API error:")
        print(response.text)
        break

    content = response.json()

    if page == 1:
        print("GitHub total_count:", content.get("total_count"))
        print("Incomplete results:", content.get("incomplete_results"))

    items = content.get("items", [])

    if not items:
        print("No more results.")
        break

    prs.extend(items)

    print("Items this page:", len(items))
    print("Collected so far:", len(prs))

    time.sleep(1)


with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(prs, json_file, indent=4, ensure_ascii=False)


print("\nCollection finished")
print("Total LangChain PRs collected:", len(prs))
print("Saved to:", output_file)