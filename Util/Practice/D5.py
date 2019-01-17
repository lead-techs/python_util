#题目：输入三个整数x,y,z，请把这三个数由小到大输出。
#定义一个空数组
numbers = []
#循环遍历，下面的4是控制循环次数
for i in range(4):
    if i > 0:
        x = int(input(f"请输入第{i}个整数："))
        #把用户输入的数传递到定义的numbers数组中
        numbers.append(x)
#输出未排序之前的数字
print(f"未排序之前是：{numbers}")
#让数字从小到大排序
print("由小到大排序完后是：",sorted(numbers))
#让数字从大到小排序
numbers.sort(reverse=True)
print(f"由大到小排序完后是：{numbers}")
#输出最大值
print(f"最大数是：{max(numbers)}")
#输出最小值
print(f"最小数是：{min(numbers)}")