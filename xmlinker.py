#!/usr/bin/python
#-*- coding: utf-8 -*-

# Copyright (C) 2013 rapidhere
#
# Author:     rapidhere <rapidhere@gmail.com>
# Maintainer: rapidhere <rapidhere@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import xmenv
import urllib2
import cookielib
import urllib

class Linker:
    __state_dict = {}
    def __init__(self):
        # Linker is a Signleton
        self.__dict__ = self.__state_dict

        if not hasattr(self,"_ckjar"):
            self._ckjar = cookielib.CookieJar()

        if not hasattr(self,"_opener"):
            self._opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self._ckjar))

        self._resp = None

    def make_link(self,url,data_dict = {},header = xmenv.HTTPHeader):
        data = urllib.urlencode(data_dict)
        req = urllib2.Request(
            url = url,
            headers = header,
            data = data
        )

        self._resp = self._opener.open(req)


    def get_respinfo(self):
        return self._resp.info().dict

    def get_respmsg(self):
        return self._resp.msg

    def get_respcode(self):
        return self._resp.code

    def get_respbuf(self):
        return self._resp.read()
