import requests

class Post:
    def __init__(self):
        blog_url = "https://api.npoint.io/caea24fdbc62fc4295cf"
        response = requests.get(blog_url)
        self.all_post = response.json()
        self.num_post = len(self.all_post)

    def get_post(self, num):
        return self.all_post[num]

