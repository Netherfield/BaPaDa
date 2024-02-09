import requests
import re
import csv
from bs4 import BeautifulSoup

# page = requests.get("https://commons.wikimedia.org/wiki/Mus%C3%A9e_du_Louvre")
# ldiv = soup.find('h3').find_next_sibling("div")
# print(ldiv.a['href'])
# subpage = requests.get(r"https://commons.wikimedia.org/" + ldiv.a['href'])
# soup = BeautifulSoup(subpage.content, "html.parser")
# print(soup.h2)


page = requests.get("https://commons.wikimedia.org/wiki/Category:Paintings_in_the_Mus%C3%A9e_d%27Orsay_by_artist")
soup = BeautifulSoup(page.content, "html.parser")
with open("soupdump.html", "w", encoding='utf-8') as fp:
    fp.write(soup.prettify())


# get all authors and link to their pages
museum_authors = []
by_letter = soup.find_all("div", {"class":"mw-category-group"})
for cat in by_letter:
    authors = cat.find_all("a", href=True)
    for item in authors:
        print(f"link: {item['href']}, text: {item.text}")
        # author, link
        x = (item.text[13:-21], "https://commons.wikimedia.org/" + item['href'])
        museum_authors.append(x)

# for i in range(5):
#     print(museum_authors[i])
#     print(museum_authors[-i])

fp = open("test.csv", "w", encoding="utf-16", newline="")
writer =csv.writer(fp)
writer.writerow(["author","title","year","link"])
for author, author_page in museum_authors:
    print(author)
    subpage = requests.get(author_page)
    soup = BeautifulSoup(subpage.content, "html.parser")
    gallery = soup.find_all("ul", {"class":"gallery mw-gallery-traditional"})
    for sub_gallery in gallery:
        works = sub_gallery.find_all("li", {"class":"gallerybox"})
        for work in works:
            img = work.find("a", {"class":"mw-file-description"})['href']
            # description = work.find("a", {"class":"galleryfilename galleryfilename-truncate"})
            link = "https://commons.wikimedia.org/" + img
            print(img)
            p_year = re.compile(r"(?<=[ .-_(])[0-9]{4}(?=[ .-_)])")
            year = p_year.search(img)


            """
            MOVE TO A SECTION WHERE IT DOESN'T TRY IT FOR EVERY PAINTING CAUSE WE ARE ONLY SELECTING A HANDFUL
            """
            work_page = requests.get(link)
            print(link)
            work_soup = BeautifulSoup(work_page.content, "html.parser")
            with open("authordump.html", "w", encoding='utf-8') as fp:
                fp.write(soup.prettify())
            title = work_soup.find("div", {"style":"display:inline-block"})
            if title is not None:
                title = title.i.text
            print(title)



            # p_title = re.compile(r"(?<=File:).*(?=.jpg)")
            # title = p_title.search(img)
            if year is not None and title is not None:
                year = year.group(0)
                print(year, title)
                line = [author,title,year,link]
                writer.writerow(line)
            # print(description.text)
    break
fp.close()