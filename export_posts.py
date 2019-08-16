from collections import namedtuple

def exportPosts(urls_filename):
    Post = namedtuple("Post", ["credits", "pics"])
    posts = [Post("@josselin", [1, 2, 3]), Post("@dreammagazine\n@josselin", [4])]
    
    return posts

if __name__ == "__main__":
    print()
