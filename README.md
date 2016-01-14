# Welcome to use JTT808

## How to add a new function on jtt808

#####step01
Put your new message id on the /conf/protocols.py
#####step02
Write your response function on the /app/views.py
#####step03
Install your function let the system know ,so go /app/urls.py
#####step04
Let the system know you have new function , set it on /process_signal/payload.py

## How to Resolution each message content according the JTT808 protocols
#####step01
Write your app/split.py according the your length of each field
#####step02
Write your app/admin.py and if you need to do some covert with data type
#####step03
Call your have write from your step01 / step02 class! Just like our position function

## For more
[How it work](http://blog.csdn.net/u011767611/article/details/50497709)
