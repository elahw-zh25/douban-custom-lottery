'''
    Copyright [2021] [elahw-zh25]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
'''

import requests
from bs4 import BeautifulSoup
import sys
import random
import time

class UserInfo:
    def __init__(self, page, name):
        self.userpage = page
        self.username = name
        self.comments = []
        
    def add_comment(self, comment):
        self.comments.append(comment)
        
    def get_comments(self):
        return self.comments;
        
def read_char():
    while 1:
        c = sys.stdin.read(1)
        if c == 'Y' or c =='y' or c =='N' or c == 'n':
            break
    return c
    
candidates = {}

next = sys.argv[1]
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
while next:
    print("正在分析 "+next, end='\r')
    try:
        f = requests.get(next, headers = headers)
    except:
        break

    res = BeautifulSoup(f.content, 'html.parser')
    reply_content = res.findAll("ul", {"id":"comments"})
    comments = reply_content[0].findAll("div", {"class":"reply-doc"})
    for c in comments:
        username = c.h4.a.text
        userpage = c.h4.a['href']
        comment = c.p.text
        if userpage not in candidates.keys():
            candidates[userpage] = UserInfo(userpage, username)
        candidates[userpage].add_comment(comment)

    next_page = res.findAll("span", {"class":"next"})

    if len(next_page) > 0 and next_page[0].a:
        next = next_page[0].a['href']
        time.sleep(1)
    else:
        break

print("")
target = int(sys.argv[2])
while target > 0:
    keys = list(candidates.keys())
    count = len(keys)
    if count == 0:
        print("没有更多的用户了。")
        break
    rand = random.randint(0, count - 1)
    key = keys[rand]
    print(candidates[key].username + ", UserPage:" + key)
    for comment in candidates[key].get_comments():
        print("@reply: " + comment)
    print("确定抽取此用户？(y/n)")
    c = read_char()
    if c == 'Y' or c == 'y':
        target = target - 1
        del candidates[key]
