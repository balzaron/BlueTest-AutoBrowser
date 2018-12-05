import requests, json
from requests import Response
from common.UserEntity import User

# filepath = '/tmp/test.log'
# logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     handlers=(logging.FileHandler(filepath), logging.StreamHandler()))
from common.config_center import globalconfig
from common.log import miologging
logger = miologging()

cookies= {'MIOYING_SESSION': globalconfig().get('userInfo').get('cookie')}
cookies = requests.utils.cookiejar_from_dict(cookies, cookiejar=None, overwrite=True)
requests.packages.urllib3.disable_warnings()
headers = {
    'Content-Type': "application/json",
    'MIOYING_SESSION': globalconfig().get('userInfo').get('cookie'),
    'cache-control': "no-cache",
    }

class Request(object):
    user: User = None
    tmp_data: Response = None
    tmp_data_list: list=[]

    def __init__(self):

        self.__session = requests.session()
        self.__session.cookies = cookies
        # try:
        #     self.__session.post(userInfo.url, userInfo.assembleJson())
        # except Exception as e:
        #     logger.error('login url or user info is not correct! {}'.format(e))

    def get(self, url:str, data:dict=None, **kwargs):
        """
        :param args:
        :param kwargs: url & request body data is required
        :return: self instance
        """
        if url is not None and data is not None:
            tmp=''
            for k,v in data.items():
                tmp += '%s=%s'%(k,v)+'&'
            url += '?'+tmp
            url = url[:-1]
            # logger.info(url)
            try:
                self.tmp_data = self.__session.get(url, verify=False, headers=headers)
                self.tmp_data_list.append(self.tmp_data)
                # logger.info(self.tmp_data)
                return self
            except Exception as e:
                logger.error(e)
        elif url is not None and data is None:
            try:
                self.tmp_data = self.__session.get(url, verify=False, headers=headers)
                self.tmp_data_list.append(self.tmp_data)
                logger.info(self.tmp_data)
                return self
            except Exception as e:
                logger.error(e)
        else:
            raise AttributeError("request body or url is not set!")

    def post(self,url,data, **kwargs):
        """
        :param url:  request url
        :param data: request body/payload
        :param kwargs: none
        :return: self instance
        """
        if data is not None and url is not None:
            # try:
            data = json.dumps(data)
            self.tmp_data = self.__session.post(url=url, data=data, headers=headers)
            self.tmp_data_list.append(self.tmp_data)
            return self
            # except Exception as e:
            #     logger.error(e)
        else:
            raise AttributeError("request body or url is not set!")

    def put(self, url, data):
        """
        :param url: request url
        :param data: request body / payload
        :return: self instance
        """
        if data is not None and url is not None:
            try:
                data = json.dumps(data)
                self.tmp_data = data.session.put(url, data, verify=False, headers=headers)
                # self.tmp_data_list.append(self.tmp_data)
                return self
            except Exception as e:
                logger.error(e)
        else:
            raise AttributeError("request body or url is not set!")

    def delete(self,url):
        pass

    def assertion(self):
        pass
    #
    #
    # def __del__(self):
    #     self.__session.close()
if __name__ == '__main__':

    url = 'https://release.miotech.com/api/user/preference/save'
    data = {"currency":"AUD","language":"en-UN"}
    req = Request()
    res = req.post(url, data)\
        .get(url, data)\
        .put(url, req.tmp_data_list[-2])\
        .post(url, req.tmp_data)
    print(res.tmp_data.status_code)
    print(res.tmp_data.json())