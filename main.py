from args import args
from config_init import initializeConfig
from properties import props 
from export_posts import exportPosts

if __name__ == "__main__":
    config_filename = args.config
    vk_token_filename = args.token
    urls_filename = args.urls

    initializeConfig(config_filename)
    print(props)

    posts = exportPosts(urls_filename)
    for post in posts:
        print(post)
