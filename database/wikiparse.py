
import re
import csv

import wikinav



def wikiscrape() -> None:
    """
    Connects to Museum author page and connects to all the author's pages,
    opens all of their work links on wikimedia commons and extracts
    as many works info as possible
    """
    museum_link = "https://commons.wikimedia.org/wiki/Category:Paintings_in_the_Mus%C3%A9e_d%27Orsay_by_artist"
    
    museum_s = wikinav.get_museum(museum_link)
    # dump authors
    museum_authors:list[str] = wikinav.get_authors(museum_s)
    with open("tmp/authordump.txt", "w", encoding='utf-8') as fp:
        for author, link in museum_authors:
            fp.write(author + "   " + link + "\n")
        
    fp = open("test.csv", "w", encoding="utf-16", newline="")
    writer =csv.writer(fp)
    writer.writerow(["author","title","year","link"])

    for author, author_page in museum_authors:
        gallery = wikinav.author_navigator(author_page)
        author_works:list[str] = wikinav.get_works(gallery)
        for work_link in author_works:
            info:list[str] = wikinav.work_extractor(work_link)



if __name__ == "__main__":
    wikiscrape()

