# coding: utf-8
# @Time: 2019-07-24 23:40
# @Author: 'haifeng.shi@klook.com'

import attr

@attr.s
class C(object):
    _x=attr.ib()

print(C(x=1))


attr.fields()

