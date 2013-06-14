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
import xmlinker

class XMManager:
    __state_dict = {}
    sign_url = "http://www.xiami.com/task/signin"
    login_url = "http://www.xiami.com/member/login"

    def __init__(self):
        # XMManager is a singleton
        self.__dict__ = self.__state_dict

    def login(self,email,psw):
        linker = xmlinker.Linker()
        linker.make_link(
            self.login_url,
            {"email":email,"password":psw,"done":"/","submit":"登 录"},
        )

    def sign(self):
        linker = xmlinker.Linker()
        linker.make_link(self.sign_url)

if __name__ == "__main__":
    man = XMManager()
