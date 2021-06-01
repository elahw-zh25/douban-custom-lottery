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

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
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

options = Options()
options.add_argument('-headless')
f = webdriver.Firefox(options=options)

next = sys.argv[1]
while next:
    print("正在分析 "+next, end='\r')
    try:
        f.get(next)
    except:
        break

    reply_content = f.find_element_by_id("comments")
    comments = reply_content.find_elements_by_class_name("reply-doc")
    for c in comments:
        user_link = c.find_element_by_tag_name("h4").find_element_by_tag_name("a")
        username = user_link.get_attribute("text")
        userpage = user_link.get_attribute("href")
        comment = c.find_element_by_class_name("reply-content").get_attribute("innerHTML")
        if userpage not in candidates.keys():
            candidates[userpage] = UserInfo(userpage, username)
        candidates[userpage].add_comment(comment)
    
    try:
        next_page = f.find_element_by_xpath("//span[@class='next']/a")
    except:
        break
    if next_page:
        next = next_page.get_attribute("href")
        time.sleep(1)
f.close()

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
    
