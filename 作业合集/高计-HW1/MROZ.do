

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




