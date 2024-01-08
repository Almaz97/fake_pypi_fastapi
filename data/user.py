import datetime


class User:

    def __init__(self, name, email, password):
        self.id = 1
        self.name = name
        self.email = email
        self.hash_password = password
        self.created_date = None
        self.profile_image_url = ""
        self.last_login: datetime.datetime = None
