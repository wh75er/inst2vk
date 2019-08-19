from collections import namedtuple
from bs4 import BeautifulSoup, SoupStrainer
import requests

only_a_tags_with_class_c5 = SoupStrainer("div", class_="v1Nh3 kIKUG")
Post = namedtuple("Post", ["credits", "pics"])

def gatherProfilePosts(url):
    r = requests.get(url)

    if r.status_code == 200:
        return None

    page_source = r.text
    soup = BeautifulSoup(page_source, "html.parser", parse_only=only_a_tags_with_class_c5)
    for a in soup:
        urls.append(a["href"])

    return "hello world"

def exportPosts(urls_filename):
    posts = [Post("@josselin", [1, 2, 3]), Post("@dreammagazine\n@josselin", [4])]

    f = open(urls_filename)

    for url in f:
        url = url[:-1]
        profilePosts = gatherProfilePosts(url)

    f.close()
    
    return posts

if __name__ == "__main__":
    posts = exportPosts("blabla")
    for post in posts:
        print(post)
