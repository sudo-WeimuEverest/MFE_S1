*导入数据
import excel C:\Users\Lenovo\Desktop\stocks.xlsx, firstrow clear

*定义变量的标签
label var r1 "贵州茅台"
label var r2 "华兰生物"
label var r3 "复兴医药"
label var r4 "万科A"
label var r5 "招商银行"
label var r6 "宁沪高速"
label var r7 "中国平安"
label var r8 "新城控股"
label var r9 "春秋航空"
label var r10 "福成股份"

result = pca r1-r10 /*主成分分析*/
outreg2 using result, drop(result) replace


