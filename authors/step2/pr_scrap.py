import requests
import json

url_base = 'https://api.github.com/search/issues?q=type:pr+is:merged+repo:run-llama/llama_index+fix%20in:title+status:success+state:closed&sort=newest&per_page=100&page='
#url_base = 'https://api.github.com/search/issues?q=type:pr+is:merged+repo:deepset-ai/haystack+fix%20in:title+status:success+state:closed&sort=newest&per_page=100&page='
#url_base = 'https://api.github.com/search/issues?q=type:pr+is:merged+repo:langchain-ai/langchain+label:%F0%9F%A4%96:bug+fix%20in:title+status:success+state:closed&sort=newest&per_page=100&page='

prs = []
for page in range(1,10):
    url = url_base+str(page)
    reponse = requests.get(url)
    content = json.loads(reponse.text)
    items = content['items']
    prs = prs + items
    print(page)

#print(len(prs))


with open("pr_llamaindex.json", "w", encoding="utf-8") as json_file:
    json.dump(prs, json_file, indent=4, ensure_ascii=False)
