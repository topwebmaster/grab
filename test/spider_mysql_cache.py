from unittest import TestCase

from grab.spider import Spider, Task, Data
from test.util import BaseGrabTestCase
from .mixin.spider_cache import SpiderCacheMixin


class BasicSpiderTestCase(TestCase, SpiderCacheMixin):
    def setUp(self):
        SpiderCacheMixin.setUp(self)

    def setup_cache(self, bot):
        bot.setup_cache(backend='mysql', database='spider_test',
                        user='web', passwd='web-**')