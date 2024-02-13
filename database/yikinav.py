
import time
import requests
from bs4 import BeautifulSoup


import yikidata

def get_museum(museum_link:str):
    page = requests.get(museum_link)
    soup = BeautifulSoup(page.content, "html.parser")

    # dump html
    with open("tmp/soupdump.html", "w", encoding='utf-8') as fp:
        fp.write(soup.prettify())
    return soup

def get_authors(soup:BeautifulSoup) -> list[str]:
    "Gets a list of authors and the link to their page"
    museum_authors = []
    subcategories = soup.find_all("div", {"class":"mw-category-group"})
    for cat in subcategories:
        authors = cat.find_all("a", href=True)
        for item in authors:
            print(f"link: {item['href']}, text: {item.text}")
            # (author, link)
            x = (item.text[13:-21], "https://commons.wikimedia.org/" + item['href'])
            museum_authors.append(x)
    return museum_authors


def author_navigator(author_page:str):
    "Extract a list of works from the author's page"
    subpage = requests.get(author_page)
    author_soup = BeautifulSoup(subpage.content, "html.parser")
    return author_soup.find("ul", {"class":"gallery mw-gallery-traditional"})

def get_works(gallery:BeautifulSoup):
    "Navigates the page for works, getting the link and extracts a list"
    author_works = []
    works = gallery.find_all("li", {"class":"gallerybox"})
    for work in works:
        img = work.find("a", {"class":"mw-file-description"})['href']
        author_works += ["https://commons.wikimedia.org/" + img]
    return author_works

def wikidata_parser(work_codes:str):
    start = time.perf_counter()
    work_data = yikidata.attributes(work_codes)
    results:list[dict] = work_data['results']['bindings']
    works_info = []
    for result in results:
        author = result['authorname']['value']
        title = result['title']['value']
        year = result['year']['value'][:4]
        link = result['imgref']['value']
        works_info += [[author, title, year, link]]
    stop = time.perf_counter()
    print(f"Query time for {author} was {stop - start:0.4f} seconds")
    return works_info
    

def code_extractor(work_link:str) -> list[str]:
    work_page = requests.get(work_link)
    work_soup = BeautifulSoup(work_page.content, "html.parser")
    auth_section = work_soup.find("td", {"id":"fileinfotpl_art_authority"})
    if auth_section is not None:
        wikidata_label = auth_section.find_next_sibling("td").find("span", {"typeof":"mw:File"})
        return wikidata_label.a['title'][9:]
        
def work_extractor(work_codes):
    if work_codes:
        return wikidata_parser(work_codes)
    else:
        raise Exception("Empty list")