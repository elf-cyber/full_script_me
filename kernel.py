import colorama 
import json
import requests
import os , time , random

while True:    
    print(colorama.Fore.GREEN+colorama.Back.BLACK+colorama.Style.DIM+'[=====>               ]25%')
    time.sleep(2)
    os.system('clear')
    print(colorama.Fore.GREEN+colorama.Back.BLACK+colorama.Style.DIM+'[==========>          ]50%')
    time.sleep(2)
    
    os.system('clear')
    print(colorama.Fore.GREEN+colorama.Back.BLACK+colorama.Style.DIM+'[===============>     ]75%')
    time.sleep(2)
    
    os.system('clear')
    print(colorama.Fore.GREEN+colorama.Back.BLACK+colorama.Style.DIM+'[====================>]100%')
    time.sleep(2)
    os.system('clear')
    print('loding..!')
    a = random.randint(1, 2)
    b = str(a)
    time.sleep(5)
    break
    
if os.name == 'nt':
    
    os.system('cls')
else:
    os.system('clear')
    
print('loding...!')
time.sleep(6)

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
    
def bunner():
    a ='''
      
      wWw W  W    wWw        oo_    wWw    c  c  wWw  wWw()_()wW  Ww(o)__(o)wWw  wWw       c  cwWw  wWw___   wWw()_()  
      (O)(O)(O)   (O)_      /  _)-< (O)_   (OO)  (O)  (O)(O o)(O)(O)(__  __)(O)  (O)       (OO)(O)  (O|___)__(O)(O o)  
      / __)||     / __)     \__ `.  / __),'.--.) / )  ( \ |^_\ (..)   (  )  ( \  / )     ,'.--.| \  / |O)(O) / __)^_\  
     / (   | \   / (           `. |/ (  / //_|_\/ /    \ \|(_)) ||     )(    \ \/ /     / //_|_\\ \/ //  _\ / (  |(_)) 
    (  _)  |  `.(  _)          _| (  _) | \___  | \____/ ||  / _||_   (  )    \o /      | \___   \o / | |_)|  _) |  /  
     \ \_ (.-.__) /         ,-'   |\ \_ '.    ) '. `--' .`)|\\(_/\_)   )/    _/ /       '.    ) _/ /  | |_))\ \_ )|\\  
      \__) `-'  )/         (_..--'  \__)  `-.'    `-..-' (/  \)       (     (_.'          `-.' (_.'   (.'-'  \__|/  \      
         
         
         ''' 
    i = random.randint(1,10)

    if i == 1:
        print(colorama.Fore.GREEN+a)
    if i == 2: 
        print(colorama.Fore.RED+colorama.Cursor.BACK()+a)
    if i ==3 :
        print(colorama.Fore.BLUE+colorama.Style.DIM+a)    
    if i == 4:
        print(colorama.Fore.CYAN+colorama.Cursor.BACK(a))
    if i == 5:
        print(colorama.Fore.YELLOW+a)
    if i == 6:
        print(colorama.Fore.LIGHTWHITE_EX+colorama.Style.DIM+colorama.Cursor.BACK(a))
    if i == 7:
        print(colorama.Fore.MAGENTA+a)
    if i == 8:
        print(colorama.Fore.LIGHTCYAN_EX+a)    
    if i == 9:
        print(colorama.Fore.CYAN+colorama.Style.DIM+a)
    if i ==10:
        print(colorama.Fore.LIGHTBLACK_EX+colorama.Style.DIM+a)
bunner()
print('loding...!')
time.sleep(6)
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

if os.name =='nt':
    print("BY")
else:    

    os.system('termux-open-url https://t.me/elf_security_cyber')    
