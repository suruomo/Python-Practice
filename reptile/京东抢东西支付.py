#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#导入库
from selenium import webdriver #打开被脚本操控的浏览器
from selenium.webdriver.common.by import By #定位条件在网页的位置和设置条件达成目标
from selenium.webdriver.support import expected_conditions as EC #判断目标是否达成
from selenium.webdriver.support.ui import WebDriverWait #等待条件达成后再进行下一步操作响应
import time #时间函数，导入目的为了在每次刷新页面前等待0.3秒
import pygame #游戏函数，导入目的是为了在抢购成功时播放音乐

login_url = 'https://passport.jd.com/new/login.aspx'#京东登陆界面网址
init_url = 'https://www.jd.com/'#京东跳转界面网址
order_url =  'https://item.jd.com/100009251834.html'#所购商品页面网址

driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')#这里是Chromedrive的路径，打开被操控浏览器
i = 0#第几次抢购

def play_music():#设定抢票成功后播放的音乐
    filepath = r"F:\histroy.mp3";#这里是抢购成功时播放音乐的路径
    pygame.mixer.init()
    # 加载音乐
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play(start=0.0)
    #播放时长，没有此设置，音乐不会播放，会一次性加载完
    time.sleep(15)
    pygame.mixer.music.stop()
    
    
def login():
    driver.get(login_url)#跳转入京东登陆网址
    driver.maximize_window()#浏览器最大化界面
    WebDriverWait(driver,1000).until(
        EC.element_to_be_clickable((By.CLASS_NAME,'login-tab-r'))#确认密码登陆按钮已经刷新出来
    )
    driver.find_element_by_class_name('login-tab-r').click()#点击密码登陆按钮
    driver.find_element_by_id('loginname').clear#清空账号框内容
    driver.find_element_by_id('loginname').send_keys('18691638297')#在账号框输入你的京东账号
    driver.find_element_by_id('nloginpwd').clear#清空密码框内容
    driver.find_element_by_id('nloginpwd').send_keys('200920092hmm')#在密码框输入你的京东密码
    driver.find_element_by_id('loginsubmit').click()#点击登陆按钮
    #手动在网页页面上完成验证操作（滑块验证）
    WebDriverWait(driver,1000).until(EC.url_to_be(init_url))#判断是否自动跳转到京东首页
    print('登陆成功')#如果自动跳转，则结果框打印登陆成功
    driver.get(order_url)#跳转到所需购买商品网页
    #time.sleep(10)#等待十秒钟后开始抢购
    
def buy():
    driver.get(order_url)
    WebDriverWait(driver,1000).until(
        EC.element_to_be_clickable((By.CLASS_NAME,'btn-add'))
    )
    tr_list = driver.find_elements_by_xpath('//div[@class="dd"]/div[@title]')
    try:
        driver.find_element_by_id('InitCartUrl').click()
        if driver.current_url.split("#")[0] !=order_url:
            print('当前有货')
            #print(driver.current_url.split("#")[0])
            #print(order_url)
            pay()
            return 1
    except:
        print("当前无货")
        pass
    for tr in tr_list:
        if (("无货") not in tr.get_attribute('title')and tr.get_attribute('class')[-8:] != 'selected'):
            tr.click()
            WebDriverWait(driver,1000).until(
        EC.element_to_be_clickable((By.ID,'InitCartUrl'))
    )
            driver.find_element_by_id('InitCartUrl').click()
            WebDriverWait(driver,1000).until(EC.url_changes)#加入购物车页面
            pay()
            return 1
            break
    return 0

def pay():
    WebDriverWait(driver,1000).until(
EC.element_to_be_clickable((By.CLASS_NAME,'btn-addtocart'))
)
    driver.find_element_by_class_name('btn-addtocart').click()
    WebDriverWait(driver,1000).until(EC.url_changes)#购物车支付页面
    WebDriverWait(driver,1000).until(
    EC.element_to_be_clickable((By.CLASS_NAME,'submit-btn'))
)
    driver.find_element_by_class_name('submit-btn').click()
    WebDriverWait(driver,1000).until(EC.url_changes)#支付界面
    WebDriverWait(driver,1000).until(
    EC.element_to_be_clickable((By.CLASS_NAME,'checkout-submit'))
)
    driver.find_element_by_class_name('checkout-submit').click()
    play_music()
    
                
login()
while True:
    key = buy()
    if key ==0:
        time.sleep(1)
        i += 1
        if i % 100 ==0:
            print("第{}次抢购".format(i))
    if key ==1:
        print('购买成功')
        break


# In[ ]:




