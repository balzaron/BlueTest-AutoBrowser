class User(object):

    def __init__(self,url, username, password):
        self._url = url
        self._username = username
        self._password = password

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, v):
        self._url = v

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, v):
        self._username = v

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, v):
        self._password = v

    def assembleMiotechJson(self):

        return {'email': self.username,
                'password': self.password,
                'recaptchaMethod': '"GEETEST"'}
