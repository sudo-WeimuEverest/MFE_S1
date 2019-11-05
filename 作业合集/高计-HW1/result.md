```
*声明存储路径
cd "C:\Users\Lenovo\Desktop\MROZ"
*导入数据
use "MROZ.dta",clear
*保留前428个数据
keep in 1/428 
*(1)obtain the OLSE
reg lwage exper expersq educ age kidslt6 kidsge6
*(4)test
test exper=expersq=educ=age=kidslt6=kidsge6
outreg2 using result
```

运行结果如下：

（1）回归结果

![1572146025289](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\1572146025289.png)

（4）检验结果

![1572146086608](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\1572146086608.png)