print(colorama.Fore.RED+colorama.Back.BLACK+colorama.Style.DIM+'''
\t   +-----------------------------------------------------------------------+
\t   |                              _    __                                  |
\t   |                        ___  | |  / _|                                 |
\t   |                       / _ \ | | | |_                                  |
\t   |                      |  __/ | | |  _|                                 |
\t   |                      \__\__ |_|_| |                                   |
\t   |                     _________________                                 |
\t   | +---------------------------+                                         |
\t   |  [??]model---------------[-]-|                                         |
\t   |  [&]fake kart-----------[1]-|                                         |
\t   |  [&]font name-----------[2]-|                                         |
\t   |  [&]info arz------------[3]-|                                         |
\t   |  [&]bio telegram--------[4]-|                                         |
\t   |  [&]info channel--------[5]-|                                         |
\t   |  [&]info insta----------[6]-|                                         |
\t   |  [&]info ip-------------[7]-|                                         |
\t   |  [&]database irancell---[8]-|                                         |
\t   |  [&]info tavalod--------[9]-|                                         |
\t   |  [&]info weather--------[10]|                                         |
\t   |  [&1]proxy http---------[11]|                                         |
\t   |  [&]proxy iran----------[12]|                                         |
\t   |  [&]proxy telegram------[13]|                                         |
\t   |  [&]zed phishing--------[14]|                                         |
\t   |  [&]tabir khab----------[15]|                                         |
\t   |  [&]license nod32-------[16]|                                         |
\t   |  [&]search music--------[17]|                                         |
\t   |  [&]korona--------------[18]|                                         |
\t   |  [&]fake info-----------[19]|                                         |
\t   |  [&]timer---------------[20]|                                         |
\t   |  [&]info facebook-------[21]|                                         |
\t   |  [&]info facebook userid[22]|                                         |
\t   | +---------------------------+                                         |
\t   |  [#]updateing....                                                     |
\t   +-----------------------------------------------------------------------+
    ''')


    
    

def fake_info():
    b = input(colorama.Fore.GREEN+'enter the city : ')
    a = requests.get('https://meysam72.tk/api/fake.php?name='+b)
    res = a.json()
    print(colorama.Fore.CYAN+'{\n"craeted by":"@e_l_f_6_6_6"'+json.dumps(res, indent=4, separators=(" , ", " ==> :  ")))
    print('''\n\n"my channel":"@elf_security_cyber"\n\n\n       }   ''')   
    res1 = input('save to sdcard and new file? ')
    if res1 == 'yes':
        os.chdir('/sdcard')
        rxt3 = open("fakeinfo.txt","w+")     
        p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
        for i in range(1):
            rxt3.write(res+'\n'+p)
            rxt3.close()
    else:
           txt = open("fakeinfo.txt","a")
           for i in range(1):
               txt.write(res+"\n")
               txt.close()

def korona():
    a = input (colorama.Fore.GREEN+'enter the country : ')

    x = requests.get('https://api.codebazan.ir/corona/?type=country&country='+a)
    a = x.json()
    
    print(colorama.Fore.CYAN+"[+]"+json.dumps(a, indent=4, separators=(" , ", " ==> :  ")))
    
    res= str(a)
    res1 = input('save to sdcard and new file? ')
    if res1 == 'yes':    
        os.chdir('/sdcard')
        rxt3 = open("corona.txt","w+")     
        p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
        for i in range(1):
            rxt3.write(res+'\n'+p)
            rxt3.close()
    else:
           p = "############################################################"   
           txt = open("corona.txt","a")
           for i in range(1):
               txt.write(res+"\n"+p)
               txt.close()
      
def music():
    a = input('enter the name music : ')

    respons = requests.get('http://api.codebazan.ir/music/?type=search&query='+a+'page=1')

    a=respons.json()
    res= str(a)
    print(colorama.Fore.CYAN+'[+]'+json.dumps(respons.json(), indent=4, separators=(" , ", " ==> :  ")))   
    res1 = input('save to sdcard and new file? ')
    if res1 == 'yes':
        os.chdir('/sdcard')
        rxt3 = open("music.txt","w+")     
        p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
        for i in range(1):
            rxt3.write(res+'\n'+p)
            rxt3.close()
    else:
           p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   
           txt = open("music.txt","a")
           for i in range(1):
               txt.write(res+"\n"+p)
               txt.close()
   
def nod32():
    a = requests.get('https://meysam72.tk/api/nod32.php')

    a=a.json()

    print(colorama.Fore.CYAN+'[+]'+json.dumps(a.json(), indent=4, separators=(" , ", " ==> :  ")))
    res= str(a)
    res1 = input('save to sdcard and new file? ')
    if res1 == 'yes':
        os.chdir('/sdcard')
        rxt3 = open("proxy.txt","w+")     
        p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
        for i in range(1):
            rxt3.write(res+'\n'+p)
            rxt3.close()
    else:
           p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   
           txt = open("proxy.txt","a")
           for i in range(1):
               txt.write(res+"\n"+p)
               txt.close()
    
    
    
    
