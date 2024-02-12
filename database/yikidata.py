import requests

wikidata_codes = {
    "year" : "P571"
}

def attribute(att:str):
    code = wikidata_codes[att]
    url = "https://query.wikidata.org/sparql"
    query = "SELECT ..."
    r = requests.get(url, params = {'format': 'json', 'query': query})
    return r.json()


SELECT ?title
WHERE {
  ?title wd: wdt:Q3921662
}