# 开发时间：2022/9/2 17:52  上海大学 21级 智能科学与技术 刘育杰 Anifalak-Lobelia
"""
免责声明
使用前应仔细阅读本声明，一旦开始使用交流学习视为接受本声明所述全部内容。

此脚本仅可用于交流学习python中通过selenium编写脚本的例子，不可用于实际，除学习外其余做法产生的结果本人概不负责。

交流学习者承诺遵守全部中国法律法规及相关规定包括但不限于：《中华人民共和国刑法》《中华人民共和国治安管理处罚法》《中华人民共和国传染病防治法》《中华人民共和国突发事件应对法》《中华人民共和国民法典》《中华人民共和国网络安全法》等法律法规和有关规定及当地法律法规和有关规定。

此脚本默认交流学习者承诺至少满足以下条件：

(1).身体状况：良好（体温不高于37.3）

(2)当天是否在上海：在上海（上海大学校内)

(3).当天进校校区：宝山

(4).当天是否住学校：住校

(5).近7日是否有高中低风险地区旅居史:无

(6).是否被认定为传染病密接：否

(7).当天是否隔离：否

(8).交流学习者及家属，非确诊或疑似“新型冠状病毒”病例，且进场前 14 天内，无任何可疑症状，包括发热、咳嗽、咽痛、胸闷、呼吸困难乏力等。

(9).交流学习者及家属，未去过或经过全国高中低风险地区，且无与全国高中低风险地区来源人员接触史。

(10).交流学习者及家属承诺，做好以下防控工作，①佩戴口罩，做好个人防护；②勤洗手，做好个人卫生；③不打通铺、串门、聚餐，杜绝聚集聊天；④咳嗽或打喷嚏时，使用纸巾遮住口鼻

(11).如有发热、咳嗽、咽痛、胸闷、呼吸困难乏力等症状，立即上报学校及社会疫情管理人员，并坚决服从隔离或治疗安排，绝不瞒报任何情况。

(12).本人杜绝接触存在如上异常症状患者的行为，包括进入患者房间或观察患者等。

如有任何与上述条件不符者，请根据自身情况如实填写，并立刻停止交流学习此脚本！
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time

"在这边把学号、密码、校内宿舍输入进去"

username = ""  # 输入学号填在“”中
password = ""  # 输入密码
Dormitory_address = ""  # 输入宿舍位置


def change_html(day):
    pass


def Screenshot():
    pass


def DoaFakeScreenShot():
    today = str(date.today())  # 获取今天的日期
    today = re.sub(r'-', '.', today)  # 将日期改为正确的格式
    change_html(today)  # 更改
    Screenshot()  # 截图


DoaFakeScreenShot()  # 截图
chrome = webdriver.Chrome()
login_url = "https://selfreport.shu.edu.cn/ReportHistory.aspx"  # 登录网址
chrome.get(login_url)
time.sleep(0.5)
chrome.find_element(by=By.ID, value="username").send_keys(username)  # 传入学号，密码
chrome.find_element(by=By.ID, value="password").send_keys(password)
chrome.find_element(by=By.ID, value="submit-button").click()
time.sleep(0.5)
chrome.find_element(by=By.ID, value="button").click()

"""-------------------------------------------------------------------------------------------------------------"""
result = chrome.find_elements(by=By.XPATH, value='//li/a')  # 通过xpath的方法找到链接
for i in range(len(result) - 1, -1, -1):  # 从下往上找(学校规定：先填之前的，再填现在的)
    str_text = result[i].text
    if re.search(r'未填报', str_text):  # 通过正则的方式判断出最晚的、没填报的
        result[i].click()
        time.sleep(0.5)
        chrome.find_element(by=By.ID, value='p1_ChengNuo-inputEl-icon').click()  # 我承诺
        time.sleep(0.5)
        chrome.find_element(by=By.ID, value='fineui_3-inputEl-icon').click()  # 没有去过外省市
        time.sleep(1)
        chrome.find_element(by=By.ID, value='fineui_22-inputEl-icon').click()  # 在上海进学校
        time.sleep(1)
        chrome.find_element(by=By.ID, value='fineui_25-inputEl-icon').click()  # 进校校区宝山
        time.sleep(1)
        chrome.find_element(by=By.ID, value='fineui_29-inputEl-icon').click()  # 当晚住校且当天不离校
        time.sleep(1)
        chrome.find_element(by=By.ID, value='fineui_31-inputEl-icon').click()  # 所在校区：宝山校区
        time.sleep(1)
        chrome.find_element(by=By.ID, value='fineui_36-inputEl-icon').click()  # 不需要进出校，不申请
        time.sleep(1)
        chrome.find_element(by=By.ID, value='p1_XiangXDZ-inputEl').send_keys(Dormitory_address)  # 校内地址
        time.sleep(1)

        try:
            # chrome.find_element(by=By.XPATH, value='//*[@id="fineui_33"]/input').send_keys(r'  这里传入行程码的绝对路径！！！看不懂算了，直接跑，大概率是能跑的   ')
            time.sleep(1)
        except:
            pass
        else:
            pass

        chrome.find_element(by=By.ID, value='fineui_40-inputEl-icon').click()  # 是否家庭地址
        time.sleep(1)
        chrome.find_element(by=By.ID, value='fineui_41-inputEl-icon').click()  # 近7日是否有高中低风险地区旅居史
        time.sleep(1)
        chrome.find_element(by=By.ID, value='fineui_45-inputEl-icon').click()  # 是否被认定为密接
        time.sleep(1)
        chrome.find_element(by=By.ID, value="p1_ctl01_btnSubmit").click()  # 提交
        time.sleep(0.5)
        chrome.find_element(by=By.ID, value='fineui_53').click()  # 确认提交
        time.sleep(0.5)
        chrome.get(login_url)  # 回到有一堆填报的网页
        time.sleep(0.5)
        result = chrome.find_elements(by=By.XPATH, value='//li/a')  # 重新读取，通过xpath的方法找到链接
"""---------------------------------------------------------------------------------------------------"""