def tabir_khab():
    a = input('enter the name :')
    respons = requests.put('http://api.codebazan.ir/mtproto/json/'+a)
    a=respons.json()  
    print(colorama.Fore.CYAN+'[+]'+json.dumps(respons.json(), indent=4, separators=(" , ", " ==> :  ")))
    res= str(a)
    res1 = input('save to sdcard and new file? ')
    if res1 == 'yes':
        os.chdir('/sdcard')
        rxt3 = open("proxy_telgram.txt","w+")     
        p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
        for i in range(1):
            rxt3.write(res+'\n'+p)
            rxt3.close()
    else:
           p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   
           txt = open("proxy_telgram.txt","a")
           for i in range(1):
               txt.write(res+"\n"+p)
               txt.close()
    
    
    

def arz():
       a = requests.get('https://meysam72.tk/api/crypto.php')
       a.encoding = 'utf-8'
       a=a.json()
       print(colorama.Fore.CYAN+'[+]'+json.dumps(a.json(), indent=4, separators=(" , ", " ==> :  ")))
       res= str(a)
       res1 = input('save to sdcard and new file? ')
       if res1 == 'yes':
           os.chdir('/sdcard')
           rxt3 = open("info_arz.txt","w+")     
           p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
           for i in range(1):
               rxt3.write(res+'\n'+p)
               rxt3.close()
       else:
              p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   
              txt = open("info_arz.txt","a")
              for i in range(1):
                  txt.write(res+"\n"+p)
                  txt.close()
       
       
       
def bio():
    a = input('enter the username : ')

    b = requests.get('https://api.codebazan.ir/telegram/?type=user&username='+a)
    a.encoding = 'utf-8'
    a=b.json()
    print(colorama.Fore.CYAN+'[+]'+json.dumps(b.json(), indent=4, separators=(" , ", " ==> :  ")))
    res= str(a)          
    res1 = input('save to sdcard and new file? ')
    if res1 == 'yes':
        os.chdir('/sdcard')
        rxt3 = open("proxy_telegram.txt","w+")     
        p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
        for i in range(1):
                  rxt3.write(res+'\n'+p)
                  rxt3.close()
    else:
                 p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   
                 txt = open("fakeinfo.txt","a")
                 for i in range(1):
                     txt.write(res+"\n"+p)
                     txt.close()
          
          
          
def kart_get():
         x = requests.get('https://api.codebazan.ir/visa-card/')
         a= x.json()
         x.encoding = 'utf-8'
         print(colorama.Fore.CYAN+'[+]'+json.dumps(x.json(), indent=4, separators=(" , ", " ==> :  ")))
         res= str(a)
         res1 = input('save to sdcard and new file? ')
         if res1 == 'yes':
             os.chdir('/sdcard')
             rxt3 = open("fake_kart.txt","w+")     
             p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
             for i in range(1):
                 rxt3.write(res+'\n'+p)
                 rxt3.close()
         else:
                p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   
                txt = open("fake_kart.txt","a")
                for i in range(1):
                    txt.write(res+"\n"+p)
                    txt.close()
         
         
               
def font():
         a = input('enter the name for font : ')

         respons = requests.get('https://api.codebazan.ir/font/?text='+a)
         respons.encoding = 'utf-8'
         a=respons.json()
         res= str(a)
         print(colorama.Fore.CYAN+'[+]'+json.dumps(respons.json(), indent=4, separators=(" , ", " ==> :  ")))
               
         res1 = input('save to sdcard and new file? ')
         if res1 == 'yes':
             os.chdir('/sdcard')
             rxt3 = open("FONT.txt","w+")     
             p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
             for i in range(1):
                 rxt3.write(res+'\n'+p)
                 rxt3.close()
         else:
                p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   
                txt = open("FONT.txt","a")
                for i in range(1):
                    txt.write(res+"\n"+p)
                    txt.close()
         
         

