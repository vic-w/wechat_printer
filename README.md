微信lomo打印机
==============

材料
----
1. 树莓派 Raspberry Pi 512M B型，214￥
2. 8G SD card, 29￥
3. HP Deskjet 1010 printer （含墨盒），淘宝上最便宜的一款彩色喷墨打印机，174￥
4. 8寸1024*768 液晶屏显示器套件HDMI+VGA+2AV，278￥
5. 一条短hdmi线，5￥
6. A7相纸100张，10￥
7. 8cm散热风扇5V，10￥
8. 电源插板，变压器，一个大纸箱，30￥

总成本750￥。0_0算一算还是挺贵的啊。

安装
----
1. 安装Win32DiskImager
2. 下载RASPBIAN的image。http://www.raspberrypi.org/downloads/
3. 使用Win32DiskImager将Raspbian的镜像灌入SD卡
4. 连接显示器和键盘。接上电源。启动数秒后进入Raspberry  Pi Software Configuration Tool。选择3，Enable Boot to Desktop/Scratch。再选择第二项：Desktop Log in as user 'pi' at the graphical desktop。选择finish退出。然后reboot。
5. 这次启动直接进入了桌面
6. 连接网线。或插入无线网卡，输入密码，连入互联网。
7. （可选）使用电脑通过ssh来操作RPi
   1. 使用ifconfig查看RPi的ip地址
   2. 打开电脑的控制台，输入ssh pi@192.168.xxx.xxx（RPi的ip）
   3. 输入密码：raspberry（这是RPi的默认登录密码）
   4. 登陆成功。现在可以用电脑的控制台来输入命令了控制RPi了。
8. 接下来为了使用方便，安装远程桌面来控制RPi。
   1. 打开控制台
   2. 更新apt-get。sudo apt-get update
   3. 安装vnc服务。sudo apt-get install tightvncserver
   4. 输入vncserver :1，并设置密码(如果忘记了这个密码，可以用vncpasswd来重设。然后service vncserver restart重启服务）
   5. 使用ifconfig查看Raspberry Pi的ip地址
   6. 使用vnc viewer连接vnc://192.168.xxx.xxx:5901，并输入刚才设置的密码(为什么是5901？因为vnc默认端口是5900，刚才输入的vncserver :1表示端口号+1）
   7. 现在应该可以看到RPi的桌面了
9. 安装打印机驱动
   1. 打开控制台
   2. 安装cups驱动。输入sudo apt-get install cups
   3. 安装cups-pdf虚拟pdf打印机（可选，我只是用它来调试）。sudo apt-get install cups-pdf
   4. 将打印机管理程序lpadmin的权限赋给用户pi。输入sudo usermod -a -G lpadmin pi
   5. 用浏览器访问RPi的631端口，打开打印机配置页面。此时只能用RPi自己的浏览器访问，因为它默认不接受外来的连接。在administration页面勾选”Allow remote administration“后可以用PC的浏览器来登录这个配置页面，这是可以关掉远程桌面，速度会快很多。
   6. 连接打印机到Raspberry Pi的USB口
   7. 在administrator标签页点击add printer (这里开始网页反应比较慢，需耐心等待）
   8. 输入用户名pi，密码raspberry
   9. 选择你的打印机。由于我的打印机型号是HP Deskjet，         默认的list上没有这款机型，所以我还需要安装hplip的最新版本（HP打印机的开源驱动程序）。
   10. 接下来设置打印机默认纸张大小为A6。（LOMO照片尺寸为A7，只有A6的一半大小，但打印机最小只能支持A6）
10. （可选）安装hplip
   1. 在http://hplipopensource.com/ 下载hplip的最新版安装包。我安装时最新版是3.15.2。需要说明的是Rasbian系统里已经自带了一个hplip，但不是最新版本，而且用apt-get upgrade升级后仍然不是最新版，所以需要从官网下载安装包。另外，下载时要选择tar格式的安装文件，不要下载sh后缀的那个，后者在RPi上编译时会死机。
   2. 参照这篇文章进行安装：http://hplipopensource.com/hplip-web/install/manual/distros/debian.html
   3. 安装完成后，就应该可以在驱动列表里找到HP Deskjet 1010了。
11. 下载wechat-printer代码。
   1. 安装git。sudo apt-get install git
   2. 下载代码。git clone https://github.com/vic-w/wechat_printer.git
   3. 运行代码。python wechat_printer/printer.py
   4. 至此微信打印机终端配置完成。

