from collections import namedtuple
from bs4 import BeautifulSoup, SoupStrainer
import requests, json, lxml

#only_dev_tags_with_post_class = SoupStrainer("div")#, class_="v1Nh3 kIKUG")
Post = namedtuple("Post", ["credits", "pics"])

def get_user_data_json(script_tags):
    try:
        json_text = None
        for tag in script_tags:
            if "window._sharedData = " in tag.text:
                json_text = tag.text
                break

        json_text = json_text[len("window._sharedData = "):]
        json_text = json_text[:-1]
        json_obj = json.loads(json_text)
        return json_obj
    except:
        print("Something went wrong with json object gathering!")

def gatherProfilePosts(url, n):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    script_tags = (soup.find_all('script'))
    json_obj = get_user_data_json(script_tags)

    username = json_obj["entry_data"]["ProfilePage"][0]["graphql"]["user"]["username"]
    images = json_obj["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]
    print(images)
    #print(json_obj)


    return "hello world"

def exportPosts(urls_filename, n):
    posts = [Post("@josselin", [1, 2, 3]), Post("@dreammagazine\n@josselin", [4])]

    f = open(urls_filename)

    for url in f:
        url = url[:-1]
        profilePosts = gatherProfilePosts(url, n)

    f.close()
    
    return posts

if __name__ == "__main__":
    posts = exportPosts("../urls", 3)
    #for post in posts:
        #print(post)
