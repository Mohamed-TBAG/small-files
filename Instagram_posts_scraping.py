from os import path
from sys import exit
import  requests
from hashlib import md5
from urllib import parse
from random import choice
from _Exceptions import *
from threading import Thread
from json import loads, dumps
from re import search as ReSearch
from random import choice, randint
from urllib.error import HTTPError
from http.cookiejar import CookieJar
from string import ascii_lowercase , digits
from http.cookiejar import CookieJar, Cookie
from logging import basicConfig, getLogger, DEBUG
def create_proxy():
    return {
        'http':'socks5h://{}:{}@127.0.0.1:9150'.format(randint(1, 99999), randint(1, 99999)),
        'https':'socks5h://{}:{}@127.0.0.1:9150'.format(randint(1, 99999), randint(1, 99999))
    }
basicConfig(filename=f"Log_{path.basename(path.abspath(__file__))[:-3]}.log", level=DEBUG, format='%(levelname)s:: - %(message)s ; Time %(asctime)s')
logger = getLogger('Instagram_Screping')
class ProfilePosts:
    def get_profile_id(self, username):
        api = f"{username}/"
        try:
            profile_id_object = self.request_object(api=api)
            profile_id_respone = self.make_request(profile_id_object, read_only=True)
            id_query = r',"props":{"id":"(.*?)",'
            page_id = ReSearch(id_query, profile_id_respone).group(1)
            return page_id
        except HTTPError:
            if HTTPError.code == 403:
                error_message = f"Error {HTTPError.code} : '{HTTPError.reason}' AT {api}"
                raise ProxyError(error_message, HTTPError.code)
            elif HTTPError.code == 429:
                error_message = f"Error {HTTPError.code} : '{HTTPError.reason}' AT {api}"
                raise TooManyRequests(error_message, HTTPError.code)
            else:
                error_message = f"Error {HTTPError.code} : '{HTTPError.reason}' AT {api}"
                raise MainException(HTTPError.reason, HTTPError.code)
        except Exception as UnknownError:
            raise MainException(str(UnknownError))
    def get_profile_posts(self, username, user_id, nextpage):
        self.finished = False
        api = "graphql/query/"
        query_hash = "42323d64886122307be10013ad2dcc44"
        variables = {
            "id" : user_id,
            "first" : 50,"after" : nextpage}
        query_params = {
            'query_hash' : query_hash,
            'variables' : dumps(variables, separators=(',', ':'))}
        try:
            profile_posts_object = self.request_object(api=api, query=query_params)
            resone_dict = self.make_request(profile_posts_object)

