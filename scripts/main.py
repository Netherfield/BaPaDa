# Copyright (c) 2023 Jules aka Netherfield

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import argparse

import utils
from utils.core import dbcheck

import flaskr
from flaskr.db_manager import manager


from database.yikiparse import wikiscrape

def clean_env():
    try:
        # clean up environment at the end of execution
        print("Removing temporary files")
        os.system("pyclean .")
        print("Removed temporary files")
    except:
        print("pyclean . \nFailed execution. Exiting...")

# start app
def main():
    """
    Parses arguments
        bapada [-h] [--scrape] [--no-db] [--test-db] [--update] [--link LINK] [--host ip_address] ...
    Currently only --scrape and -h are implemented
    """
    # bapada [-h] [--scrape] [--no-db] [--test-db] [--update] [--link] ...
    # for now just --scrape
    parser = argparse.ArgumentParser(
                        prog="BaPaDa",
                        description="Museum Webapp",
                        epilog="Thank you fro using BaPaDa")
    # store_true means that if --scrape then scrape=True, if not included then scrape=False
    parser.add_argument("--scrape", "-s", dest="scrape", action="store_true",
                        help="scrape data from [--link] (this can take a while)")
    parser.add_argument("--server", dest="server", action="store_true",
                        help="Establish connection to sql server at host [--host]")
    args = parser.parse_args()
    
    if args.scrape:
        print("""You are trying to scrape the database again.
              It would take a lot of time so please reconsider.
              The flag is fake anyway.""")
    
    # if args.db:
    #   ...create db or don't idk
    if dbcheck:
        ...
    else:
        manager(server=args.server)

    clean_env()
    
# launch flask
# wait
# launch chrome/ff/edge
if __name__ == "__main__":
    main()



