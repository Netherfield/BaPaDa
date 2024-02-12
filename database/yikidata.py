import requests
import json

def attributes(work_codes:str|list[str]):
    url = "https://query.wikidata.org/sparql"
    if type(work_codes) == list:
        code_values = " wd:".join(work_codes)
        item = """VALUES ?item { wd:""" + code_values + """ }
      ?item rdfs:label ?title ;"""
    elif type(work_codes) == str:
        item = "wd:" + work_codes + " rdfs:label ?title ;"
    query = """SELECT DISTINCT ?title ?authorname ?year ?imgref
      WHERE {
        """ + item + """
                   wdt:P170 ?author ;
                   wdt:P571 ?year ;
                   wdt:P18 ?imgref ; filter(lang(?title) = "en").
      ?author rdfs:label ?authorname ; filter(lang(?authorname) = "en").
}
    """
    r = requests.get(url, params = {'format': 'json', 'query': query})
    return r.json()

