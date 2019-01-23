import logging

import requests, json
from requests import Response
from mioAuto.model.UserObj import User

requests.packages.urllib3.disable_warnings()
logger = logging.getLogger(__name__)

class Request(object):
    user: User = None
    data: Response = None
    data_list: list=[]

    def __init__(self, cookies):
        _cookies = {'MIOYING_SESSION': cookies}
        _cookies = requests.utils.cookiejar_from_dict(_cookies, cookiejar=None, overwrite=True)
        self.headers = {
            'Content-Type': "application/json",
            'MIOYING_SESSION': cookies,
            'cache-control': "no-cache",
        }

        self.__session = requests.session()
        self.__session.cookies = _cookies


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
                self.data = self.__session.get(url, verify=False, headers=self.headers)
                self.data_list.append(self.data)
                # logger.info(self.data)
                return self
            except Exception as e:
                logger.error(e)
        elif url is not None and data is None:
            try:
                self.data = self.__session.get(url, verify=False, headers=self.headers)
                self.data_list.append(self.data)
                logger.info(self.data)
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
            self.data = self.__session.post(url=url, data=data, headers=self.headers)
            self.data_list.append(self.data)
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
                self.data = data.session.put(url, data, verify=False, headers=self.headers)
                # self.data_list.append(self.data)
                return self
            except Exception as e:
                logger.error(e)
        else:
            raise AttributeError("request body or url is not set!")

    def delete(self,url):
        pass

    def assertion(self):
        pass

