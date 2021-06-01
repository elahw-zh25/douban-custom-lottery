# douban-lottery-custom
用于帮助有特殊需求的小组抽奖机制。一般的抽奖可以直接使用豆瓣抽奖小助手。
使用方法：
```
python3 lottery.py TARGET_LINK NUMER_OF_LOTTERY
```
在这个小组贴：https://www.douban.com/group/topic/228012134/ 里随机抽10个人的代码如下：
```
python3 lottery.py https://www.douban.com/group/topic/228012134/ 10
```
运行结果如下


# prerequisite
- python3
- selenium
  可以使用pip进行安装。 
  ```
  pip3 install selenium
  ```
- geckodriver
  mac os 可以直接使用 homebrew 安装 
  ```
  brew install geckodriver
  ```