def channel():
        a = input('enter the username channel : ')

        b = requests.get('https://api.codebazan.ir/telegram/?type=challinfo&id='+a)
        a=b.json()
        b.encoding = 'utf-8'
        res= str(a)
        print(colorama.Fore.CYAN+'[+]'+json.dumps(b.json(), indent=4, separators=(" , ", " ==> :  ")))    
        res1 = input('save to sdcard and new file? ')
        if res1 == 'yes':
            os.chdir('/sdcard')
            rxt3 = open("info_channel_telgram.txt","w+")     
            p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
            for i in range(1):
                rxt3.write(res+'\n'+p)
                rxt3.close()
        else:
               p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   
               txt = open("info_channel_telgram.txt","a")
               for i in range(1):
                   txt.write(res+"\n"+p)
                   txt.close()
        
        
        
        
def info_insta():
        b = input(colorama.Fore.GREEN+'enter the username : ')
        a = requests.get('https://meysam72.tk/api/instainfo.php?url='+b)
        a.encoding = 'utf-8'
        print(colorama.Fore.CYAN+"off") 
def ip():
        a = input (colorama.Fore.GREEN+'enter the ip : ')
        x = requests.get('https://api.codebazan.ir/ipinfo/?ip='+a)
        
        x.encoding = 'utf-8'
        a=x.json()
        print(colorama.Fore.CYAN+'[+]'+json.dumps(x.json(), indent=4, separators=(" , ", " ==> :  ")))
        res= str(a)
        res1 = input('save to sdcard and new file? ')
        if res1 == 'yes':    
            os.chdir('/sdcard')
            rxt3 = open("ip.txt","w+")     
            p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
            for i in range(1):
                rxt3.write(res+'\n'+p)
                rxt3.close()
        else:
               p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   
               txt = open("ip.txt","a")
               for i in range(1):
                   txt.write(res+"\n"+p)
                   txt.close()      
              
def irancell():
        userID = input(colorama.Fore.GREEN+'enter the number {930,933,935,936,937,938,939} : ')
     

        response = requests.get('https://ziroapi.xyz/Apis/irancell/?phone='+userID)

        response.encoding = 'utf-8'
        a=response.json()
        print(colorama.Fore.CYAN+'[+]'+json.dumps(response.json(), indent=4, separators=(" , ", " ==> :  ")))
        res= str(a)
        res1 = input('save to sdcard and new file? ')
        if res1 == 'yes':
            os.chdir('/sdcard')
            rxt3 = open("database_irancell.txt","w+")     
            p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
            for i in range(1):
                rxt3.write(res+'\n'+p)
                rxt3.close()
        else:
               p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   
               txt = open("database_irancell.txt","a")
               for i in range(1):
                   txt.write(res+"\n"+p)
                   txt.close()
def tavalod():
        a1 = input(colorama.Fore.RESET+'enter the year :')
        b = input(colorama.Fore.GREEN+'enter the month : ')
        c = input(colorama.Fore.RED+'enter the day : ')

        a = requests.get('https://meysam72.tk/api/tavalod.php?year='+a1+'&month='+b+'&day='+c)
        a.encoding = 'utf-8'
        a=a.json()
        print(colorama.Fore.CYAN+'[+]'+json.dumps(a.json(), indent=4, separators=(" , ", " ==> :  ")))
        res= str(a)
        res1 = input('save to sdcard and new file? ')
        if res1 == 'yes':
            os.chdir('/sdcard')
            rxt3 = open("info_tavalod.txt","w+")     
            p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
            for i in range(1):
                rxt3.write(res+'\n'+p)
                rxt3.close()
        else:
               p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   
               txt = open("info_tavalod.txt","a")
               for i in range(1):
                   txt.write(res+"\n"+p)
                   txt.close()
def  weather():
        a = requests.get('https://api.openweathermap.org/data/2.5/weather?q=tehran&appid=afa35eb138c4bfb90705e36c96098f28')

        x=a.json()
        a.encoding = 'utf-8'
        print(colorama.Fore.CYAN+'[+]"'+json.dumps(a.json(), indent=4, separators=(" , ", " ==> :  ")))
        res= str(x)
        res1 = input('save to sdcard and new file? ')
        if res1 == 'yes':
            os.chdir('/sdcard')
            rxt3 = open("info_wether.txt","w+")     
            p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
            for i in range(1):
                rxt3.write(res+'\n'+p)
                rxt3.close()
        else:
               p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   
               txt = open("info_wether.txt","a")
               for i in range(1):
                   txt.write(res+"\n"+p)
                   txt.close()
              
