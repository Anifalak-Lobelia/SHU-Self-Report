# SHU self report
上海大学每日一报 健康之路 会自动填写所有未填报的每日一报 行程码适用  SHU Shanghai University self report script
____________________________________________
## __免责声明__
__使用前应仔细阅读本声明，一旦开始使用交流学习视为接受本声明所述全部内容。__

___此脚本仅可用于交流学习python中通过selenium编写脚本的例子，不可用于实际，除学习外其余做法产生的结果本人概不负责。___

__交流学习者承诺遵守全部中国法律法规及相关规定包括但不限于：《中华人民共和国刑法》《中华人民共和国治安管理处罚法》《中华人民共和国传染病防治法》《中华人民共和国突发事件应对法》《中华人民共和国民法典》《中华人民共和国网络安全法》等法律法规和有关规定及当地法律法规和有关规定。__

__此脚本默认交流学习者承诺至少满足以下条件：__

__(1).身体状况：良好（体温不高于37.3）__

__(2)当天是否在上海：在上海（上海大学校内)__

__(3).当天进校校区：宝山__

__(4).当天是否住学校：住校__

__(5).近7日是否有高中低风险地区旅居史:无__

__(6).是否被认定为传染病密接：否__

__(7).当天是否隔离：否__

__(8).交流学习者及家属，非确诊或疑似“新型冠状病毒”病例，且进场前 14 天内，无任何可疑症状，包括发热、咳嗽、咽痛、胸闷、呼吸困难乏力等。__

__(9).交流学习者及家属，未去过或经过全国高中低风险地区，且无与全国高中低风险地区来源人员接触史。__

__(10).交流学习者及家属承诺，做好以下防控工作，①佩戴口罩，做好个人防护；②勤洗手，做好个人卫生；③不打通铺、串门、聚餐，杜绝聚集聊天；④咳嗽或打喷嚏时，使用纸巾遮住口鼻__

__(11).如有发热、咳嗽、咽痛、胸闷、呼吸困难乏力等症状，立即上报学校及社会疫情管理人员，并坚决服从隔离或治疗安排，绝不瞒报任何情况。__

__(12).本人杜绝接触存在如上异常症状患者的行为，包括进入患者房间或观察患者等。__

___如有任何与上述条件不符者，请根据自身情况如实填写，并立刻停止交流学习此脚本！___
______________________________________________

### 1.chromedriver（新手小白必看！！！！！！！按照下面这俩个网页链接做一定不会错！！！！！！！！！！）
本项目中需要用到 chromedriver 请至 https://chromedriver.storage.googleapis.com/index.html 网站中下载

请把chromedriver 与 SHU-self-report.py 文件 放在一文件夹中  (代码中并不是绝对路径，而是相对路径，有需求可以更改为绝对路径)

关于chromedriver 的具体使用方法请见 https://blog.csdn.net/weixin_45109684/article/details/117650036

### 2.配置python环境
配置Python环境:  __selenium__

### 3.更改python文件中的内容
仅需更改学号、密码、校内宿舍


![信息填写](https://user-images.githubusercontent.com/112788213/195988379-b4ce63d7-4292-4413-a556-f2321d221934.png)

### 4.联系我
脚本目前有很多不足，欢迎大家联系、改进、指导。邮箱：liuyujie@shu.edu.cn


__如果可以的话点个小星星Star是对我最大的鼓励！谢谢！__


![star](https://user-images.githubusercontent.com/112788213/195989156-4948283f-d1b6-4bdf-9202-80f27a4d45a5.png)


### 5.可能还会用到的一些小工具
1. 行程码网页：https://xc.caict.ac.cn/#/login


2. 如果有能力的同学应该能自行解决行程码的问题。我在脚本中提供了提交行程码的接口。按照如图所示的操作，在r''中填写行程码截图的绝对路径
![绝对路径](https://user-images.githubusercontent.com/112788213/195988674-f538f319-13d8-4d4a-8552-df9f4990ac70.png)

### 6.更新
#### 2023-2-6
转眼间到了2月份，今天是开学的日子，去年一整年的混乱与无助终将过去也已经过去，今后再无可能有任何形式的封校和隔离，乙类乙管的当下唯有保护好自己的身体，此脚本已失去任何意义，祝各位身体健康、万事如意、学业有成。


#### 2022-12-3
1. 网页元素有所改动，已做更改

2. 提升了运行速度（之前sleep的时间太长了，在保证可行的范围内缩减了停顿的时间）

#### 2022-11-26
1. 网页元素有所变动，已做更改

2. 现在新增一个选项，已做填写

![new](https://user-images.githubusercontent.com/112788213/204083648-9d61e483-721d-4665-89e6-a3b5e4d510cb.png)

#### 2022-10-15
1. 现在登陆界面新增窗口已做修改

![截图](https://user-images.githubusercontent.com/112788213/195988235-f6f472b3-710e-497a-b07a-e8b37e074864.png)

2. 网页元素有所变动，已经更改了元素正确的id位置

3. 优化了前面的教程，使教程更易看懂

#### 2022-10-06
1. 现在强制要提交行程码的截图。本脚本完全适用行程码截图！！！

具体思路无法细说，但是目前能提供东西都在第五点中

2. 网络元素变动，已经更改了元素正确的id位置

3. 怎么才过了俩天又要更新（生气！！！）

#### 2022-10-04
1. 优化了一下代码，使其更加适应现在的环境

2. 提供了行程码的思路

#### 2022-09-22
1. 学校新增是否感染过新冠病毒，网页元素有所变多，已经更改元素id位置

2. 学校新增：若前一天未填报每日一报，则需上传行程码截图，因此上了带传行程码版本，但行程码截图如何获取需自行学习努力，目前这里仅提供完全合规合法的行程码网页  https://xc.caict.ac.cn/#/login 至于后续如何获取截图，请各位自行学习，八仙过海、各显神通（太刑了）
