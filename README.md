# 豆瓣特殊机制手动开奖  

用于帮助有特殊需求的小组抽奖机制，比如需要筛选掉一些主动放弃抽奖的用户。每抽选一位候选人，抽选者可以查看被抽中人的个人主页及本帖回复，以便人工筛选掉一些不符合抽奖规定的选手。
目前仅支持回复抽奖。一般的抽奖可以直接使用豆瓣抽奖小助手。  
  
**申明：本代码只是用于帮助自动化一些复杂的人工流程，使用本代码进行其他不符合豆瓣社区规定的行为后果自负。**  
  
使用方法：
```
python3 lottery.py TARGET_LINK NUMER_OF_LOTTERY
```
在这个小组贴：https://www.douban.com/group/topic/228012134/ 里随机抽10个人的指令：
```
python3 lottery.py https://www.douban.com/group/topic/228012134/ 10
```
运行结果如下
![](https://github.com/elahw-zh25/douban-custom-lottery/blob/main/Example.png)

# Prerequisite
- python
- BeautifulSoup, requests
  可以使用pip进行安装。 
  ```
  pip install bs4 requests
  ```


