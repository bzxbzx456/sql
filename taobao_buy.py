import datetime
import time


def login(self):
    # 打开登陆界面
    self.browser.get('https://login.taobao.com/member/login.jhtml')
    # 等待浏览器与selenium完美契合之后在进行下一步动作
    self.browser.implicitly_wait(2)
    print("请你在10秒钟登录")
    time.sleep(10)
    # 跳转到购物车页面
    self.browser.find_element_by_xpath('//*[@id="mc-menu-hd"]/span[2]').click()
    time.sleep(1)
    # 将购物车东西进行全选
    self.browser.find_element_by_id("J_SelectAll").click()
    time.sleep(2)

def panicbuy(self,buy_time):
    while True:
        #获取当时间
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if now_time >= buy_time:
            try:
                self.browser.find_element_by_id("J_Go").click()
                time.sleep(0.5)
                self.browser.find_element_by_link_text('提交订单').click()
                break
            except Exception as e:
                print(e)
                time.sleep(1)
        print(now_time)
        time.sleep(1)
