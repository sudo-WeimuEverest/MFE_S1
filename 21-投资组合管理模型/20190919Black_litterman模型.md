## Black-Litterman模型

“中庸之道”

### 基本假设

> 所有投资者有相同的信息和观点，按照马科维茨的最优组合理论进行股票选择，当前预期收益率及发行量使得市场恰好出清，供需平衡

### 实践步骤

1. 判断市场的对超额收益的看法---求均衡市场下各种资产的隐含超额收益率
   $$
   max(\omega^{T}\mu - \frac{\lambda}{2}\omega^{T}\Sigma \omega)
   $$
   

   马科维茨是求权重

- Black反向操作，权重使用市场市值

$$
\Pi = \lambda \Sigma \omega_{mkt}
$$

> 投资者的风险厌恶系数 $\lambda$ 需要根据经验指定

- 得到市场预期
  $$
  \Pi = \mu + \epsilon_{\Pi}
  $$

  $$
  \epsilon_{\Pi} \sim N(0, \tau\Sigma)
  $$


（从CAPM出发也可以得到相应的均衡组合，求得市场风险价格）

New Combined Return Vector: $E[R] = [(\tau\Sigma)^{-1}+P'\Omega^{-1}P]^{-1}[(\tau\Sigma)^{-1}\Pi+P'\Omega^{-1}Q]$

> $\tau$ 代表了市场隐含收益率 $\Pi$ 相对于期望收益率 $\mu$ 的误差
> $$
> \Pi = \mu + \epsilon \quad \epsilon \sim N(0, \tau \Sigma) 
> $$
> 

1. 允许投资者对期望收益的不同看法（但是有基准的市场收益率）

   可以只针对个别的资产有其特殊观点，如“我预期A的收益将超过B的收益”，“我预期明年资产C的收益将达到Y” 

   核心假设如下：
   $$
   q = P \mu + \epsilon_{q}
   $$

   $$
   \epsilon_{q} \sim N(0, \Omega)
   $$

   q是K维向量，P是K * N，K是投资者观点个数

   ![1569135365553](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\1569135365553.png)

2. 融合预期
   $$
   y = X\mu + \epsilon
   $$

   由GLS可得到收益率的估计

   ![1569136358275](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\1569136358275.png)

3. 放入马科维茨的最优化模型，对最优权重进行相应调整

   权重变化主要集中在投资者观点与均衡观点有偏差的部分，没有观点的部分资产的权重有稳定性

   ![1569139069840](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\1569139069840.png)

### 优点

- 吸收了市场的观点，克服了不稳定性
- 内在一致性的框架
- 更多依赖于便于观察可估的信息
- 便于辨认和理解的权衡因素

### 拓展

- 融入多因子模型
  $$
  R_{i} = \alpha_{i} + F \beta_{i} + \epsilon_{i}
  $$
  

$$
q_{i} = \alpha_{i} + F\beta_{i}
$$

$$
\omega_{i} = var(\epsilon_{i})
$$

​	随后应用于BL模型

- 融入动量策略

> 动量策略的基本想法是买入表现好的股票，卖出表现差的股票，期望同样的趋势在不久的未来还会延续
>
> Returns to Buying winners and selling losers: implications for Stock market efficiency

- Wing Cheung---扩增BL模型