###################   (((  resone_dict  ))) is the response for each 50 post

            end_cursor = resone_dict["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]["end_cursor"]
            self.save_end_curso(username, end_cursor)
            if end_cursor == "" or end_cursor == None:
                self.finished = True
        except HTTPError:
            if HTTPError.code == 403:
                error_message = f"Error {HTTPError.code} : '{HTTPError.reason}' AT {api}"
                raise ProxyError(error_message, HTTPError.code)
            elif HTTPError.code == 429:
                error_message = f"Error {HTTPError.code} : '{HTTPError.reason}' AT {api}"
                raise TooManyRequests(error_message, HTTPError.code)
            else:
                error_message = f"Unknown Error {HTTPError.code} : '{HTTPError.reason}' AT {api}"
                raise MainException(HTTPError.reason, HTTPError.code)
        except KeyError as KeyNotFound:
            raise MainException(f"there is some dict data are not found; {KeyNotFound}")
        except Exception as UnknownError:
            raise MainException(f"UnKnown error : {UnknownError}")
        if self.finished:
            print(f"all {username} posts finish")
            return
        self.get_profile_posts(username, user_id, end_cursor)

    def save_end_curso(self, username, end_cursor):
        end_cursor_data = {
            "username":username,
            "end_cursor":end_cursor
            }
        with open("end_cursor_dicts.txt","a+", encoding="utf-8") as end_cursor_dicts:
            end_cursor_dicts.write(f"{end_cursor_data}\n")
            end_cursor_dicts.close()

    def first_scraped_cursor(self, username, end_cursor):
        end_cursor_data = {
            "username":username,
            "end_cursor":end_cursor
            }
        with open("first_end_cursor.txt","a+", encoding="utf-8") as end_cursor_dicts:
            end_cursor_dicts.write(f"{end_cursor_data}\n")
            end_cursor_dicts.close()
class InstaBaseAPI(ProfilePosts):
    INSTA_URL = 'https://www.instagram.com/'
    LANDING_URL = 'api/v1/public/landing_info/'
    RE_CSRF_QUERY   = r'csrf_token\\":\\"([^\\"]+)'
    RE_HASH_QUERY   = r'rollout_hash\":\"([^\"]+)'
    RE_IgDid_QUERY  = r'"}]},"device_id":"(.*?)",'
    RE_DATR_QUERY   = r'_js_datr":{"value":"(.*?)",'
    RE_MID_QUERY    = r'mid=(.*?);'
    req_session=requests.Session()
    req_session.proxies = create_proxy()
    def __init__(self):
        self.posts_counter = 0
        self.hands = []
        self.req_session.cookies = CookieJar()
        self.gis_val = self.gis()
        self.init_data()
    def init_data(self):
        self.req_session.cookies.set_cookie(
            Cookie(
                0, 'ig_cb', '1', None, False,
                'www.instagram.com', False, None, '/',
                False, False, None, True, None, None, {}))
        HTML_respone   = self.make_request(self.request_object(""),read_only=True)
        self.csrftoken = ReSearch(self.RE_CSRF_QUERY ,HTML_respone).group(1)
        self.r_hash    = ReSearch(self.RE_HASH_QUERY ,HTML_respone).group(1)
        _js_ig_did     = ReSearch(self.RE_IgDid_QUERY,HTML_respone).group(1)
        _js_datr       = ReSearch(self.RE_DATR_QUERY ,HTML_respone).group(1)

        _cookies_info = {
            'datr': _js_datr,
            'ig_did': _js_ig_did,
            'dpr': "0.75",
            'ig_nrcb': '1',
            'ig_pr': '1'
            }
        self.cookies_setter(_cookies_info)
        self.make_request(
            self.request_object(self.LANDING_URL)
            )
    def gis(self):
        """DO NOT RUN"""
        options = ascii_lowercase + digits
        text = ''.join([choice(options) for _ in range(8)])
        return md5(text.encode()).hexdigest()
    def GIS(self, query):
        """DO NOT RUN"""
        if self.gis_val and query.get('query_hash') and query.get('variables'):
            vars = query.get('variables')
        else:return None
        signiture = md5()
        signiture.update('{rhx_gis}:{var}'.format(rhx_gis=self.gis_val,var=vars).encode('utf-8'))
        signiture = signiture.hexdigest()
        return signiture
    def cookies_setter(self, cookies:dict):
        """DO NOT RUN"""
        for k, v in cookies.items():
            self.req_session.cookies.set_cookie(
                Cookie(
                0, k, v, None, False,
                'www.instagram.com', False, None, '/',
                False, False, None, True, None, None, {}))
    @property
    def headers(self):
        return {
            'User-Agent': 'Instagram 148.0.0.33.121 Android (28/9; 480dpi; 1080x2137; HUAWEI; JKM-LX1; HWJKM-H; kirin710; en_US; 216817344)',
            'Accept': '*/*',
            'Accept-Language': 'en-US',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'close'
            }
    def request_object(self, api, query=None, data=None, headers=None):
        url = self.INSTA_URL+api
        _Data=None
        if not headers:
            headers = self.headers
        if data and query:
            print("DO not send data and query in same request\nthe code is not ready")
            exit(0)
        elif query and not data:
            url += '?' + parse.urlencode(query)
            Gis = self.GIS(query)
            if Gis:
                headers['X-Instagram-GIS'] = Gis
        elif data and not query:
            headers.update({
                'x-csrftoken': self.csrftoken,
                'x-requested-with': 'XMLHttpRequest',
                'x-instagram-ajax': self.r_hash,
                'Referer': 'https://www.instagram.com',
                'Authority': 'www.instagram.com',
                'Origin': 'https://www.instagram.com',
                'Content-Type': 'application/x-www-form-urlencoded'
            })
            _Data = (''.encode('ascii') if data == "" else parse.urlencode(data).encode('ascii'))
        return self.req_session.prepare_request(request=requests.Request('GET', url, data=_Data, headers=headers))
        
    def make_request(self, req:requests.PreparedRequest, read_only=False, full_response=False):
        retries=8
        while True:
            try:
                proxy = create_proxy()
                response = self.req_session.send(req, proxies=proxy)
                if response.status_code == 401:
                    logger.error(f"bad proxy : {proxy}")
                    raise LoginRequired("Forbidden request, change the proxy",401)
                elif response.status_code != 200:
                    logger.error(f"bad proxy : {proxy}")
                    raise NoResponse("change the proxy", response.status_code)
                if "require_login" in response.text or \
                "Please wait a few minutes before trying again" in response.text:
                    logger.error(f"bad proxy : {proxy}")
                    raise ProxyError("BAD PROXY, Change it",403)
                if full_response:
                    return response
                if read_only:
                    return response.text
                return loads(response.text)
            except Exception as e:
                logger.error(f"{e}")
                print(e)
                self.req_session.proxies=create_proxy()
                retries-=1
                if retries==0:
                    break
                print("Retrying...")
        raise ManyBadProxies("chack your proxy list")
def get_user_data(username):
    api =  "api/v1/users/web_profile_info/"
    data = {"username": username}
    page_api = a.request_object(api=api,query=data)
    page_respone = a.make_request(page_api)

    ########     ((( page_respone ))) is  first response , it contains only first 12 post

    first_end_cursor = page_respone["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]["end_cursor"]
    a.first_scraped_cursor(username, first_end_cursor)
    a.save_end_curso(username, first_end_cursor)
    a.get_profile_posts(username=username, user_id=a.get_profile_id(username), nextpage=first_end_cursor)
if "__main__" == __name__:
    a = InstaBaseAPI()
    usernames=[
        "radio_alghad",
        "mohamedalhabbo",
        "instagram",
        "qaflab"
        ]
    for username in usernames:
        try:
            Thread(get_user_data(username)).start()
        except Exception as e:
            print(f"Error : {e}")
    print("All users finished")