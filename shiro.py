# - *- coding: utf- 8 - *-
import SHIRO
from SHIRO import *
from akad.ttypes import *
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
#import pyimgflip
from googletrans import Translator
import youtube_dl

#Self_V03A_by.MASHIRO_URAHARA

print ("======[ SELF.BOT V03A ]======")
print ("===========[ MASHIRO URAHARA ]=============")
shiro = LineClient()
shiro = LineClient(authToken='ISI TOKEN DISINI')
shiro.log("Auth Token : " + str(shiro.authToken))
channel = LineChannel(shiro)
shiro.log("Channel Access Token : " + str(channel.channelAccessToken))
print ("Selfbot_run.....")

poll = LinePoll(shiro)
call = shiro
creator = ["u1d9e3a6f2aca5d6a037dec9fc7fbf927"] #Tambah sama mid kamu
owner = ["u1d9e3a6f2aca5d6a037dec9fc7fbf927"] #Tambah sama mid kamu 
admin = ["u1d9e3a6f2aca5d6a037dec9fc7fbf927"] #Tambah sama mid kamu
staff = ["u1d9e3a6f2aca5d6a037dec9fc7fbf927"]
mid = shiro.getProfile().mid
KAC = [shiro]
ABC = [shiro]
Bots = [mid]
Shiro = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []

welcome = []

responsename1 = shiro.getProfile().displayName

settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": 1,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":True,
    "dblacklist":True,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":False,
    "contact":False,
    'autoJoin':True,
    'autoAdd':False,
    'autoRead':False,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":True,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "selfbot":True,
    "mention":"SINI KAK GABUNG CHAT AJA 😊",
    "Respontag":"Berasa ada yg tag",
    "welcome":"Selamat datang & semoga betah",
    "comment":"Like like & like by Shiro.bot\nCreator: line.me/ti/p/~mashiro.ch4n",
    "message":"Terimakasih sudah add saya 😃",
    }

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('mashiro.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
with open('admin.json', 'r') as fp:
    admin = json.load(fp)      
with open('staff.json', 'r') as fp:
    staff = json.load(fp) 
    
Setbot1 = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot1)
Setbot2 = codecs.open("settings.json","r","utf-8")
settings = json.load(Setbot2)
Setbot3 = codecs.open("wait.json","r","utf-8")
wait = json.load(Setbot3)
Setbot4 = codecs.open("read.json","r","utf-8")
read = json.load(Setbot4)

mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
    
    
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def backupData():
    try:
        backup1 = Setmain
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup1, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup2 = settings
        f = codecs.open('settings.json','w','utf-8')
        json.dump(backup2, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup3 = wait
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup3, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup4 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup4, f, sort_keys=True, indent=4, ensure_ascii=False)        
        return True
    except Exception as error:
        logError(error)
        return False     

