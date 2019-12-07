Materials Studio作为一款成功的商业化计算软件，提供了非常人性化的图形界面，用来建模、计算和查看结果。但有个缺点是什么东西都需要你用鼠标点来点去（当然更大的缺点是它像个黑匣子，你不知道它计算的过程），这对习惯了在Linux下用脚本提交批量任务的老手来说实在是太boring了：）好在，windows还保留了一个古老的功能——批处理（batch processing），也就是.bat文件，双击可以直接运行一系列的命令。

 

废话少说，下面以CASTEP为例，说明Materials Studio批处理计算的方法：

 

首先做好输入文件，想必大家都会，就是不点Run，点Files，save files。

 

其次，编写批处理文件（可先用文本文档写，另存为.bat文件），该文件位置不限。例如，要计算两个任务，编写批处理文件如下：

例子：本人试验过的一个Ni.bat批处理文件的内容如下：

@echo on 

cd D:"Materials Studio Projects""Ni_Fe_TiC Files"Documents"Ni CASTEP Energy"
call C:"Program Files"Accelrys"Materials Studio 5.0"etcCASTEPbinRunCASTEP -np 2 Ni

cd D:"Materials Studio Projects""Ni_Fe_TiC Files"Documents"Ni CASTEP Energy (2)"
call C:"Program Files"Accelrys"Materials Studio 5.0"etcCASTEPbinRunCASTEP -np 2 Ni

pause


说明： 
第一句，@echo on ，目的是显示执行后面的命令，可用@echo off关闭，无所谓。

第二句，D:"Materials Studio Projects""Ni_Fe_TiC Files"Documents"Ni CASTEP Energy"，进入到Ni这个任务输入文件所在的目录，注意文件夹带空格的要整体用""引起来，具体位置当然看个人而定。

第三句，C:"Program Files"Accelrys"Materials Studio 5.0"etcCASTEPbinRunCASTEP -np 2 Ni，调用RunCASTEP程序用2个核跑任务Ni，后面的类推。


  这里要注意的是，这个目录是MS默认的安装路径，如果不是默认安装要做相应改正，这个大家找找看就是了。在Win下，虽然有RunCASTEP.bat，RunCASTEP.Readme，但是在批处理调用的时候不要带上扩展名，直接用RunCASTEP即可。同样，任务名也是这样处理的，依照保存在Ni CASTEP Energy文件夹中的任务名决定。

最后一句，pause，直接执行计算完后窗口会直接关闭，用pause语句，计算完后出现“按任意键继续...”，可以使窗口保持打开状态，当然此时任务也都已经算完了，窗口打开与否对任务没有影响、

OK，找到这个批处理文件，双击执行。