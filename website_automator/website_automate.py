import pandas as pd
import webbrowser
import sys

URLS = {
    "work" : ["www.google.ca", "www.slack.com"],
    "personal" : ["www.youtube.com", "www.netflix.com"]
}

def open_webpages(urls):
    for url in urls:
        webbrowser.open_new_tab(url)

if __name__ == "__main__": # run only directly from terminal
    set_name = sys.argv[1] # sys.argv() list of all command line arguments
    urls = URLS[set_name]
    open_webpages(urls)
