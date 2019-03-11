#!C:/SoftWare/Virtualenv/python3
# @FileName: HeaderMidWare
# @Author: 李易阳
# @Time: 2019/3/11
# @Soft: PyCharm


# 导包
from scrapy.utils.project import get_project_settings
import random

# 其实这里有两种方式
# 一种是利用get_project_settings获取settings
# 另外一个是crawler


class HeaderMidware():
    def __init__(self, ua_list):
        self.ua_list = ua_list

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            ua_list=crawler.settings.get("USER_AGENT_LIST")
        )

    def process_request(self, request, spider):
        ua = random.choice(self.ua_list)
        if ua:
            request.headers["User-Agent"] = ua
            spider.logger.info(u'User-Agent is : {} {}'.format(request.headers.get('User-Agent'), request))
