# Copyright (c) 2023 Jules aka Netherfield
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import requests

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

