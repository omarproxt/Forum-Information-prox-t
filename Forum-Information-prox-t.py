import os
os.system ('clear')
import requests, pyfiglet,time,sys,webbrowser 
Ab='\033[1;92m'
aB='\033[1;91m'
AB='\033[1;96m'
aBbs='\033[1;93m'
AbBs='\033[1;95m'
A_bSa = '\033[1;31m'
a_bSa = '\033[1;32m'
faB_s = '\033[2;32m'
a_aB_s = '\033[2;39m'
Ba_bS = '\033[2;36m'
Ya_Bs = '\033[1;34m'
S_aBs = '\033[1;33m'
logo = pyfiglet.figlet_format('omarproxt')
print(a_bSa+logo)
webbrowser.open('https://t.me/omarproxt25')
import amino
client = amino.Client()
com_id = client.get_from_code(input("-- Community Link••>> ")).json["extensions"]["community"]["ndcId"]
community_info = client.get_community_info(comId=com_id).json
icon = community_info["icon"]
tagline = community_info["tagline"]
endpoint = community_info["endpoint"]
description = community_info["content"]
created_time = community_info["createdTime"]
community_cover = str(community_info["promotionalMediaList"]).split("'")[1]
print(f"""

-- Community icon link••>>  {icon}

-- Community cover link••>> {community_cover}

-- Community tagline••>> {tagline}

-- Community endpoint••>> {endpoint}

-- Community created time••>> {created_time}
""")
