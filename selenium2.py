# -*- coding: UTF-8 -*-
import threading
import re
import os
import pycurl
import io
from bs4 import BeautifulSoup
from collections import Counter
import pymysql
import sys
import time


def mainurl(url1):
    global linkurl
    linkurl = []
    try:
        c = pycurl.Curl()
        urlcstom = url1
        if not 'http://' in url1:
            url = 'http://' + urlcstom
        else:
            url = urlcstom
        c.setopt(c.URL, url)

        b = io.BytesIO()

        c.setopt(c.WRITEFUNCTION, b.write)

        #c.setopt(c.FOLLOWLOCATION, 1)
        #c.setopt(c.HEADER, True)

        c.perform()
        s = b.getvalue().decode('UTF-8')
        soup = BeautifulSoup(b.getvalue(), "html.parser")
        tags = soup('link')
        for tag in tags:
            x = tag.get('href', None)
            if not 'http://' in x and x != '':
                if x[0] != '/':
                    weburl = url + '/' + x
                else:
                    weburl = url + x
            else:
                weburl = x

            linkurl.append(weburl)

        tags = soup('a')
        for tag in tags:
            x = tag.get('href', None)
            if not 'http://' in x and x != '':
                if x[0] != '/':
                    weburl = url + '/' + x
                else:
                    weburl = url + x
            else:
                weburl = x
            linkurl.append(weburl)
        linkurl = list(set(linkurl))
    except:
        pass