def proxy():
        a = requests.get('https://meysam72.tk/api/proxyhttp.php')
        a.encoding = 'utf-8'
        a=a.text
        print(colorama.Fore.CYAN+'[+]'+json.dumps(a.json(), indent=4, separators=(" , ", " ==> :  ")))
        res= str(a)
        res1 = input('save to sdcard and new file? ')
        if res1 == 'yes':
            os.chdir('/sdcard')
            rxt3 = open("proxy_http.txt","w+")     
            p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
            for i in range(1):
                rxt3.write(res+'\n'+p)
                rxt3.close()
        else:
               p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   
               txt = open("proxy_http.txt","a")
               for i in range(1):
                   txt.write(res+"\n"+p)
                   txt.close()
        
def iran():
        a = requests.get('https://meysam72.tk/api/proxyiran.php')
        a.encoding = 'utf-8'
        a=a.text
        print(colorama.Fore.CYAN+'[+]'+json.dumps(a.json(), indent=4, separators=(" , ", " ==> :  ")))
        res= str(a)
        res1 = input('save to sdcard and new file? ')
        if res1 == 'yes':
            os.chdir('/sdcard')
            rxt3 = open("proxy_iran.txt","w+")     
            p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
            for i in range(1):
                rxt3.write(res+'\n'+p)
                rxt3.close()
        else:
               p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   
               txt = open("proxy_iran.txt","a")
               for i in range(1):
                   txt.write(res+"\n"+p)
                   txt.close()
        
def telegram():
        respons = requests.put('http://api.codebazan.ir/mtproto/json/')
        respons.encoding = 'utf-8' 
        a=respons.json()
        print(colorama.Fore.CYAN+'[+]'+json.dumps(respons.json(), indent=4, separators=(" , ", " ==> :  ")))
        res= str(a)
        res1 = input('save to sdcard and new file? ')
        if res1 == 'yes':
            os.chdir('/sdcard')
            rxt3 = open("proxy_telgram.txt","w+")     
            p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
            for i in range(1):
                rxt3.write(res+'\n'+p)
                rxt3.close()
        else:
               p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   
               txt = open("proxy_telgram.txt","a")
               for i in range(1):
                   txt.write(res+"\n"+p)
                   txt.close()
def phishing():
        a = input (colorama.Fore.GREEN+'enter the url : ')

        x = requests.get('https://api.codebazan.ir/fishinfo/index.php?link='+a)
        a= x.json()
        x.encoding = 'utf-8'
        print(colorama.Fore.CYAN+'[+]'+json.dumps(x.json(), indent=4, separators=(" , ", " ==> :  ")))
        res1 = input('save to sdcard and new file? ')
        res= str(a)
        if res1 == 'yes':
            os.chdir('/sdcard')
            rxt3 = open("fish_info.txt","w+")     
            p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
            for i in range(1):
                rxt3.write(res+'\n'+p)
                rxt3.close()
        else:
               p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   
               txt = open("fish_info.txt","a")
               for i in range(1):
                   txt.write(res+"\n"+p)
                   txt.close()
              
              
              
def timer():
    while True:
        a = time.localtime()
    
        c = time.strftime(colorama.Fore.CYAN+colorama.Back.BLACK+colorama.Style.BRIGHT+'\n\t"year is":"%Y\n\n\t\t"mon is":"%m\n\n\t\t\t"day is":"%d"\n\n\t\t"yaer day":"%j"\n\n\t"monts":"%b"\n\n\n\n"%Z"\n\n\n\n\t\t\t}' , a)
    
        b = time.strftime(colorama.Fore.CYAN+colorama.Back.BLACK+colorama.Style.BRIGHT+'{\n\n"time is":"%H:%M:%S"\n' , a )
    
        print(b , c)
        time.sleep(1)
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')              

