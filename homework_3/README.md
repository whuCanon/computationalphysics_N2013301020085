#Homework 3 Description     

##摘要    
本文介绍了作业程序设计的想法、原理和具体实现，实现过程中考虑到具体需求和发展需要，设计了一个基于命令行的微型伪图形用户接口。  

##背景介绍    
对于本次作业level3，考虑到要基于命令行支持动画效果，所以必须刷新和动态改变字符位置；又要支持旋转操作，则必须创建一个虚拟屏幕面板来模拟像素点操作。于是想到通过创建一个基于命令行的迷你GUI来实现。      

##正文    

###实现原理     

####虚拟屏幕的实现     

-  要实现虚拟屏幕则必须定义一个虚拟屏幕类`Canvas`，用于创建其对象；    
- 屏幕自然需要宽、高和像素属性，其中宽`width`和高`height`通过用户创建对象时输入；像素为一字典类型变量`tupMatrix`，键为一二元组表示x、y坐标，值为字符表示要在(x, y)显示的字符，以向右为x轴方向，向下为y轴方向。      

####将虚拟屏幕显示在命令行界面     

- 为Canvas类创建一个函数`draw()`，该函数从(0, 0)到(width, height)顺序遍历所有点，这里可以利用print函数自动换行的规则。在打印时每行创建一临时变量`tmp_str = ""`存储字符串，若该点存在字符(即`tupMatrix[(x, y)].has_key() == True`)则将字符添加`tmp_str += tupMatrix[(x, y)]`，否则存入空格；    
- 每当遍历完一行后，执行`print tmp_str` 打印输出；    
- 遍历所有行，打印整个虚拟屏幕。    

####在虚拟屏幕上画图写字    
    
- 首先需要将要画的东西转换成字模形式，转换软件推荐ASCII Generator 2；    
- 为Canvas类创建一个函数`draw_image(text, pos)`，该函数接收所要显示的字符串和显示的位置，然后以该位置为作图打印的原点，依次将字符串中的字符存入像素字典，规定当字符为特定字符或者换行符时，基于作图原点进行换行处理；    
- **若要支持旋转功能，则必须在draw_image函数中增加可选参数`angle ＝ 0`，然后在Canvas类中定义旋转函数rotate并在draw_image函数中调用。要实现旋转函数首先需要在draw_image函数中根据输入的字符串text来确定图像的宽`image_width`和高`image_height`，然后将宽高以及位置信息和角度传入rotate函数来求出图像在虚拟屏幕中的中心点，由此可求得图像每点基于图像中心点旋转后的坐标，然后将旋转后的坐标更新至像素字典tupMatrix即可。**     

####动画效果的实现    
- 通过以上方法只能得到静态的图像，要实现动态效果需要使用循环语句不断刷新终端，于是在类中定义update函数，该函数先调用系统终端清屏函数进行清屏，然后调用draw函数将虚拟屏幕打印至终端,再将像素信息清空，等待下次输入。再通过在执行代码中不断调用`canvas.draw_*(*)`和`update()`来达到刷新屏幕的目的；   
- 为了防止屏幕闪烁，同时节省CPU资源，需要为Canvas类设置屏幕刷新率`REFRESH_RATE`，并在update函数中调用`time.sleep(REFRESH_RATE)`函数来延迟刷新屏幕。   

####举例说明    
	import math  
	import MiniGUI  
	  
	PAINTING_WIDTH = 100  # 屏幕宽度，100个字符宽度  
	PAINTING_HEIGHT = 30  
	MOVING_SPEED = [1, 1] # 移动速度 
	ROTATE_SPEED = 0.2    # 旋转速度
	  
	pos = [0, 0]  # 物体的位置  
	angle = 0     # 物体的角度  
	canvas = MiniGUI.Canvas(PAINTING_WIDTH, PAINTING_HEIGHT)  # 创建虚拟屏幕  
	while True:  
	    pos[0] += MOVING_SPEED[0]  # 更新位置  
	    pos[1] += MOVING_SPEED[1]  
	    pos[0] %= PAINTING_WIDTH  
	    pos[1] %= PAINTING_HEIGHT  
	    angle += ROTATE_SPEEN      # 更新角度  
	    angle %= math.pi * 2  
	    canvas.draw_image("############", pos, angle)  # 将显示信息'画'至虚拟屏幕  
	    update()  # 打印虚拟屏幕  

###程序实现  

####源代码  
 
[MiniGUI.py](https://raw.githubusercontent.com/whuCanon/computationalphysics_N2013301020085/master/homework_3/MiniGUI.py)  
[homework_3.py](https://raw.githubusercontent.com/whuCanon/computationalphysics_N2013301020085/master/homework_3/homework_3.py)  

####运行方法  

将两文件放在同一文件夹中，命令行进入该文件夹，最大化命令行窗口后`python homework_3.py`运行
Windows用户请修改`MiniGUI.py`下的`os.sys('clear')`为`os.sys('cls')`后运行。  

##结论  

由于命令行环境下的字符行距和列距相差较大，故旋转实现起来效果不太好；  另外没有找到命令行下的键盘事件接口，无法做进一步的发展，希望老师或者知道的同学给予指导。   

##致谢  

本次作业全部原创（感谢Ron89学长对doc格式的建议以及找出单词的错误）  
欢迎参考借鉴~互相帮助~  
