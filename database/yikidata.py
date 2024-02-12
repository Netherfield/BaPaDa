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

"""
SELECT ?title
WHERE {
  ?title wd: wdt:Q3921662
}
"""


"""
SELECT DISTINCT ?painting ?paintingLabel ?artist ?artistLabel ?image ?creationDate ?artistBirthDate ?artistDeathDate ?movement ?movementLabel
WHERE {
  ?painting wdt:P31 wd:Q3305213;    # Quadro
            wdt:P170 ?artist;        # Artista
            wdt:P571 ?creationDate;  # Data di creazione
            wdt:P18 ?image.          # Immagine
            
  OPTIONAL { ?artist wdt:P569 ?artistBirthDate. }  # Data di nascita dell'artista
  OPTIONAL { ?artist wdt:P570 ?artistDeathDate. }  # Data di morte dell'artista
  OPTIONAL { ?painting wdt:P135 ?movement. }      # Movimento artistico
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
LIMIT 500

"""