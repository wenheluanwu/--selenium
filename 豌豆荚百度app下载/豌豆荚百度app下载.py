import os
from selenium import webdriver
from selenium.webdriver.common.by import 

#  浏览器驱动写入到环境变量
os.environ["PATH"] += r"D:\ChromeDriver"

#  创建浏览器驱动对象
driver = webdriver.Chrome()
#  窗口最大化
driver.maximize_window()

#  浏览器访问网站
driver.get("https://www.wandoujia.com/apps/39899/")
#  隐式等待十秒
driver.implicitly_wait(10)

#  网站下载按键的html
"""
<a class="__normal_realname__ normal-dl-btn  " data-bd-track="detail-common_download_main" data-ch="detail_normal_dl" data-app-name="百度" auto-inspect-button-type="download" data-spm-anchor-id="aligames_platform_ug.wdj_seo.0.0">普通下载</a>
"""

#   通过链接文本定位
文本普通下载 = driver.find_element(By.LINK_TEXT,"普通下载")
文本普通下载.click()

#   通过class属性中的部分文本定位
属性名普通下载 = driver.find_element(By.CLASS_NAME,"normal-dl-btn")
属性名普通下载.click()

#   通过一个自定义属性定位
自定义属性定位下载 = driver.find_element(By.CSS_SELECTOR,"[data-app-name='百度']")
自定义属性定位下载.click()

"""
[data-app-name="百度"] XPath 代码是为了基于元素的自定义数据属性来定位。让我详细解释下:
[...] 这种中括号表示法在XPath中是添加predicate筛选条件的语法。
data-app-name="百度" 部分检查了元素的data-app-name属性的值是否等于"百度"。
XPath中的属性选择必须要用@符号加属性名,比如 @class。但是对于自定义数据属性如data-xxx,可以直接写属性名,不需要@符号。
所以[data-app-name="百度"]整体效果是选择所有data-app-name属性值为"百度"的元素。
"""

#   通过组合使用class和文本属性定位
多属性组合下载 = driver.find_element(By.XPATH,"//a[contains(@class, 'normal-dl-btn') and text()='普通下载']")
多属性组合下载.click()

"""
XPath '//a[contains(@class, "normal-dl-btn") and text()="普通下载"]' 使用了几个XPath的函数和语法来定位元素,让我解释下:
//a: 选取页面中的所有<a>标签元素
[...]: 中括号表示Adding a predicate过滤条件,用于从所有<a>中细化选择
contains(@class, "normal-dl-btn"): 调用contains()函数,检查class属性是否包含"normal-dl-btn"文本
and: 与运算符,相当于逻辑"AND"
text()="普通下载": 调用text()函数获取标签之间的文本,检查文本是否等于"普通下载"
所以整体效果就是:先选中所有<a>标签,然后在这些标签中过滤出class属性包含"normal-dl-btn" AND 标签文本等于 “普通下载” 的元素
"""

#   如果链接唯一的话,可以使用绝对路径定位:
XPATH绝对定位下载 = driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div[1]/div[2]/div[3]/div/a[1]")
XPATH绝对定位下载.click()
