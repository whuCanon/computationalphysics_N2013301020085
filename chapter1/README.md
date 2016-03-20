
#Population Growth Model  

##摘要  
本次作业挑选`1.6-人口增长问题`作为作业内容，给出了针对人口增长问题的常微分方程的近似解决方案。

##背景介绍  
对于人口增长模型一般使用以下公式描述  
![formula1](https://raw.githubusercontent.com/whuCanon/computationalphysics_N2013301020085/master/chapter1/Resource/formula1.png)  
其中N为人口数，aN对应人口增长，bN<sup>2</sup>对应人口死亡。当人口数量很大时，由于资源有限的原因导致人口存在上限，所以人口消减项由N<sup>2</sup>影响，当b=0时，人口呈指数增长。

##正文  

###实现原理  

####常微分方程的数值近似解   
人口增长模型对应的常微分方程可写成   
![formula2](https://raw.githubusercontent.com/whuCanon/computationalphysics_N2013301020085/master/chapter1/Resource/formula2.png)  
若取dt为某一足够小的近似值，当已知N的初值N(t<sub>0</sub>)后多次迭代，便可得到之后所有的数值近似解。  

####参数设置  
- 对于此方程，需要设置的参数有a、b、N(t<sub>0</sub>)、dt、end_t。  
- 对于a、b、N(t<sub>0</sub>)容易看出参数a为人口增长系数，建议的值在0.01-100之间；参数b为人口消减系数，建议的值在0-10之间。参数a、b和人口初值N(t<sub>0</sub>)均可通过用户输入方式得到，且数值类型为浮点数，因为人口初值可以科学计数法方式设定。  
- 对于end_t，通过考察方程可发现，当N=a/b时，dN=0，即人口数N将无限趋于a/b，为了显示适当比例的人口增长曲线图，end_t需要根据输入的a、b、N(t<sub>0</sub>)来决定。又当处于b=0的极端情况时，人口数将指数增长，这将可能超出matplotlib能接受的最大数值，故需要对此情况做特殊处理。  
- 对于dt，由于end_t的范围变动很大，故设置一个固定的计算次数而让dt的值由计算次数决定。  

####作图工具  
本次作业使用作图工具为matplotlib库。

###程序实现  

python源码地址：[population_model](https://raw.githubusercontent.com/whuCanon/computationalphysics_N2013301020085/master/chapter1/population_model.py "population model")

###结果分析  

-  当a=0.1,b=0.001,N(t_0)=2时，人口增长曲线如图，可以推出，当N=a/b时，人口增长出现拐点  
![](https://raw.githubusercontent.com/whuCanon/computationalphysics_N2013301020085/master/chapter1/Resource/population_model_1.png)  

-  当a=10,b=3,N(t<sub>0</sub>)=1000时，人口迅速下降后趋于一稳定值  
![](https://raw.githubusercontent.com/whuCanon/computationalphysics_N2013301020085/master/chapter1/Resource/population_model_2.png)

##结论  

由以上分析可知，当资源数量有限且为一常量时，人口数量将趋近于定值a/b。

##致谢  
