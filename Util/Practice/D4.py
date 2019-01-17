#输入某年某月某日，判断这一天是这一年的第几天？
dat = input('请输入某年某月某日，格式为 yyyy-mm-dd ：')
y = int(dat[0:4])  #获取年份
m = int(dat[5:7])  #获取月份
d = int(dat[8:])  #获取日

ly = False

if y%100 == 0:  #若年份能被100整除
    if y%400 == 0:  #且能被400整除
        ly = True  #则是闰年
    else:
        ly = False
elif y%4 == 0:  #其它情况下，若能被4整除
    ly = True  #则为闰年
else:
    ly = False

if ly == True:  #若为闰年，则2月份有29天
    ms = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    ms = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = 0
for i in range(1, 13):  #从1到12逐一判断，以确定月份
    if i == m:
        for j in range(i-1):  #确定月份i之后，则将ms列表中的前i-1项相加
            days += ms[j]
        print('%s是该年份的第%s天。' % (dat, (days + d))) #最后再加上“日”，即是答案