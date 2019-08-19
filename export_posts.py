from collections import namedtuple
from bs4 import BeautifulSoup, SoupStrainer
import requests, json, lxml
import os

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
    images = json_obj["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]
    count = 0
    saved_images = []
    for image in images:
        image = image["node"]
        if count >= n:
            break
        if image["__typename"] == "GraphSidecar" or image["__typename"] == "GraphImage":
            saved_images.append(image)
            count+=1

    return saved_images

def gatherInfoAboutSubOwner(text):
    _id = ""
    got_id = False
    for word in text:
        for sym in word:
            if got_id == True:
                if sym not in ["\n", ",", " "]:
                    _id += sym
                else:
                    return _id
            if sym == "@":
                got_id = True
                
    return _id

def formProfilePosts(jsonPosts, count):
    posts = []
    for postJson in jsonPosts:
        owner = postJson["owner"]["username"]
        subowner = gatherInfoAboutSubOwner(postJson["edge_media_to_caption"]["edges"][0]["node"]["text"])
        credits = "inst\n@{}\n@{}".format(owner, subowner) if subowner != "" else "inst\n@{}".format(owner)

        os.system("wget -q -O temp/{}.jpg {}".format(count, postJson["display_url"]))
        post = Post(credits, [count])
        posts.append(post)

        count+=1

    return posts, count

def exportPosts(urls_filename, n):
    posts = []

    f = open(urls_filename)

    count = 1
    for url in f:
        url = url[:-1]
        profilePostsJson = gatherProfilePosts(url, n)
        profile_posts, count = formProfilePosts(profilePostsJson, count)
        posts.extend(profile_posts)

    f.close()

    return posts

if __name__ == "__main__":
    posts = exportPosts("../urls", 3)
    #for post in posts:
        #print(post)
