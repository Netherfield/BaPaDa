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

import csv
import time

import database.yikinav as yikinav



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
        
    fp = open("data/museum2.csv", "w", encoding="utf-16", newline="")
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
                print("No codes for this author")
        if i == 2:
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