def time_banner():
    
    a = time.localtime()

    c = time.strftime(colorama.Fore.CYAN+colorama.Back.BLACK+colorama.Style.BRIGHT+'\n\t"year is":"%Y\n\t\t"mon is":"%m\n\t\t\t"day is":"%d"\n\t\t"yaer day":"%j"\n\t"monts":"%b"\n\n\n\n"%Z"\n\n\n\n\t\t\t}' , a)

    b = time.strftime(colorama.Fore.CYAN+colorama.Back.BLACK+colorama.Style.BRIGHT+'{\n\n"time is":"%H:%M:%S"\n' , a )

    print(b , c)
    
    
def info_face_book():
    a = input('enter the number 9000000000: ')
    
    b = requests.get('https://api.town-host.ir/Facebook/api/?phone='+a)
    
    a= b.json()
    res= str(a)
    print(json.dumps(b.json(), indent=4 , separators=(":" , "==>")))
    res1 = input('save to sdcard and new file? ')
    if res1 == 'yes':    
        rxt3 = open("database_facebook_number.txt","w+")     
        p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
        for i in range(1):
            rxt3.write(res+'\n'+p)
            rxt3.close()
    else:
           p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   
           txt = open("database_facebook_number.txt","a")
           for i in range(1):
               txt.write(res+"\n"+p)
               txt.close()
def user_id_facebook():
        userID = input(colorama.Fore.GREEN+'[$]enter the user id facebook : ')
     
        response = requests.get('https://api.town-host.ir/Facebook/api/?id='+userID)

        response.encoding = 'utf-8'
        a= response.json()
        print(colorama.Fore.CYAN+'[+]'+json.dumps(response.json(), indent=4, separators=(" , ", " ==> :  ")))
        res= str(a)
        res1 = input('save to sdcard and new file? ')
        if res1 == 'yes':    
            rxt3 = open("databse_facebook_userid.txt","w+")     
            p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
            for i in range(1):
                rxt3.write(res+'\n'+p)
                rxt3.close()
        else:
               p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   
               txt = open("databse_facebook_userid.txt","a")
               for i in range(1):
                   txt.write(res+"\n"+p)
                   txt.close()
                   



                  
a1 = '1'
a2 = '2'
a3 = '3'
a4 = '4'
a5 = '5'
a6 = '6'
a7 = '7'
a8 = '8'
a9 = '9'
a10 = '10'
a11 = '11'
a12 = '12'
a13 = '13'
a14 = '14'
a15 = '15'
a16 = '16'
a17 = '17'
a18 = '18'
a19 = '19'
a20 = '20'
a21 = '21'
a22 = '22'
a23 = '23'
while True:
    
    res = input('[-]enter the number script : ')
    
    if res == a1:
        bunner()
        time_banner()
        kart_get()
    if res == a2:
        bunner()
        time_banner()
        font()
    if res == a3:
        bunner()
        time_banner()
        arz()
    if res == a4:
        bunner()
        time_banner()
        bio()
    if res == a5 :
        bunner()
        time_banner()
        channel()
    if res == a6:
        bunner()
        time_banner()
        info_insta()
        
    if res == a7:
        bunner()
        time_banner()
        ip()
        
    if res == a8:
        bunner()
        time_banner()
        irancell() 
    if res == a9:
        bunner()
        time_banner()
        tavalod()
    if res == a10:
        bunner()
        time_banner()
        weather()
    if res == a11:
        bunner()
        time_banner()
        proxy()
    if res == a12:
        bunner()
        time_banner()
        iran()
    if res == a13:
        bunner()
        time_banner()
        telegram()
    if res == a14:
        bunner()
        time_banner()
        phishing()
    if res == a15:
        bunner()
        time_banner()
        tabir_khab()
    if res == a16:
        bunner()
        time_banner()
        nod32()
    if res == a17:
        bunner()
        time_banner()
        music()
    if res == a18:
        bunner()
        time_banner()
        korona()
    if res == a19:
        bunner()
        time_banner()
        fake_info()
    if res == a20:
        bunner()
        timer()
    if res == a21:
        bunner()
        timer()
        info_face_book()
    if res == a22:
       bunner()
       time_banner()
       user_id_facebook()
    if res == 'exit':
        break

if os.name == 'nt':
    print("my channel : @elf_security_cyber")
else:    
    os.system('termux-open-url https://t.me/elf_security_cyber')     
           
