import time
import requests
from bs4 import BeautifulSoup
from lxml import etree

#用于python登录自己选择的页面
headers = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}
try:
    re = requests.get('https://www.hafu.edu.cn/index/ggtz.htm', headers=headers)
    soup = BeautifulSoup(re.content, 'html.parser')
except:
    print("网址出错了")

dom = etree.HTML(re.content)
con = dom.xpath('//a[@class="c269582"]/text()')
times = dom.xpath('//span[@class="c269582_date"]/text()')
web = dom.xpath('//a[@class="c269582"]/@href')



NowTime = time.strftime('%Y-%m-%d', time.localtime())
# NowTime = '2025-01-20' #测试代码

for i in range(len(con)):
    if NowTime in times[i]:
        mydata = {
            'text': con[i],  # 通知的标题
            'desp': '内容:' + con[i] + '<br>'   # 通知的描述，包含公告内容
                    '网址:' + "https://www.hafu.edu.cn"+web[i].split("..",2)[1] + '<br>'   # 公告的链接
                    '日期:' + times[i]  # 公告的日期
        }
        # 发送 POST 请求到指定的 URL，通知服务有新公告
        requests.post('你的token.send', data=mydata)
        # 用来暂停2秒钟，防止发送遗漏
        # time.sleep(2)  
        print('ok')
    else:
        print("暂无通知")
