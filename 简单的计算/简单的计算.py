import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#  把浏览器驱动写入到环境配置
os.environ["PATH"] += r"D:\ChromeDriver"

#  创建谷歌浏览器驱动对象
driver = webdriver.Chrome()
#  隐式等待10秒
driver.implicitly_wait(10)
#  窗口最大化
driver.maximize_window()
#  进入数学计算网站
driver.get("https://www.wolframalpha.com/")

#  寻找需要计算的元素
ElementaryMath = driver.find_element(By.LINK_TEXT,"Elementary Math")
#  点击它
ElementaryMath.click()

#  寻找基础数学计算对象
number_add = driver.find_element(By.LINK_TEXT,"125 + 375")
#  点击它
number_add.click()

#  寻找计算输入文本框元素
input_number = driver.find_element(By.CLASS_NAME,"kEfuLV")
#  对文本框按下crtl + a
input_number.send_keys(Keys.CONTROL + "a")
#  对文本框使按下del键
input_number.send_keys(Keys.DELETE)
#  输入要计算的数据例如35 + 75
input_number.send_keys("35 + 75")
#  寻找计算按键元素
compute = driver.find_element(By.CSS_SELECTOR,"path[d^='M19 2H5a3 3 0 0 0-3 3v14a3']")
#  点击它
compute.click()
