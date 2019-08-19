import vk_api
import time

day = 86400
hour = 3600

def findTimeIncrement(n):
    k = 24/n
    return k*hour

def sendPosts(token_filename, posts):
    current_time = time.time()
    f = open(token_filename, 'r')
    token = None
    for tkn in f:
        token = tkn
    f.close()
    token = token[:-1]

    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()

    upload = vk_api.VkUpload(vk_session)

    n = len(posts)
    inc = findTimeIncrement(n)
    publish_time = current_time + 30
    for post in posts:
        photos = []
        
        for image in post.pics:
            photos.append("temp/{}.jpg".format(image))

        photo_list = upload.photo_wall(
            photos
        )

        vk_photo_url = ','.join("photo{owner_id}_{id}".format(**item) for item in photo_list)

        vk.wall.post(owner_id=-185664229, attachments=vk_photo_url, message=post.credits, publish_date=publish_time)

        publish_time += inc
    
    return 

if __name__=="__main__":
    sendPosts("../token", [])
