#!C:/SoftWare/Virtualenv/python3
# @FileName: fake_useragent
# @Author: 李易阳
# @Time: 2019/3/11
# @Soft: PyCharm

from fake_useragent import UserAgent

class RandomUserAgentMiddleWare(object):
    # 随机更换useragent
    def __init__(self, crawler):
        # 初始化
        super(RandomUserAgentMiddleWare, self).__init__()
        self.ua = UserAgent()
        # 从setting文件中读取RANDOM_UA_TYPE值
        self.ua_type = crawler.settings.get('RANDOM_UA_TYPE','random')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        def get_ua():
            return getattr(self.ua, self.ua_type)

        print(get_ua())
        request.headers.setdefault("User_Agent", get_ua())




