微信lomo打印机
==============

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
   4. 输入vncserver :1，并设置密码
   5. 使用ifconfig查看Raspberry Pi的ip地址
   6. 使用vnc viewer连接vnc://192.168.xxx.xxx:5901，并输入刚才设置的密码(为什么是5901？因为vnc默认端口是5900，刚才输入的vncserver :1表示端口号+1）
   7. 现在应该可以看到RPi的桌面了
9. 安装打印机驱动
   1. 打开控制台
   2. 安装cups驱动。输入sudo apt-get install cups
   3. 安装cups-pdf虚拟pdf打印机（可选，我只是用它来调试）。sudo apt-get install cups-pdf
   4. 将打印机管理程序lpadmin的权限赋给用户pi。输入sudo usermod -a -G lpadmin pi
   5. 用浏览器访问RPi的631端口，打开打印机配置页面。此时只能用RPi自己的浏览器访问，因为它默认不接受外来的连接。如果想用PC访问需要修改/etc/cups/cupsd.conf文件。详见此链接http://www.howtogeek.com/169679/how-to-add-a-printer-to-your-raspberry-pi-or-other-linux-computer/
   6. 连接打印机到Raspberry Pi的USB口
   7. 在administrator标签页点击add printer
   8. 输入用户名pi，密码raspberry
   9. 选择你的打印机
10. 下载wechat-printer代码。

