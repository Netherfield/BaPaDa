import csv
import time

import yikinav



def wikiscrape() -> None:
    """
    Connects to Museum author page and connects to all the author's pages,
    opens all of their work links on wikimedia commons and extracts
    as many works info as possible
    """
    museum_link = "https://commons.wikimedia.org/wiki/Category:Paintings_in_the_Mus%C3%A9e_d%27Orsay_by_artist"
    
    museum_s = yikinav.get_museum(museum_link)
    # dump authors
    museum_authors:list[str] = yikinav.get_authors(museum_s)
    with open("tmp/authordump.txt", "w", encoding='utf-8') as fp:
        for author, link in museum_authors:
            fp.write(author + "   " + link + "\n")
        
    fp = open("data/museum.csv", "w", encoding="utf-16", newline="")
    print("Starting csv compilation")
    
    writer =csv.writer(fp)
    writer.writerow(["author","title","year","link"])
    print("Starting parse")
    i = 0
    for author, author_page in museum_authors:
        print("Getting info for: ", author)
        gallery = yikinav.author_navigator(author_page)
        if gallery:
            author_works:list[str] = yikinav.get_works(gallery)
            work_codes = []
            for work_link in author_works:
                code = yikinav.code_extractor(work_link)
                if code is not None:
                    print("Found wikidata code: ", code)
                    work_codes += [code]
            if work_codes:
                print("Got the following codes")
                print(work_codes)
            try:
                print("Trying for work info")
                works_info = yikinav.work_extractor(work_codes)
                writer.writerows(works_info)
            except Exception as e:
                print(e)
                print("Non codes for this author")
        if i == 100:
            break
        i += 1
    print("csv created at: database/data/museum.csv")
    print("finished")
    
    fp.close()

if __name__ == "__main__":
    start = time.perf_counter()
    wikiscrape()
    stop = time.perf_counter()
    print(f"Total time: {stop - start:f0.4} seconds")

