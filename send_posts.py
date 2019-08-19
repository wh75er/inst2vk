import vk_api
import time

day = 86400
hour = 3600

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

    photo_list = upload.photo_wall(
        "temp/1.jpg"
    )

    vk_photo_url = ','.join("photo{owner_id}_{id}".format(**item) for item in photo_list)

    vk.wall.post(owner_id=-185664229, attachments=vk_photo_url, message="hello world", publish_date=1566239997)
    
    return 

if __name__=="__main__":
    sendPosts("../token", [])
