# project
bluetooth one connect multi use raspberry pi3 and HC-05
---------------------------------------------------------
首先設定HC-05的AT cammand use ble.ino

AT command
AT+ROLE = 0
AT+UART = 115200,0,0
AT+NAME = one
AT+PSWD = 1111
AT+COMDE = 0

----------------------------------------------------------
啟用raspberry pi3 
下載藍牙套件
sudo apt-get update
sudo apt-get install bluetooth bluez python bluez
sudo apt-get upgrade
下載完畢後
hciconfig 查看藍芽配置訊息
sudo bluetoothctl 啟用藍牙
agent on
default-agent
scan on 掃描周遭藍芽裝置
pair 藍牙位址
ctrl+z 跳出
sudo rfcomm connect 1 藍牙位址 &
連接成功後，raspberry 的/dev內會創建一個rfcomm1的藍牙串口

接著使用 rasp2blue.py 便可連接藍芽裝置
重複做即可一對多接藍牙