def restartBot():
    backupData()
    python = sys.executable
    os.exeshiro(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '\n•> %02d Hari \n•> %02d Jam \n•> %02d Menit \n•> %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '\n•> %02d Hari \n🇲?? %02d Jam \n•> %02d Menit \n•> %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(shiro.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        shiro.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        shiro.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def mentionMembers2(to, mid):
    try:
        arrData = ""
        textx = "Total User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(shiro.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        shiro.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        shiro.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMeention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@ShiroSelf "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    shiro.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    
def sendMeention2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@ShiroSelf "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    shiro.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        
def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Wkwkwk".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(shiro.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        shiro.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        shiro.sendMessage(to, None, contentMetadata={"STKID":"51626512","STKPKGID":"11538","STKVER":"1"}, contentType=7)
    except Exception as error:
        shiro.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Haii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = shiro.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nDi group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(shiro.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        shiro.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        shiro.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Byee  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = shiro.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]+"\nDari group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(shiro.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        shiro.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        shiro.sendMessage(to, "[ INFO ] Error :\n" + str(error))        

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = shiro.getAllContactIds()
        gid = shiro.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"◐ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n•> Group : "+str(len(gid))+"\n•> Teman : "+str(len(teman))+"\n•> Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n•> Runtime : \n • "+bot
        shiro.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        shiro.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╭════════════════" + "\n" + \
                  "║»» Shiro_SelfBots" + "\n" + \
                  "║»════════════════" + "\n" + \
                  "║»» Help BOT" + "\n" + \
                  "║»════════════════" + "\n" + \
                  "║»» " + key + "About\n" + \
                  "║»» " + key + "Open\n" + \
				  "║»» " + key + "shiroose\n" + \
				  "║»» " + key + "Ginfo\n" + \
				  "║»» " + key + "Grup list\n" + \
				  "║»» " + key + "Info 「@」\n" + \
				  "║»» " + key + "「@」Kick\n" + \
				  "║»» " + key + "Me\n" + \
                  "║»» " + key + "Mid「@」\n" + \
				  "║»» " + key + "Mybot\n" + \
                  "║»» " + key + "Mymid\n" + \
				  "║»» " + key + "Respon\n" + \
				  "║»» " + key + "Self:restart\n" + \
				  "║»» " + key + "Runtime\n" + \
				  "║»» " + key + "Speed/Sp\n" + \
                  "║»» " + key + "Sprespon\n" + \
				  "║»» " + key + "Steal name「@」\n" + \
                  "║»» " + key + "Steal bio「@」\n" + \
                  "║»» " + key + "Steal cv「@」\n" + \
				  "║»» " + key + "Steal pp「@」\n" + \
                  "║»» " + key + "Steal vp「@」\n" + \
                  "║»═══════════════" + "\n" + \
                  "║»» " + key + "Sider「on/off」\n" + \
                  "║»» " + key + "tag\n" + \
				  "║»» " + key + "Read [ on/off ]\n" + \
                  "║»» " + key + "Cek\n" + \
				  "║»» " + key + "Dor\n" + \
                  "║»════════════════" + "\n" + \
                  "║» http://line.me/ti/p/~mashiro.ch4n" + "\n" + \
                  "╰═══ CREATOR: ©Shiro™"
    return helpMessage

def help1():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "╭════════════════" + "\n" + \
                  "║»» Shiro_SelfBots" + "\n" + \
                  "║»══════════════" + "\n" + \
                  "║»» HELP 2 " + "\n" + \
                  "║»══════════════" + "\n" + \
                  "║»» " + key + "Cek spam\n" + \
                  "║»» " + key + "Cek pesan\n" + \
                  "║»» " + key + "Cek respon\n" + \
                  "║»» " + key + "Cek welcome\n" + \
                  "║»» " + key + "Cek leave\n" + \
                  "║»» " + key + "Msg spam:「Text」\n" + \
                  "║»» " + key + "Msg pesan:「Text」\n" + \
                  "║»» " + key + "Msg respon:「Text」\n" + \
                  "║»» " + key + "Msg welcome:「Text」\n" + \
                  "║»» " + key + "Msg leave:「Text」\n" + \
                  "║»» " + key + "Myname:「Name」\n" + \
                  "║»» " + key + "Cpp「Foto」\n" + \
                  "║»» " + key + "Gift:「Mid」「Jumlah」\n" + \
                  "║»» " + key + "Spam:「Mid」「Jumlah」\n" + \
				  "║»» " + key + "Set spamtag:「jumlahnya」\n" + \
                  "║»» " + key + "Spamtag「@」\n" + \
                  "║»» " + key + "Set pamcall:「jumlahnya」\n" + \
                  "║»» " + key + "Spamcall\n" + \
                  "║»» " + key + "Bc:「Text」\n" + \
                  "║»» " + key + "Setkey「New Key」\n" + \
                  "║»» " + key + "My key\n" + \
                  "║»» " + key + "Reset key\n" + \
				  "║»» " + key + "Self「on/off」\n" + \
				  "║»══════════════" + "\n" + \
                  "║» http://line.me/ti/p/~mashiro.ch4n" + "\n" + \
                  "╰═══ CREATOR: ©Shiro™"
    return helpMessage1

def help2():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "╭════════════════" + "\n" + \
                  "║»» Shiro_SelfBots" + "\n" + \
                  "║»════════════════" + "\n" + \
                  "║»» HELP 3" + "\n" + \
                  "║»════════════════" + "\n" + \
                  "║»» Help Blacklist " + "\n" + \
                  "║»═══════════════" + "\n" + \
                  "║»» List Menu " + "\n" + \
                  "║»» " + key + "Ban list\n" + \
				  "║»» " + key + "Ban 「@」\n" + \
				  "║»» " + key + "Ban/ (kirim kontak) \n" + \
                  "║»» " + key + "Blc\n" + \
				  "║»» " + key + "shiroearban\n" + \
				  "║»» " + key + "Refresh\n" + \
				  "║»» " + key + "Unban「@」\n" + \
				  "║»» " + key + "Unban/ (kirim kontak)\n" + \
				  "║»════════════════" + "\n" + \
                  "║» Help Setting " + "\n" + \
                  "║»════════════════" + "\n" + \
                  "║»» List Menu " + "\n" + \
                  "║»» " + key + "@Autoadd「on/off」\n" + \
				  "║»» " + key + "@Autojoin「on/off」\n" + \
				  "║»» " + key + "@Autoleave「on/off」\n" + \
				  "║»» " + key + "@Contact「on/off」\n" + \
				  "║»» " + key + "@Jointicket「on/off」\n" + \
				  "║»» " + key + "@Respon「on/off」\n" + \
				  "║»» " + key + "@Unsend「on/off」\n" + \
                  "║»» " + key + "@Welcome「on/off」\n" + \
                  "║»════════════════" + "\n" + \
                  "║»» Help Protect " + "\n" + \
                  "║»═══════════════" + "\n" + \
                  "║»» List Menu " + "\n" + \
				  "║»» " + key + "Allprotect 「on/off」\n" + \
                  "║»» " + key + "Notag「on/off」\n" + \
                  "║»» " + key + "Protectqr「on/off」\n" + \
                  "║»» " + key + "Protectjoin「on/off」\n" + \
                  "║»» " + key + "Protectkick「on/off」\n" + \
                  "║»» " + key + "Protectcancel「on/off」\n" + \
                  "║»» " + key + "Protectinvite「on/off」\n" + \
				  "║»══════════════" + "\n" + \
                  "║» http://line.me/ti/p/~mashiro.ch4n" + "\n" + \
                  "╰═══ CREATOR: ©Shiro™"
    return helpMessage2

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return

        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                        shiro.acceptGroupInvitation(op.param1)
                        ginfo = shiro.getGroup(op.param1)
                        shiro.sendMessage(op.param1,"Bye bye.... \n Group " +str(ginfo.name))
                        shiro.sendMessage(op.param1,"Selfbot respon by Shiro [Anonymous_BOT]\n\nList bot:\n\n∆ Selfbot (only)\n∆ Self + 3 assist 1 ghost\n∆ Self + 6 assist 2 ghost\n\nKepo? Call me ^_^\nhttp://line.me/ti/p/~mashiro.ch4n \n")
                        shiro.leaveGroup(op.param1)


        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                        shiro.acceptGroupInvitation(op.param1)
                        ginfo = shiro.getGroup(op.param1)
                        shiro.sendMessage(op.param1,"Haii salken all")
                        shiro.sendMessage(op.param1,"Protect by Shiro [Anonymous_BOT]\n\nList bot:\n\n∆ Selfbot (only)\n∆ Self + 3 assist 1 ghost\n∆ Self + 6 assist 2 ghost\n\nKepo? Call me ^_^\nhttp://line.me/ti/p/~mashiro.ch4n \n")

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = shiro.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            shiro.cancelGroupInvitation(op.param1,[_mid])
                    except:
                      pass

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = shiro.getGroup(op.param1)
                contact = shiro.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                shiro.sendImageWithURL(op.param1, image)

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        shiro.sendText(op.param1, wait["message"])

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

#-------------------------------------------------------------------------------                        
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass             

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        shiro.findAndAddContactsByMid(op.param1,admin)
                        shiro.inviteIntoGroup(op.param1,admin)
                        shiro.kickoutFromGroup(op.param1,[op.param2])
                    except:                
                     pass

            return

        if op.type == 55:
            try:
                if op.param1 in Setmain["readPoint"]:
                   if op.param2 in Setmain["readMember"][op.param1]:
                       pass
                   else:
                       Setmain["readMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = shiro.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = shiro.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        shiro.sendImageWithURL(op.param1, image)                        
                        
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = shiro.getGroup(at)
                                Shiro = shiro.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(Shiro.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':Shiro.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                shiro.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                shiro.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = shiro.getGroup(at)
                                Shiro = shiro.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Pesan Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(Shiro.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                shiro.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = shiro.getGroup(at)
                                Shiro = shiro.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(Shiro.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                shiro.sendMessage(at, str(ret_))
                                shiro.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)        
                                                                                                                                                                                                                                                                                                                                           
        if op.type == 26 or op.type == 25:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           shiro.sendMessage(msg.to, wait["Respontag"])
                           shiro.sendMessage(msg.to, None, contentMetadata={"STKID":"51626530","STKPKGID":"11538","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentiongift"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           idth = ["a0768339-c2d3-4189-9653-2909e9bb6f58","ec4a14ea-7437-407b-aee7-96b1cbbc1b4b","f35bd31f-5ec7-4b2f-b659-92adf5e3d151","ba1d5150-3b5f-4768-9197-01a3f971aa34","2b4ccc45-7309-47fe-a006-1a1edb846ddb","168d03c3-dbc2-456f-b982-3d6f85f52af2","d4f09a5f-29df-48ac-bca6-a204121ea165","517174f2-1545-43b9-a28f-5777154045a6","762ecc71-7f71-4900-91c9-4b3f213d8b26","2df50b22-112d-4f21-b856-f88df2193f9e"]
                           plihth = random.choice(idth)
                           jenis = ["5","6","7","8"]
                           plihjenis = random.choice(jenis)
                           shiro.sendMessage(msg.to, "Ye ngetag ngetag, minta digift ya? cek PC gih, udah gue gift tuh. Jangan lupa bilang makasih yak!")
                           shiro.sendMessage(msg._from, None, contentMetadata={"PRDID":plihth,"PRDTYPE":"THEME","MSGTPL":plihjenis}, contentType=9)
                           break                       
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           shiro.sendMessage(msg.to, "Jangan tag saya....")
                           shiro.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    shiro.sendMessage(msg.to,"「Cek ID Sticker」\n•> STKID : " + msg.contentMetadata["STKID"] + "\n•> STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n•> STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    shiro.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = shiro.getContact(msg.contentMetadata["mid"])
                        path = shiro.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        shiro.sendMessage(msg.to,"⏩ Nama: " + msg.contentMetadata["displayName"] + "\n⏩ MID: " + msg.contentMetadata["mid"] + "\n⏩ Status: " + contact.statusMessage + "\n⏩ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        shiro.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                
            if msg.contentType == 1:
                    path = shiro.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n• Sticker ID : {}".format(stk_id)
                   ret_ += "\n• Sticker Version : {}".format(stk_ver)
                   ret_ += "\n• Sticker Package : {}".format(pkg_id)
                   ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = shiro.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
                            
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    shiro.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    shiro.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = shiro.getContact(msg.contentMetadata["mid"])
                        path = shiro.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        shiro.sendMessage(msg.to,"»» Nama : " + msg.contentMetadata["displayName"] + "\n»» MID : " + msg.contentMetadata["mid"] + "\n»» Status Msg : " + contact.statusMessage + "\n»» Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        shiro.sendImageWithURL(msg.to, image)
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        shiro.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        shiro.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        shiro.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        shiro.sendMessage(msg.to,"Contact itu bukan anggota bot")
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        shiro.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        shiro.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        shiro.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        shiro.sendMessage(msg.to,"Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        shiro.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        shiro.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        shiro.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        shiro.sendMessage(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        shiro.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        shiro.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        shiro.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        shiro.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = shiro.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            shiro.sendMessage(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = shiro.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     shiro.updateGroupPicture(msg.to, path)
                     shiro.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["foto"]:
                            path = shiro.downloadObjectMsg(msg_id)
                            del Setmain["foto"][mid]
                            shiro.updateProfilePicture(path)
                            shiro.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = shiro.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     shiro.updateProfilePicture(path1)
                     shiro.sendMessage(msg.to, "Berhasil mengubah foto profile")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        shiro.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               shiro.sendMessage(msg.to, str(helpMessage))

                        if cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = help1()
                               shiro.sendMessage(msg.to, str(helpMessage1))

                        if cmd == "help3":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage2 = help2()
                               shiro.sendMessage(msg.to, str(helpMessage2))
                                                                                       
                        if cmd == "selfbot on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                shiro.sendMessage(msg.to, "Selfbot diaktifkan")
                                
                        elif cmd == "selfbot off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                shiro.sendMessage(msg.to, "Selfbot dinonaktifkan")                                                                 

                        if cmd == "unsend on":
                            if msg._from in admin:
                                wait["unsend"] = True
                                shiro.sendMessage(msg.to, "Deteksi Unsend Diaktifkan")
                                
                        if cmd == "unsend off":
                            if msg._from in admin:
                                wait["unsend"] = False
                                shiro.sendMessage(msg.to, "Deteksi Unsend Dinonaktifkan")                                

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭════════ STATUS ════════\n"
                                if wait["unsend"] == True: md+="║»» ✔️ Unsend「ON」\n"
                                else: md+="║»» ❌ Unsend「OFF」\n"                                
                                if wait["Mentionkick"] == True: md+="║»» ✔️ Notag「ON」\n"
                                else: md+="║»» ❌ Notag「OFF」\n"
                                if wait["detectMention"] == True: md+="║»» ✔️ Respon「ON」\n"
                                else: md+="║»» ❌ Respon「OFF」\n"                   
                                if wait["autoJoin"] == True: md+="║»» ✔️ Autojoin「ON」\n"
                                else: md+="║»» ❌ Autojoin「OFF」\n"
                                if settings["autoJoinTicket"] == True: md+="║»» ✔️ Jointicket「ON」\n"
                                else: md+="║»» ❌ Jointicket「OFF」\n"                                
                                if wait["autoAdd"] == True: md+="║»» ✔️ Autoadd「ON」\n"
                                else: md+="║»» ❌ Autoadd「OFF」\n"
                                if msg.to in welcome: md+="║»» ✔️ Welcome「ON」\n"
                                else: md+="║»» ❌ Welcome「OFF」\n"                 
                                if wait["autoLeave"] == True: md+="║»» ✔️ Autoleave「ON」\n"
                                else: md+="║»» ❌ Autoleave「OFF」\n"
                                if msg.to in protectqr: md+="║»» ✔️ Protecturl「ON」\n"
                                else: md+="║»» ❌ Protecturl「OFF」\n"
                                if msg.to in protectjoin: md+="║»» ✔️ ProtectJoin「ON」\n"
                                else: md+="║»» ❌ ProtectJoin「OFF」\n"
                                if msg.to in protectkick: md+="║»» ✔️ Protectkick「ON」\n"
                                else: md+="║»» ❌ Protectkick「OFF」\n"
                                if msg.to in protectcancel: md+="║»» ✔️ Protectcancel「ON」\n"
                                else: md+="║»» ❌ Protectcancel「OFF」\n"
                                if msg.to in protectinvite: md+="║»» ✔️ Protectinvite「ON」\n"
                                else: md+="║»» ❌ Protectinvite「OFF」\n"                                
                                shiro.sendMessage(msg.to, md+"║»»══════════════════════\n║»» Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n║»» Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n  ╰═══════════════════════")

                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in admin:
                                shiro.sendMessage(msg.to,"Creator Bot") 
                                ma = ""
                                for i in creator:
                                    ma = shiro.getContact(i)
                                    shiro.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "About":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「 Shiro.bot 」\n")
                               shiro.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me" or text.lower() == 'mek':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': msg._from}
                               shiro.sendMessage1(msg)
                               
                        elif text.lower() == "aku":
                            if msg._from in admin:                        	
                             tz = pytz.timezone("Asia/Jakarta")
                             timeNow = datetime.now(tz=tz)
                             day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                             hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                             bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                             hr = timeNow.strftime("%A")
                             bln = timeNow.strftime("%m")
                             for i in range(len(day)):
                                 if hr == day[i]: hasil = hari[i]
                             for k in range(0, len(bulan)):
                                 if bln == str(k): bln = bulan[k-1]
                             readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                             shiro.sendMessage(to,"┣━━╦KONTAK PROFILE╦━━╣\n " + readTime)
                             sendMeention(to, "@!", [sender])
                             shiro.sendContact(to, sender)                                 

                        elif text.lower() == "mymid":
                            if msg._from in admin:
                               shiro.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = shiro.getContact(key1)
                               shiro.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               shiro.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = shiro.getContact(key1)
                               shiro.sendMessage(msg.to, "»» Nama : "+str(mi.displayName)+"\n»» Mid : " +key1+"\n»» Status Message"+str(mi.statusMessage))
                               shiro.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(ki.getContact(key1)):
                                   shiro.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   shiro.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               shiro.sendMessage1(msg)

                        elif text.lower() == "shiroeanall chat":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               try:
                                   shiro.sendMessage(msg.to,"Chat dibersihkan...")
                               except:
                                   pass

                        elif cmd.startswith("steal name "):
                          if msg._from in admin:
                              if 'MENTION' in msg.contentMetadata.keys()!= None:
                                  names = re.findall(r'@(\w+)', text)
                                  mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                  mentionees = mention['MENTIONEES']
                                  lists = []
                                  for mention in mentionees:
                                      if mention["M"] not in lists:
                                          lists.append(mention["M"])
                                  for ls in lists:
                                      contact = shiro.getContact(ls)
                                      shiro.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                            
                        elif cmd.startswith("steal bio "):
                            if msg._from in admin:
                              if 'MENTION' in msg.contentMetadata.keys()!= None:
                                  names = re.findall(r'@(\w+)', text)
                                  mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                  mentionees = mention['MENTIONEES']
                                  lists = []
                                  for mention in mentionees:
                                      if mention["M"] not in lists:
                                          lists.append(mention["M"])
                                  for ls in lists:
                                      contact = shiro.getContact(ls)
                                      shiro.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                            
                        elif cmd.startswith("steal pp "):
                            if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        path = "http://dl.profile.line-cdn.net/" + shiro.getContact(ls).pictureStatus
                                        shiro.sendImageWithURL(msg.to, str(path))
                            
                        elif cmd.startswith("steal cv "):
                            if msg._from in admin:
                                if line != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            path = shiro.getProfileCoverURL(ls)
                                            shiro.sendImageWithURL(msg.to, str(path))
                        elif cmd.startswith("steal vp "):
                            if msg._from in admin:
                                    targets = []
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            contact = shiro.getContact(target)
                                            path = "http://dl.profile.line.naver.jp"+contact.picturePath+"/vp"
                                            shiro.sendVideoWithURL(msg.to, path)
                                        except Exception as e:
                                            pass                                            

                        elif cmd.startswith("bc: "):
                           if msg._from in admin:
                             sep = text.split(" ")
                             bc = text.replace(sep[0] + " ","")
                             saya = shiro.getGroupIdsJoined()
                             for group in saya:
                                ryan = shiro.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Broadcast 」\nfrom:  "
                                ret_ = "{}".format(str(bc))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                shiro.sendMessage(group, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif text.lower() == "my key":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               shiro.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("set key "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   shiro.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   shiro.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "reset key":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               shiro.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd == "self:restart":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               shiro.sendMessage(msg.to, "Restart Sukses Bos!...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               shiro.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = shiro.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(ki.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                shiro.sendMessage(msg.to, "║»» BOT Grup Info\n\n ║»» Nama Group : {}".format(G.name)+ "\n»» ID Group : {}".format(G.id)+ "\n»» Pembuat : {}".format(G.creator.displayName)+ "\n»» Waktu Dibuat : {}".format(str(timeCreated))+ "\n»» Jumlah Member : {}".format(str(len(G.members)))+ "\n»» Jumlah Pending : {}".format(gPending)+ "\n»» Group Qr : {}".format(gQr)+ "\n»» Group Ticket : {}".format(gTicket))
                                shiro.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                shiro.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                shiro.sendMessage(msg.to, str(e))

                        elif cmd.startswith("info grup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = shiro.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = shiro.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(shiro.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "║»» BOT Grup Info\n"
                                ret_ += "\n║»» Nama Group : {}".format(G.name)
                                ret_ += "\n║»» ID Group : {}".format(G.id)
                                ret_ += "\n║»» Pembuat : {}".format(gCreator)
                                ret_ += "\n║»» Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n║»» Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n║»» Jumlah Pending : {}".format(gPending)
                                ret_ += "\n║»» Group Qr : {}".format(gQr)
                                ret_ += "\n║»» Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                shiro.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd == "list group":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = shiro.getGroupIdsJoined()
                               for i in gid:
                                   G = shiro.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "║»» " + str(a) + ". " +G.name+ "\n"
                               shiro.sendMessage(msg.to,"╭════════[ GROUP LIST ]\n║»»\n"+ma+"║»»\n  ╰═══════[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = shiro.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   shiro.updateGroup(X)
                                   shiro.sendMessage(msg.to, "QR telah dibuka")

                        elif cmd == "shiroose":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = shiro.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   shiro.updateGroup(X)
                                   shiro.sendMessage(msg.to, "QR telah ditutup")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = shiro.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      shiro.updateGroup(x)
                                   gurl = shiro.reissueGroupTicket(msg.to)
                                   shiro.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "cpp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["foto"][mid] = True
                                shiro.sendMessage(msg.to,"Kirim fotonya.....")

                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = shiro.getProfile()
                                profile.displayName = string
                                shiro.updateProfile(profile)
                                shiro.sendMessage(msg.to,"Nama diganti jadi " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "tag" or text.lower() == '😆':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            	group = shiro.getGroup(msg.to) 
                          Rmem = [contact.mid for contact in group.members]
                          Dmem = len(Rmem)//20
                          try:                          	
                              for mentionMembers in range(Dmem+1):
                                  no = 0
                                  ret_ = "╔════════════\nShiro.bot\n╚════════════\n╔════════════"
                                  dataMid = []
                                  for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                      dataMid.append(dataMention.mid)
                                      no += 1
                                      ret_ += "\n╠ [{}] @!".format(str(no))
                                  ret_ += "\n╚══════════════\n╔═══════════════\n   TOTAL MEMBER [ {} ]\n╚═══════════════".format(str(len(dataMid)))
                                  sendMeention2(msg.to, ret_, dataMid)                             
                          except Exception as Ewe:
                              print(Ewe)
                                  
                        elif cmd == "dor" or text.lower() == '😆':
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                            	group = shiro.getGroup(msg.to)
                          Rmem = [contact.mid for contact in group.members]
                          Dmem = len(Rmem)//20
                          try:                          	
                              for mentionMembers2 in range(Dmem+1):
                                  no = 0
                                  ret_ = "╔════════════\n   Shiro [ √  ]\n╚════════════\n╔════════════"
                                  dataMid = []
                                  for dataMention in group.members[mentionMembers2*20 : (mentionMembers2+1)*20]:
                                      dataMid.append(dataMention.mid)
                                      no += 1
                                      ret_ += "\n╠.[{}] @!".format(str(no))
                                  ret_ += "\n╚══════════════\n╔════════════\n.  TOTAL MEMBER [ {} ]\n╚══════════════".format(str(len(dataMid)))
                                  sendMeention(msg.to, ret_, dataMid)
                          except Exception as Ewe:
                              print(Ewe) 

                        elif cmd == "list bot":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +shiro.getContact(m_id).displayName + "\n"
                                shiro.sendMessage(msg.to,"»» BOT\n\n"+ma+"\nTotal「%s」BOT" %(str(len(Bots))))

                        elif cmd == "list admin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +shiro.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +shiro.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +shiro.getContact(m_id).displayName + "\n"
                                shiro.sendMessage(msg.to,"»» BOT admin\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotal「%s」" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +shiro.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +shiro.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +shiro.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +shiro.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +shiro.getGroup(group).name + "\n"                                    
                                shiro.sendMessage(msg.to,"»» Shiro SelfPro\n\n»» PROTECT URL :\n"+ma+"\n»» PROTECT KICK :\n"+mb+"\n»» PROTECT JOIN :\n"+md+"\n»» PROTECT CANCEL:\n"+mc+"\n»» PROTECT INVITE :\n"+me+"\nTotal「%s」Protect yang aktif" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite))))

                        elif cmd == "respon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                shiro.sendMessage(msg.to,responsename1)
                                             
                        elif cmd == "sprespon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = shiro.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = shiro.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = shiro.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                shiro.sendMessage(msg.to, " »» Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/1000,get_contact_time/1000,get_group_time/1000))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               shiro.sendMessage(msg.to, "Speed ...")
                               elapsed_time = time.time() - start
                               shiro.sendMessage(msg.to, "{} detik".format(str(elapsed_time/1000)))

                        elif cmd == "read on":
                          if wait["selfbot"] == True:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['readPoint'][msg.to] = msg_id
                                 Setmain['readMember'][msg.to] = {}
                                 shiro.sendMessage(msg.to, "Reading point diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "read off":
                          if wait["selfbot"] == True:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['readPoint'][msg.to]
                                 del Setmain['readMember'][msg.to]
                                 shiro.sendMessage(msg.to, "Reading point dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "cek":
                            if msg.to in Setmain['readPoint']:
                                if Setmain['readMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['readMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Read Member ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(shiro.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        shiro.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['readPoint'][msg.to]
                                        del Setmain['readMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['readPoint'][msg.to] = msg.id
                                    Setmain['readMember'][msg.to] = {}
                                else:
                                    shiro.sendMessage(msg.to, "none user.....")
                            else:
                                shiro.sendMessage(msg.to, "Ketik [Read on] dulu")
                                
                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  shiro.sendMessage(msg.to, "╔═══════════════\n╠ Cek sider diaktifkan\n╠═══════════════\n╠ Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n╠ Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n╚═══════════════")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  shiro.sendMessage(msg.to, "╔═══════════════\n╠ Cek sider dinonaktifkan\n╠═══════════════\n╠ Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n╠ Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n╚═══════════════")
                              else:
                                  shiro.sendMessage(msg.to, "Sudak tidak aktif")                                

                        elif cmd.startswith("set spamtag: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["limit"] = num
                                shiro.sendMessage(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("set spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                shiro.sendMessage(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["limit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                shiro.sendMessage1(msg)
                                            except Exception as e:
                                                shiro.sendMessage(msg.to,str(e))
                                    else:
                                        shiro.sendMessage(msg.to,"KEBANYAKAN GOBLOK!")
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = shiro.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                shiro.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        shiro.sendMessage(msg.to,str(e))
                                else:
                                    shiro.sendMessage(msg.to,"KEBANYAKAN BANGSAT!")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      shiro.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      shiro.sendMessage(midd, str(Setmain["message"]))

#===========Settings============#
                        elif '@Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = shiro.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  shiro.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = shiro.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    shiro.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
#===========Protection============#                                    

                        elif 'Protectqr ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protect ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect qr/url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = shiro.getGroup(msg.to)
                                       msgs = "Protect qr/url diaktifkan\nDi Group : " +str(ginfo.name)
                                  shiro.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = shiro.getGroup(msg.to)
                                         msgs = "Protect qt/url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect qr/url sudah tidak aktif"
                                    shiro.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = shiro.getGroup(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  shiro.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = shiro.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    shiro.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = shiro.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  shiro.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = shiro.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    shiro.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = shiro.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  shiro.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = shiro.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    shiro.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'Protectinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = shiro.getGroup(msg.to)
                                       msgs = "Protect invite diaktifkan\nDi Group : " +str(ginfo.name)
                                  shiro.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = shiro.getGroup(msg.to)
                                         msgs = "Protect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    shiro.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)  
                                    
                        elif 'Allprotect ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Allprotect ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)                                      
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = shiro.getGroup(msg.to)
                                      msgs = "ALL protect sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = shiro.getGroup(msg.to)
                                      msgs = "Sudah mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  shiro.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""                                         
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = shiro.getGroup(msg.to)
                                         msgs = "ALL protect sudah off\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = shiro.getGroup(msg.to)
                                         msgs = "Sudah menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    shiro.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

#===========KICKOUT============#
                        elif ("Kick " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

#===========ADMIN ADD============#
                        elif ("Creatoradd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           creator[target] = True
                                           f=codecs.open('creator.json','w','utf-8')
                                           json.dump(creator, f, sort_keys=True, indent=4,ensure_ascii=False) 
                                           shiro.sendMessage(msg.to,"Berhasil menambahkan creator")
                                       except:
                                           pass                                           
                                           
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin[target] = True
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False) 
                                           shiro.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass                                           

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff[target] = True
                                           f=codecs.open('staff.json','w','utf-8')
                                           json.dump(staff, f, sort_keys=True, indent=4,ensure_ascii=False) 
                                           shiro.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass                                           

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           shiro.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Creatordell " in msg.text):
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del creator[target]
                                           f=codecs.open('creator.json','w','utf-8')
                                           json.dump(creator, f, sort_keys=True, indent=4,ensure_ascii=False) 
                                           shiro.sendMessage(msg.to,"Berhasil menghapus Creator")
                                       except:
                                           pass
                                           
                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del admin[target]
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False) 
                                           shiro.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del staff[target]
                                           f=codecs.open('staff.json','w','utf-8')
                                           json.dump(staff, f, sort_keys=True, indent=4,ensure_ascii=False) 
                                           shiro.sendMessage(msg.to,"Berhasil menghapus Staff")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.remove(target)
                                           shiro.sendMessage(msg.to,"Berhasil menghapus bot")
                                       except:
                                           pass

                        elif cmd == "addadmin/" or text.lower() == 'addadmin/':
                            if msg._from in creator:
                                wait["addadmin"] = True
                                shiro.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "delladmin/" or text.lower() == 'delladmin/':
                            if msg._from in creator:
                                wait["delladmin"] = True
                                shiro.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "addstaff/" or text.lower() == 'addstaff/':
                            if msg._from in creator:
                                wait["addstaff"] = True
                                shiro.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "delstaff/" or text.lower() == 'dellstaff/':
                            if msg._from in creator:
                                wait["dellstaff"] = True
                                shiro.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "addbot/" or text.lower() == 'addbot/':
                            if msg._from in creator:
                                wait["addbots"] = True
                                shiro.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "dellbot/" or text.lower() == 'dellbot/':
                            if msg._from in creator:
                                wait["dellbots"] = True
                                shiro.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in creator:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                shiro.sendMessage(msg.to,"Refresh Done!")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = shiro.getContact(i)
                                    shiro.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = shiro.getContact(i)
                                    shiro.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = shiro.getContact(i)
                                    shiro.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "@notag on" or text.lower() == '@notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                shiro.sendMessage(msg.to,"Notag diaktifkan")

                        elif cmd == "@notag off" or text.lower() == '@notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = False
                                shiro.sendMessage(msg.to,"Notag dinonaktifkan")

                        elif cmd == "@contact on" or text.lower() == '@contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                shiro.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "@contact off" or text.lower() == '@contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                shiro.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "@respon on" or text.lower() == '@respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                shiro.sendMessage(msg.to,"Auto respon diaktifkan")

                        elif cmd == "@respon off" or text.lower() == '@respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                shiro.sendMessage(msg.to,"Auto respon dinonaktifkan")                   

                        elif cmd == "@autojoin on" or text.lower() == '@autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                shiro.sendMessage(msg.to,"Autojoin diaktifkan")

                        elif cmd == "@autojoin off" or text.lower() == '@autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                shiro.sendMessage(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "@autoleave on" or text.lower() == '@autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                shiro.sendMessage(msg.to,"Autoleave diaktifkan")

                        elif cmd == "@autoleave off" or text.lower() == '@autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                shiro.sendMessage(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "@autoadd on" or text.lower() == '@autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                shiro.sendMessage(msg.to,"Auto add diaktifkan")

                        elif cmd == "@autoadd off" or text.lower() == '@autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                shiro.sendMessage(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "@sticker on" or text.lower() == '@sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                shiro.sendMessage(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "@sticker off" or text.lower() == '@sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                shiro.sendMessage(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "@jointicket on" or text.lower() == '@jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                shiro.sendMessage(msg.to,"Join ticket diaktifkan")

                        elif cmd == "@jointicket off" or text.lower() == '@jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                shiro.sendMessage(msg.to,"Join Ticket dinonaktifkan")

#===========COMMAND BLACKLIST============#

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           shiro.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           shiro.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban/" or text.lower() == 'ban/':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                shiro.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "unban/" or text.lower() == 'unban/':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                shiro.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "ban list" or text.lower() == 'ban list':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                shiro.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +shiro.getContact(m_id).displayName + "\n"
                                shiro.sendMessage(msg.to,"»» Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    shiro.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = shiro.getContact(i)
                                        shiro.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "shiroearban" or text.lower() == 'shiroearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = shiro.getContacts(wait["blacklist"])
                              mc = "[%i]User Blacklist" % len(ragets)
                              shiro.sendMessage(msg.to,"List ban dihapus " +mc)

#===========COMMAND SET RESPON============#

                        elif 'Msg pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Msg pesan: ','')
                              if spl in [""," ","\n",None]:
                                  shiro.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  shiro.sendMessage(msg.to, "「Pesan Msg」\n\n「{}」".format(str(spl)))

                        elif 'Msg welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Msg welcome: ','')
                              if spl in [""," ","\n",None]:
                                  shiro.sendMessage(msg.to, "Gagal mengganti Welcome Message")
                              else:
                                  wait["welcome"] = spl
                                  shiro.sendMessage(msg.to, "「Welcome Msg」\n\n「{}」".format(str(spl)))
                                  
                        elif 'Msg leave: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Msg leave: ','')
                              if spl in [""," ","\n",None]:
                                  shiro.sendMessage(msg.to, "Gagal mengganti Leave Msg")
                              else:
                                  wait["leave"] = spl
                                  shiro.sendMessage(msg.to, "「Leave Msg」\n\n「{}」".format(str(spl)))                                    

                        elif 'Msg respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Msg respon: ','')
                              if spl in [""," ","\n",None]:
                                  shiro.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  shiro.sendMessage(msg.to, "「Respon Msg」\n\n「{}」".format(str(spl)))

                        elif 'Msg spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Msg spam: ','')
                              if spl in [""," ","\n",None]:
                                  shiro.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["message"] = spl
                                  shiro.sendMessage(msg.to, "「Spam Msg」\n\n「{}」".format(str(spl)))

                        elif 'Msg sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Msg sider: ','')
                              if spl in [""," ","\n",None]:
                                  shiro.sendMessage(msg.to, "Gagal mengganti Sider Message")
                              else:
                                  wait["mention"] = spl
                                  shiro.sendMessage(msg.to, "「Sider Msg」\n\n「{}」".format(str(spl)))

#---------CEK RESPON BOT--------------

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               shiro.sendMessage(msg.to, "「Pesan Msg」\n\n「 " + str(wait["message"]) + " 」")
                               
                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               shiro.sendMessage(msg.to, "「Welcome Msg」\n\n「 " + str(wait["welcome"]) + " 」")
                               
                        elif text.lower() == "cek leave":
                            if msg._from in admin:
                               shiro.sendMessage(msg.to, "「Leave Msg」\n\n「 " + str(wait["leave"]) + " 」")                                                                

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               shiro.sendMessage(msg.to, "「Respon Msg」\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               shiro.sendMessage(msg.to, "「Spam Msg」n\n「 " + str(Setmain["message"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               shiro.sendMessage(msg.to, "「Sider Msg」\n\n「 " + str(wait["mention"]) + " 」")
 
                        elif cmd == "Dorr!":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                              if msg.toType == 11:
                                print ("Ratain")
                                _name = msg.text.replace("Dorr!","")
                              gs = shiro.getGroup(msg.to)
                              targets = []
                              for g in gs.members:
                                if _name in g.displayName:
                                  targets.append(g.mid)
                              if targets == []:
                                shiro.sendMessage(msg.to,"Not found")
                              else:
                                for target in targets:
                                  if target in admin:
                                    pass
                                  elif target in Bots:
                                    pass
                                  elif target in staff:
                                    pass
                                  else:
                                    try:
                                      klist=[shiro]
                                      kicker=random.choice(klist)
                                      kicker.kickoutFromGroup(msg.to,[target])
                                      print (msg.to,[g.mid])
                                    except:
                                      try:
                                        shiro.kickoutFromGroup(msg.to,[target])
                                      except:
                                        shiro.kickoutFromGroup(msg.to,[target])             
                 
#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = shiro.findGroupByTicket(ticket_id)
                                     shiro.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     shiro.sendMessage(msg.to, "OTW JOIN GROUP : %s" % str(group.name))                                     

    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
                               