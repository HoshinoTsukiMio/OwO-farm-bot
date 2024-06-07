import json, math, random, os, time, hashlib, threading, datetime
try:
    import json, math, random, os, time, hashlib, threading, datetime
    from data.file import phrases, actvar, gamblevar
    from update import update_bot
    import requests, psutil, pytz
    from pypresence import Presence
    from blessed import Terminal
    from notifypy import Notify
except ModuleNotFoundError :
    print("Please Run: 'pip install -r lib.lib'")
    time.sleep(2)
    exit()

# Get the current working directory
current_dir = os.getcwd()
# Join the current directory with the filename
flie_data = os.path.join(current_dir, 'data\\data.json')
file_cache = os.path.join(current_dir, 'data\\cache.json')
#Call cfg.json file 
with open(flie_data, 'r', encoding='utf-8') as a:
    cfgs = json.load(a)
#chalk
term = Terminal()
red = term.red
green = term.green
blue = term.blue
yellow = term.yellow
magenta = term.magenta
#▄▀█ █▀▀ █▀▀ █▀▀ █▀ █▀   ▀█▀ █░█ █▀▀   █▀ █▀▀ ▀█▀ ▀█▀ █ █▄░█ █▀▀ █▀
#█▀█ █▄▄ █▄▄ ██▄ ▄█ ▄█   ░█░ █▀█ ██▄   ▄█ ██▄ ░█░ ░█░ █ █░▀█ █▄█ ▄█

setting               = cfgs["settings"]
prefix                = str(setting['prefix'])
bot_prefix            = str(setting['bot_prefix'])
owo                   = str(setting['owo'])
pray                  = str(setting['pray'])
curse                 = str(setting['curse'])
hunt                  = str(setting['hunt'])
battle                = str(setting['battle'])
autoquest             = str(setting['autoquest'])
extratokencheck       = str(setting['extratoken'])
randommess            = str(setting['randommess'])
presence              = str(setting['presence'])
banbypass             = str(setting['banbypass'])
auto_update           = str(setting['auto_update'])
#========================================================================================================================
inventory             = setting['inventory']
inventorycheck        = str(inventory['inventorycheck'])
gemcheck              = str(inventory['gemcheck'])
lootboxcheck          = str(inventory['lootboxcheck'])
fabledlootboxcheck    = str(inventory['fabledlootboxcheck'])
cratecheck            = str(inventory['cratecheck'])
#========================================================================================================================
animals               = setting['animals']
a_enable              = str(animals['enable'])
a_type                = str(animals['type'])
animaltype            = animals['animaltype']
common                = str(animaltype['common'])
uncommon              = str(animaltype['uncommon'])
rare                  = str(animaltype['rare'])
epic                  = str(animaltype['epic'])
mythical              = str(animaltype['mythical'])
patreon               = str(animaltype['patreon'])
cpatreon              = str(animaltype['cpatreon'])
legendary             = str(animaltype['legendary'])
gem                   = str(animaltype['gem'])
bot                   = str(animaltype['bot'])
distorted             = str(animaltype['distorted'])
fabled                = str(animaltype['fabled'])
special               = str(animaltype['special'])
hidden                = str(animaltype['hidden'])
#========================================================================================================================
upgradeautohunt       = setting['upgradeautohunt']
upg_enable            = str(upgradeautohunt['enable'])
upg_type              = str(upgradeautohunt['upgtype'])
#========================================================================================================================
gamble                = setting['gamble']
coinflip              = gamble['coinflip']
coinflip_enable       = str(coinflip['enable'])
coinflip_amount       = str(coinflip['amount'])

slots                 = gamble['slots']
slots_enable          = str(slots['enable'])
slots_amount          = str(slots['amount'])
#========================================================================================================================
main                  = cfgs['main']
main_token            = str(main['token'])
main_id               = str(main['userid'])
main_channelid        = str(main['channelid'])
main_owodmchannelid   = str(main['owodmchannelid'])
main_questchannelid   = str(main['autoquestchannelid'])

extra                 = cfgs['extra']
extra_token           = str(extra['token'])
extra_id              = str(extra['userid'])
extra_channelid       = str(extra['channelid'])
extra_owodmchannelid  = str(extra['owodmchannelid'])
extra_questchannelid  = str(extra['autoquestchannelid'])

cp                    = cfgs['custom_presence']
client_id_            = str(cp['client_id'])
state_                = str(cp['state'])
large_image_          = str(cp['large_image'])
small_image_          = str(cp['small_image'])
large_text_           = str(cp['large_text'])
small_text_           = str(cp['small_text'])
label1_               = str(cp['label1'])
label2_               = str(cp['label2'])
label_link1_          = str(cp['label_link1'])
label_link2_          = str(cp['label_link2'])

#========================================================================================================================
notification = Notify()
process = psutil.Process()
quest = True
etoken = False
active_bot = True
capcha_flag = False
task_bot_active = True
captcha_check_var = False
if (extra_token == main_token):
    extratokencheck = "false"

version = "0.0.0.0"
banversion = "0.0.0"


def updatebot():
    print("Updating...")
    update = requests.get(
        "updatefile link"
    )
    # Save the new version to the local file system
    with open("update.py", "wb") as b:
        b.write(update.content)
#========================================================================================================================
def auto_update_bot():
    if auto_update == "true":
        versions = requests.get('')
        if versions  != version:
            global active_bot, task_bot_active
            active_bot = False
            task_bot_active = False
            print("New version detected")
            update_bot()
            time.sleep(5)
            exit(0)
#========================================================================================================================
def show_presence(): # this only work on discord app not web
    if presence == "true":
        RPC = Presence(f"{client_id_}")
        RPC.connect()
        RPC.update(
                state = f"{state_}",
                large_image = f"{large_image_}",
                small_image= f"{small_image_}",
                large_text= f"{large_text_}",
                small_text= f"{small_text_}",
                buttons=[
                        {"label": f"{label1_}", "url": f"{label_link1_}"},
                        {"label": f"{label2_}", "url": f"{label_link2_}"}
                ]
        )
def notification_def(tokentype):
    noti_count = 11
    while noti_count > 1:
        if captcha_check_var == True:
            noti_count = noti_count - 1
            noti_count_str = str(noti_count)
            notification.title = f"[{tokentype}] Captcha Detected!"
            notification.message = f"SOLVE CAPTCHA AND RESTART BOT\nyou only have {noti_count_str}min left"
            notification.icon = "data/owo.ico"
            print(f"notification {noti_count}")
            notification.send()
        else:
            break
        time.sleep(60)
#███╗░░░███╗░█████╗░██╗███╗░░██╗  ██████╗░███████╗███████╗
#████╗░████║██╔══██╗██║████╗░██║  ██╔══██╗██╔════╝██╔════╝
#██╔████╔██║███████║██║██╔██╗██║  ██║░░██║█████╗░░█████╗░░
#██║╚██╔╝██║██╔══██║██║██║╚████║  ██║░░██║██╔══╝░░██╔══╝░░
#██║░╚═╝░██║██║░░██║██║██║░╚███║  ██████╔╝███████╗██║░░░░░
#╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝  ╚═════╝░╚══════╝╚═╝░░░░░
def rantime():
    rdt = random.randint(0, 5) + round(random.uniform(0, 1), 3)
    while rdt < 1:
        rdt = random.randint(0, 5) + round(random.uniform(0, 1), 3)
        continue
    return rdt
#========================================================================================================================
def nonce():
    rannonce = 1098393848631590 + math.floor(round(random.uniform(0, 1), 3) * 9999)
    return rannonce
#========================================================================================================================
def autoseed(token):
    seed = hashlib.sha256(f"seedaccess-entropyverror-apiv10.{token}".encode()).digest()
    return seed
#========================================================================================================================
def sleepy(tokentype):
      print(red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
            magenta(f"[{tokentype}Token] ") +
            red(f"Waiting ..."))
#========================================================================================================================
def bot_owo(token, tokentype, channelid):
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": "owo",        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
        magenta(f"[{tokentype}]") +     
        blue(" OwO ✅ ")    
        )
#========================================================================================================================
def bot_hunt(token, timehunt, tokentype, channelid):
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": prefix + "hunt",        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
        magenta(f"[{tokentype}]") +     
        blue(" Hunt ✅ (" + str(timehunt) + " ms)")    
        )
#========================================================================================================================
def bot_battle(token, timebattle, tokentype, channelid):
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": prefix + "battle",        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
        magenta(f"[{tokentype}]") +     
        blue(" Battle ✅ (" + str(timebattle) + " ms)")    
        )   
#========================================================================================================================
def get_ran_mess():
    grm = random.randint(0, (len(phrases)-1))
    return phrases[grm]
#========================================================================================================================
def get_ran_act():
    gra = random.randint(0, (len(actvar)-1))
    return actvar[gra]
#========================================================================================================================
def get_ran_gamble():
    gra = random.randint(0, (len(gamblevar)-1))
    return gamblevar[gra]
#========================================================================================================================
def ran_message(token, channelid):
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": get_ran_mess(),        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
#========================================================================================================================
def bot_animals(token, tokentype, channelid, a_type):
    animalcheck = False
    animaltypes = ""
    ranks = [
        "common",
        "uncommon",
        "rare",
        "epic",
        "mythical",
        "patreon",
        "cpatreon",
        "legendary",
        "gem",
        "bot",
        "distorted",
        "fabled",
        "special",
        "hidden",
    ]
    for e in ranks:
        if animaltype[e] == "true":
            animaltypes += f"{e} "

    if a_type == "sacrifice" or a_type == "sell" or a_type == "sac":
        animalcheck = True

    if animalcheck:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": f"owo {a_type} {animaltypes}",
                "nonce": nonce(),
                "tts": False,
                "flags": 0,
            },
        )
        print( 
            red(f"{time.strftime('%H:%M:%S')} ") + 
            magenta(f"[{tokentype}] ") +
            blue(f"Animals ✅ / Type: {a_type}"))
    else:
        print(
            red(f"{time.strftime('%H:%M:%S')} ") + 
            magenta(f"[{tokentype}] ") + 
            blue(f"[{tokentype}] Animals ❌ / Error: Incorrect Type"))
#========================================================================================================================
def bot_pray(token, tokentype, channelid, pray):
    if pray == "true":
        if (tokentype == "Extra Token") :
            ct = prefix + "pray"
            bt = "Pray"
        else:
            ct = prefix + "pray"
            bt = "Pray"
    elif pray == "main":
        if (tokentype == "Extra Token"):
            ct = prefix + "pray <@" + main_id + ">"
            bt = "Pray to main"
        else:
            ct = prefix + "pray"
            bt = "Pray"
    elif pray == "extra":
        if (tokentype == "Extra Token"):
            ct = prefix + "pray"
            bt = "Pray"
        else:
            ct = prefix + "pray <@" + extra_id + ">"
            bt = "Pray to extra"
    else:
        ct = " "
        bt = " "
            
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": ct,        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
        magenta(f"[{tokentype}] ") +
        yellow( bt +"✅")
    )
#========================================================================================================================
def bot_curse(token, tokentype, channelid, curse):
    ct = None
    if curse == "true":
        if (tokentype == "Extra Token") :
            ct = prefix + "curse"
            bt = "Curse"
        else:
            ct = prefix + "curse"
            bt = "Curse"
    elif curse == "main":
        if (tokentype == "Extra Token"):
            ct = prefix + "curse <@" + main_id + ">"
            bt = "Curse to main"
        else:
            ct = prefix + "pray"
            bt = "Pray"
    elif curse == "extra":
        if (tokentype == "Extra Token"):
            ct = prefix + "pray"
            bt = "Pray"
        else:
            ct = prefix + "curse <@" + extra_id + ">"
            bt = "Curse to extra"
    else:
        ct = ""
        bt = ""
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": ct,        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
        magenta(f"[{tokentype}] ") +
        yellow( bt + "✅")
    )
#========================================================================================================================
def cookie(token, tokentype, channelid):
    if (tokentype == "Extra Token"):
        ct = prefix + "cookie <@"+ main_id + ">"
    else :
        ct = prefix + "cookie <@"+ extra_id +">"
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": ct,        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
        magenta(f"[{tokentype}]") +
        yellow(" Cookie ✅")
    )
#========================================================================================================================
def daily(token, tokentype, channelid):
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": prefix + "daily",        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
        magenta(f"[{tokentype}]") +
        yellow(" Daily ✅")
    )
#========================================================================================================================
def bot_coinflip(token, tokentype, channelid):
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": prefix + "coinflip " + coinflip_amount,        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
        magenta(f"[{tokentype}]") +
        yellow(" Gamble / CoinFlip ✅ / Amount: " +
                coinflip_amount)
    )
#========================================================================================================================
def bot_slots(token, tokentype, channelid):
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": prefix + "coinflip " + slots_amount,        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
        magenta(f"[{tokentype}]") +
        yellow(" Gamble / slots ✅ / Amount: " +
                slots_amount)
    )
#========================================================================================================================
def upgradeall(token, tokentype, channelid):
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": prefix + "upgrade " + upg_type + " all",        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
        magenta(f"[{tokentype}]") +
        yellow(" Upgrade AutoHunt ✅ ")
    )
#▒█▀▀█ █░░█ █▀▀ █▀▀ ▀▀█▀▀ 　 █▀▀█ █▀▀▄ █▀▀▄ 　 ▒█░░░ ░▀░ █▀▀ ▀▀█▀▀ 
#▒█░▒█ █░░█ █▀▀ ▀▀█ ░░█░░ 　 █▄▄█ █░░█ █░░█ 　 ▒█░░░ ▀█▀ ▀▀█ ░░█░░ 
#░▀▀█▄ ░▀▀▀ ▀▀▀ ▀▀▀ ░░▀░░ 　 ▀░░▀ ▀░░▀ ▀▀▀░ 　 ▒█▄▄█ ▀▀▀ ▀▀▀ ░░▀░░
def dailycount():
    with open(file_cache, 'r', encoding='utf-8') as c:
        data = json.load(c)
    dailychecker = data["dailychecker"]
    base_time = datetime.time(7, 0, 0)
    day_base = datetime.datetime.strptime(data["day_daily"], "%Y-%m-%d").date()
    base_datetime = datetime.datetime.combine(day_base, base_time)
    base_datetime_utc = base_datetime.replace(tzinfo=pytz.utc)
    now_utc = datetime.datetime.now(pytz.utc)
    print(f"{base_datetime}\n{base_datetime_utc}\n{now_utc}")
    if (base_datetime_utc < now_utc):
        data["dailychecker"] = "ready"
        with open(file_cache, "w", encoding='utf-8') as s:
            json.dump(data, s)
            dailychecker == "ready"
        return dailychecker
    else:
        dailychecker == "done"
        return dailychecker

def checklist(token, tokentype, channelid):
    dailychecker = dailycount()
    print(dailychecker)
    if dailychecker == "ready":
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": f"{prefix}cl",        
                'nonce': nonce(),
                "tts": False,
                "flags": 0,
                    },
        )
        print(
            red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ")+
            magenta(f"[{tokentype}] ") +
            blue(f"Sending Checklist📜...")
        )
        while True:
            response = requests.get(
                f"https://discord.com/api/v9/channels/{channelid}/messages?limit=1",
                headers={"authorization": token},
            )
            try:
                body = response.json()
                author = body[0]["author"]
                id = author["id"]
                if (id == "408785106942164992"):
                    embeds = body[0]["embeds"]
                    cont = embeds[0]["description"]
                    print(
                    red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ")+
                    magenta(f"[{tokentype}] ")+
                    blue(f"Getting Checklist🔎..."))
                    print(green(f"{cont}"))
                    if "☑️ 🎉" in cont:
                        with open(file_cache, "r", encoding='utf-8') as d:
                            data = json.load(d)
                        now_utc = datetime.datetime.now(pytz.utc)
                        data["day_daily"] = now_utc.strftime("%Y-%m-%d")
                        data["dailychecker"] = "done"
                        with open(file_cache, "w", encoding='utf-8') as e:
                            json.dump(data, e)

                        return "checklist completed"
                    elif "⬛ 🎁" in cont:
                        daily(token, tokentype, channelid)
                    elif "⬛ 🍪" in cont:
                        cookie(token, tokentype, channelid)
                    elif "⬛ 📝" in cont:
                        print(
                            magenta((f"[{tokentype}] ") +
                            blue(f"YOUR DAILY VOTE IS AVAILABLE!"))
                        )
                    break
                else:
                    continue
            except (KeyError, json.JSONDecodeError) as e:
                if isinstance(e, IndexError) and str(e) == "list index out of range":
                    print(red("Unable to get Checklist❗"))
                    return
                else:
                    print(
                        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
                        magenta(f"[{tokentype}] ") +
                        red("Unable to get Checklist❗")
                    )
        time.sleep(0.01)
#========================================================================================================================
def run__bot__captcha(token, tokentype, channelid, dmchannelid):
    while True:
        global active_bot, capcha_flag, task_bot_active, captcha_check_var, main_thread, extra_thread
        response = requests.get(
            f"https://discord.com/api/v9/channels/{channelid}/messages?limit=1",
            headers={"authorization": token}
        )
        responsedm = requests.get(
            f"https://discord.com/api/v9/channels/{dmchannelid}/messages?limit=1",
            headers={"authorization": token}
        )
        with open(file_cache, 'r', encoding='utf-8') as f:
            data = json.load(f)
        id_DM = data["capcha_id_Dm"]
        id_message = data["capcha_id_message"]
        try:
            body = response.json()
            content = body[0]["content"]
            author = body[0]["author"]
            id = author["id"]
            id_mess= body[0]["id"]
            
            bodydm = responsedm.json()
            contentmd = bodydm[0]["content"]
            authordm = bodydm[0]["author"]
            iddm = authordm["id"]
            id_messdm= bodydm[0]["id"]
            if (body == None ):
                    dmprotectprouwu(token, channelid, tokentype)
            elif ((("captcha" in content) or ("Are you a real human?" in  contentmd)) and 
                ((id == "408785106942164992")or(iddm == "408785106942164992")) and 
                (id_mess != id_message) and 
                (id_messdm != id_DM) and 
                capcha_flag == False):
                data["capcha_id_Dm"] = id_mess
                data["capcha_id_message"] = id_messdm
                with open(file_cache, "w", encoding="utf-8") as g:
                    json.dump(data, g)
                active_bot = False
                print(
                    red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
                    magenta(f"[{tokentype}]") +
                    red(f"Chat Captcha! ❌")
                )
                active_bot = False
                task_bot_active = False
                captcha_check_var = True
                capcha_flag = True
                main_thread.join()
                extra_thread.join()
                time.sleep(10)
                notification_def(tokentype)
        except (KeyError, json.JSONDecodeError) as e:
            print(
                red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
                magenta(f"[{tokentype}]") +
                red(f"Error while checking captcha! ⚠️")
            )
#========================================================================================================================
def dmprotectprouwu(token, channelid, tokentype):    
    try: 
        requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token, "super-x": autoseed()},
        json={
            "content": "hi bro",        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
    except (KeyError, json.JSONDecodeError) as e:
        print(
            red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
            magenta(f"[{tokentype}]") +
            red(" OwO dm channel id incorrect ❌ ")
        )
#========================================================================================================================
def checkinv(token, channelid, tokentype):
    if gemcheck == "true":
        response = requests.get(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token}
        )
        body = response.json()
        cont = body[0]['content']
        if "You found:" in cont or "and caught a" in cont:
            collection = ["alulu"]
            print(
                red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
                magenta(f"[{tokentype}]") +
                blue("inventory checking 🔍 (type-1)")
            )
            if "gem1" not in cont:
                collection.append("huntgem")
            if "gem3" not in cont:
                collection.append("empgem")
            if "gem4" not in cont:
                collection.append("luckgem")
            if "gem1" in cont and "gem3" in cont and "gem4" in cont:
                getinv(token, channelid, tokentype, "nogem", ["nocollection"])
            else:
                getinv(token, channelid, tokentype, "gemvar", collection)
    else:
        print(
            f"{datetime.datetime.now().strftime('%H:%M:%S')} [{tokentype}] inventory checking 🔍 (type-2)"
        )
        getinv(token, channelid, tokentype, "nogem", ["nocollection"])
#========================================================================================================================
def getinv(token, channelid, tokentype, gemc, collectc):
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": prefix + "inv",
            "tts": False,
            "flags": 0,
                },
    )
    time.sleep(3)
    response = requests.get(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token}
    )
    body = response.json()
    cont = body[0]['content']
    if gemc == "gemvar":
        empgem = ""
        empgemstatus = False
        luckgem = ""
        luckgemstatus = False
        huntgem = ""
        huntgemstatus = False
        specialgem = ""
        specialgemstatus = False
        gem = ""
        gemusebro = False

        if "huntgem" in collectc:
            if "`057`" in cont:
                huntgem = "57"
                huntgemstatus = True
            elif "`056`" in cont:
                huntgem = "56"
                huntgemstatus = True
            elif "`055`" in cont:
                huntgem = "55"
                huntgemstatus = True
            elif "`054`" in cont:
                huntgem = "54"
                huntgemstatus = True
            elif "`053`" in cont:
                huntgem = "53"
                huntgemstatus = True
            elif "`052`" in cont:
                huntgem = "52"
                huntgemstatus = True
            elif "`051`" in cont:
                huntgem = "51"
                huntgemstatus = True

        if "empgem" in collectc:
            if "`071`" in cont:
                empgem = "71"
                empgemstatus = True
            elif "`070`" in cont:
                empgem = "70"
                empgemstatus = True
            elif "`069`" in cont:
                empgem = "69"
                empgemstatus = True
            elif "`068`" in cont:
                empgem = "68"
                empgemstatus = True
            elif "`067`" in cont:
                empgem = "67"
                empgemstatus = True
            elif "`066`" in cont:
                empgem = "66"
                empgemstatus = True
            elif "`065`" in cont:
                empgem = "65"
                empgemstatus = True

        if "luckgem" in collectc:
            if "`078`" in cont:
                luckgem = "78"
                luckgemstatus = True
            elif "`077`" in cont:
                luckgem = "77"
                luckgemstatus = True
            elif "`076`" in cont:
                luckgem = "76"
                luckgemstatus = True
            elif "`075`" in cont:
                luckgem = "75"
                luckgemstatus = True
            elif "`074`" in cont:
                luckgem = "74"
                luckgemstatus = True
            elif "`073`" in cont:
                luckgem = "73"
                luckgemstatus = True
            elif "`072`" in cont:
                luckgem = "72"
                luckgemstatus = True

        if "specialgem" in collectc:
            if "`085`" in cont:
                specialgem = "85"
                specialgemstatus = True
            elif "`084`" in cont:
                specialgem = "84"
                specialgemstatus = True
            elif "`083`" in cont:
                specialgem = "83"
                specialgemstatus = True
            elif "`082`" in cont:
                specialgem = "82"
                specialgemstatus = True
            elif "`081`" in cont:
                specialgem = "81"
                specialgemstatus = True
            elif "`080`" in cont:
                specialgem = "80"
                specialgemstatus = True
            elif "`079`" in cont:
                specialgem = "79"
                specialgemstatus = True

        if huntgemstatus:
            gem += f" {huntgem}"
            gemusebro = True
        if empgemstatus:
            gem += f" {empgem}"
            gemusebro = True
        if luckgemstatus:
            gem += f" {luckgem}"
            gemusebro = True
        if specialgemstatus:
            gem += f" {specialgem}"
            gemusebro = True
        if gemusebro:
            gemuse(token, gem, channelid, tokentype)

    if lootboxcheck == "true":
        if "`050`" in cont:
            time.sleep(2)
            boxuse(token, "lootbox all", channelid, tokentype)

    if fabledlootboxcheck == "true":
        if "`049`" in cont:
            time.sleep(2)
            boxuse(token, "lootbox fabled all", channelid, tokentype)

    if cratecheck == "true":
        if "`100`" in cont:
            time.sleep(2)
            boxuse(token, "crate all", channelid, tokentype)
#========================================================================================================================
def boxuse(token, box, channelid, tokentype):
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": prefix + box,        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
        magenta(f"[{tokentype}]") +     
        yellow(box + " ✅")    
    )
#========================================================================================================================
def gemuse(token, gem, channelid, tokentype):
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": prefix + "use " + gem,        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
        magenta(f"[{tokentype}]") + 
        yellow(" Gem ✅")
            )
#========================================================================================================================
def questprayme(tokenrd, useridst, channelid, pro1, pro2):
    np = pro2 - pro1
    global quest, active_bot, pray
    pray = "false"
    for np in range (np, 0, -1):
        if active_bot:
            requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": tokenrd},
            json={
                "content": prefix + f"pray <@{useridst}>",        
                'nonce': nonce(),
                "tts": False,
                "flags": 0,
                    },
                )
            time.sleep(300)
            if np == 1:
                quest = True
                pray = str(setting['pray'])
        else:
            break
#========================================================================================================================
def questcurseme(tokenrd, useridst, channelid, pro1, pro2):
    np = pro2 - pro1
    global quest, active_bot, curse
    for np in range (np, 0, -1):
        if active_bot:
            curse = "false"
            requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": tokenrd},
            json={
                "content": prefix + f"curse <@{useridst}>",        
                'nonce': nonce(),
                "tts": False,
                "flags": 0,
                    },
                )
            time.sleep(300)
            if np == 1:
                curse = str(setting['curse'])
                quest = True
        else:
            break
#========================================================================================================================
def questbattlefriend(tokenst, tokenrd, useridst, channelid, pro1, pro2):
    np = pro2 - pro1
    for np in range (np, 0, -1):
        global quest, active_bot, battle
        battle = "false"
        if active_bot:
            requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": tokenrd},
            json={
                "content": prefix + f"battle <@{useridst}>",        
                'nonce': nonce(),
                "tts": False,
                "flags": 0,
                    },
                )
            time.sleep(3)
            requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": tokenst},
            json={
                "content": prefix + "ab",        
                'nonce': nonce(),
                "tts": False,
                "flags": 0,
                    },
                )
            time.sleep(17)
            if np == 1:
                battle = str(setting['battle'])
                quest = True
        else:
            break
#========================================================================================================================
def questuseactionreceive(tokenrd, useridst, channelid, pro1, pro2):
    np = pro2 - pro1
    global quest, active_bot
    for np in range (np, 0, -1):
        if active_bot:
            
            requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": tokenrd},
            json={
                "content": prefix + f"{get_ran_act()} <@"+ useridst +">",        
                'nonce': nonce(),
                "tts": False,
                "flags": 0,
                    },
                )
            time.sleep(10)
            if np == 1:
                quest = True
        else:
            break
#========================================================================================================================
def questuseactiongive(token, channelid, pro1, pro2):
    np = pro2 - pro1
    global quest, active_bot
    for np in range (np, 0, -1):
        if active_bot:
            
            requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": prefix + f"{get_ran_act()} <@408785106942164992>",        
                'nonce': nonce(),
                "tts": False,
                "flags": 0,
                    },
                )
            time.sleep(10)
            if np == 1:
                quest = True
        else:
            break
#========================================================================================================================
def questgamble(token, channelid, pro1, pro2) :
    np = pro2 - pro1
    global quest
    for np in range (np, 0, -1):
        global active_bot
        if active_bot:
            requests.post(
                f"https://discord.com/api/v9/channels/{channelid}/messages",
                headers={"authorization": token},
                json={
                    "content": prefix + get_ran_gamble(),        
                    'nonce': nonce(),
                    "tts": False,
                    "flags": 0,
                        },
                )
            time.sleep(16)
            if np == 1:
                quest = True
        else:
            break
#========================================================================================================================
def questsayowo(token, channelid, pro1, pro2):
    np = pro2 - pro1
    global quest, active_bot
    if owo != "true":
        for np in range(np, 0, -1):
            if active_bot:
                bot_owo(token, "OwO Quest", channelid)
                time.sleep(16)
                if np == 1:
                    quest = True
            else:
                break
#========================================================================================================================
def doquest(questss,tokenst,tokenrd,useridst,channelid,progress1,progress2):
    global quest
    quests = questss
    print(quests)
    if (("Say 'owo'") in  quests):
        quest = False
        if owo != "true":
            do_questsayowo = threading.Thread(
                target=questsayowo, 
                args=(
                    tokenst,
                    channelid,
                    int(progress1), 
                    int(progress2)
                )
            )
            return do_questsayowo.start()
    elif (("Gamble") in quests and
            (slots_enable != "true"  or
            coinflip_enable != "true")):
            quest = False
            do_questgamble = threading.Thread(
                target=questgamble, 
                args=(
                    tokenst,
                    channelid,
                    int(progress1),
                    int(progress2)
                )
            )
            return do_questgamble.start()
    elif (("Use an action command on someone") in quests):
        quest = False
        do_questuseactiongive = threading.Thread(
            target=questuseactiongive, 
            args=(
                tokenst,
                channelid,
                int(progress1),
                int(progress2)
            )
        )
        return do_questuseactiongive.start()
    if extratokencheck == "true":
        if (("Have a friend curse you" in quests )):
            quest = False
            do_questcurseme = threading.Thread(
                target=questcurseme,
                args=(
                    tokenrd, 
                    useridst,
                    channelid,
                    int(progress1),
                    int(progress2)
                )
            )
            return do_questcurseme.start()
        elif (("Have a friend pray to you") in quests):
            quest = False
            do_questprayme = threading.Thread(
                target=questprayme,
                args=(
                    tokenrd, 
                    useridst,
                    channelid,
                    int(progress1),
                    int(progress2)
                )
            )
            return do_questprayme.start()
        elif (("Battle with a friend") in quests):
                quest = False
                do_questbattlefriend = threading.Thread(
                    target=questbattlefriend,
                    args=(
                        tokenst, 
                        tokenrd,
                        main_id,
                        channelid,
                        int(progress1),
                        int(progress2)
                    )
                )
                return do_questbattlefriend.start()
        elif (("Have a friend use an action command on you") in quests):
            quest = False
            do_questuseactionreceive = threading.Thread(
                target=questuseactionreceive,
                args=(
                    tokenrd, 
                    useridst,
                    channelid,
                    int(progress1),
                    int(progress2)
                )
            )
            return do_questuseactionreceive.start()
        
def get_quest_1(cont, conts):
    try:
        aquests = cont[0]["description"].split("**1. ")[1].split("**")[0]
        aprogress1 = cont[0]["description"].split("Progress: [")[1].split("/")[0]
        aprogress2 = cont[0]["description"].split("/")[1].split("]")[0]

        avarlock_quest_ = "**1. "
        avarlock_quest__ = "]`"
        avarlock_quest___ = "<:blank:427371936482328596>`‣ 🔒 Locked`"
        achecklockquest = cont[0]["description"].split("**1. ")[1].split("]")[0]
        ajoinvar1 = "".join([avarlock_quest_, achecklockquest, avarlock_quest__])
        ajoinvar2 = "\n".join([ajoinvar1, avarlock_quest___])

        if ajoinvar2 in conts:
            aquests = ""
            aprogress1 = ""
            aprogress2 = ""
            return aquests, aprogress1, aprogress2
        else:
            aquests = quest_filter(aquests)
            return aquests, aprogress1, aprogress2
    except IndexError:
        aquests = ""
        aprogress1 = ""
        aprogress2 = ""
        return aquests, aprogress1, aprogress2

def get_quest_2(cont, conts):
    try:
        bquests = cont[0]["description"].split("**2. ")[1].split("**")[0]
        bcheckquest1 = cont[0]["description"].split("**2. ")[1].split("Progress: [")[0]
        bvar1 = "Progress: ["
        bcheckquest11 = "".join([bcheckquest1, bvar1])
        bprogress1 = cont[0]["description"].split(bcheckquest11)[1].split("/")[0]
        bvar2 = "/"
        bcheckquest2 = "".join([bcheckquest11, bprogress1, bvar2])
        bprogress2 = cont[0]["description"].split(bcheckquest2)[1].split("]")[0]
        bquests = quest_filter(bquests)

        bvarlock_quest_ = "**2. "
        bvarlock_quest__ = "]`"
        bvarlock_quest___ = "<:blank:427371936482328596>`‣ 🔒 Locked`"
        bchecklockquest = cont[0]["description"].split("**2. ")[1].split("]")[0]
        bjoinvar1 = "".join([bvarlock_quest_, bchecklockquest, bvarlock_quest__])
        bjoinvar2 = "\n".join([bjoinvar1, bvarlock_quest___])

        if bjoinvar2 in conts:
            bquests = ""
            bprogress1 = ""
            bprogress2 = ""
            return bquests, bprogress1, bprogress2
        else:
            bquests = quest_filter(bquests)
            return bquests, bprogress1, bprogress2
    except IndexError:
        bquests = ""
        bprogress1 = ""
        bprogress2 = ""
        return bquests, bprogress1, bprogress2

def get_quest_3(cont, conts):
    try:
        cquests = cont[0]["description"].split("**3. ")[1].split("**")[0]
        ccheckquest1 = cont[0]["description"].split("**3. ")[1].split("Progress: [")[0]
        cvar1 = "Progress: ["
        ccheckquest11 = "".join([ccheckquest1, cvar1])
        cprogress1 = cont[0]["description"].split(ccheckquest11)[1].split("/")[0]
        cvar2 = "/"
        ccheckquest2 = "".join([ccheckquest11, cprogress1, cvar2])
        cprogress2 = cont[0]["description"].split(ccheckquest2)[1].split("]")[0]
        cquests = quest_filter(cquests)

        cvarlock_quest_ = "**3. "
        cvarlock_quest__ = "]`"
        cvarlock_quest___ = "<:blank:427371936482328596>`‣ 🔒 Locked`"
        cchecklockquest = cont[0]["description"].split("**3. ")[1].split("]")[0]
        cjoinvar1 = "".join([cvarlock_quest_, cchecklockquest, cvarlock_quest__])
        cjoinvar2 = "\n".join([cjoinvar1, cvarlock_quest___])

        if cjoinvar2 in conts:
            cquests = ""
            cprogress1 = ""
            cprogress2 = ""
            return cquests, cprogress1, cprogress2
        else:
            cquests = quest_filter(cquests)
            return cquests, cprogress1, cprogress2
    except IndexError:
        cquests = ""
        cprogress1 = ""
        cprogress2 = ""
        return cquests, cprogress1, cprogress2

def quest_filter(quest):
    if "Say 'owo'" in quest:
        quest == "Say 'owo'"
    elif "Gamble" in quest:
        quest == "Gamble"
    elif "Use an action command on someone" in quest:
        quest == "Use an action command on someone"
    elif "Battle with a friend" in quest:
        quest == "Battle with a friend"
    elif "Have a friend curse you" in quest:
        quest == "Have a friend curse you"
    elif "Have a friend pray to you" in quest:
        quest == "Have a friend pray to you"
    elif "Have a friend use an action command on you" in quest:
        quest == "Have a friend use an action command on you"
    return quest
    
def timecount():
    with open(file_cache, 'r', encoding='utf-8') as h:
        data = json.load(h)
    questchecker = data["questchecker"]
    base_time = datetime.time(7, 0, 0)
    day_base = datetime.datetime.strptime(data["day_daily"], "%Y-%m-%d").date()
    base_datetime = datetime.datetime.combine(day_base, base_time)
    base_datetime_utc = base_datetime.replace(tzinfo=pytz.utc)
    now_utc = datetime.datetime.now(pytz.utc)
    if (base_datetime_utc < now_utc):
        data["questchecker"] = "ready"
        with open(file_cache, "w", encoding='utf-8') as i:
            json.dump(data, i)
            questchecker == "ready"
        return questchecker
    else:
        questchecker == "done"
        return questchecker
        
def getquests(tokenst,tokenrd,useridst,channelid, tokentype):
    questchecker = timecount()
    global quest, active_bot
    aquests = ""
    bquests = ""
    cquests = ""
    if (active_bot)and(questchecker == "ready"):
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": tokenst},
            json={
                "content": f"{prefix}quest",        
                'nonce': nonce(),
                "tts": False,
                "flags": 0,
                },
        )
        time.sleep(2)
        response = requests.get(
            f"https://discord.com/api/v9/channels/{channelid}/messages?limit=1",
            headers={"authorization": tokenst}
        )
        try:
            body = response.json()
            cont = body[0]["embeds"]
            conts = cont[0]["description"]
            time.sleep(2)
            if "You finished all of your quests!" in cont[0]['description']:
                with open(file_cache, "r", encoding='utf-8') as j:
                    data = json.load(j)
                now_utc = datetime.datetime.now(pytz.utc)
                data["day_quest"] = now_utc.strftime("%Y-%m-%d")
                data["questchecker"] = "done"
                with open(file_cache, "w", encoding='utf-8') as k:
                    json.dump(data, k)

                print(red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                    magenta(f"[{tokentype}]") +
                    yellow(" You have already finished all of your quests!")
                )
            else:
                varquest1 = get_quest_1(cont,conts)
                aquests, aprogress1, aprogress2 = varquest1
                varquest2 = get_quest_2(cont, conts)
                bquests, bprogress1, bprogress2 = varquest2
                varquest3 = get_quest_3(cont, conts)
                cquests, cprogress1, cprogress2 = varquest3                
                if (aquests == bquests) and (aquests == cquests):
                    progress2 = max(aprogress2, bprogress2, cprogress2)
                    progress1 = min(aprogress1, bprogress1, cprogress1)
                    do_quest_1 = threading.Thread(target=doquest, args=(aquests,tokenst,tokenrd,useridst,channelid,progress1,progress2))
                    return do_quest_1.start()
                elif (((aquests == bquests) or (aquests == cquests)or(bquests == cquests)) and ((aquests != "") and (bquests != ""))):
                    if (aquests == bquests):
                        progress2 = max(aprogress2, bprogress2)
                        progress1 = min(aprogress1, bprogress1)
                        do_quest_2 = threading.Thread(target=doquest, args=(aquests,tokenst,tokenrd,useridst,channelid,progress1,progress2))
                        do_quest_2.start
                        if cquests != "":
                            if (("pray" or "curse") in aquests) and (("pray" or "curse") in cquests):
                                progress = int(progress2) - int(progress1)
                                time.sleep(progress * 60 * 5)
                                do_quest_2_1= threading.Thread(target=doquest, args=(cquests,tokenst,tokenrd,useridst,channelid,cprogress1,cprogress2))
                                do_quest_2_1.start
                            else:
                                do_quest_2_2= threading.Thread(target=doquest, args=(cquests,tokenst,tokenrd,useridst,channelid,cprogress1,cprogress2))
                                do_quest_2_2.start
                    elif (cquests != ""):
                        if (aquests == cquests):
                            progress2 = max(aprogress2, cprogress2)
                            progress1 = min(aprogress1, cprogress1)
                            do_quest_3 = threading.Thread(target=doquest, args=(aquests,tokenst,tokenrd,useridst,channelid,progress1,progress2))
                            do_quest_3.start
                            if (("pray" or "curse") in aquests) and (("pray" or "curse") in bquests):
                                progress = int(progress2) - int(progress1)
                                time.sleep(progress * 60 * 5)
                                do_quest_3_1 = threading.Thread(target=doquest, args=(bquests,tokenst,tokenrd,useridst,channelid,bprogress1,bprogress2))
                                do_quest_3_1.start
                            else:
                                do_quest_3_2 = threading.Thread(target=doquest, args=(bquests,tokenst,tokenrd,useridst,channelid,bprogress1,bprogress2))
                                do_quest_3_2.start
                        elif (bquests == cquests):
                            progress2 = max(aprogress2, cprogress2)
                            progress1 = min(aprogress1, cprogress1)
                            do_quest_4 = threading.Thread(target=doquest, args=(bquests,tokenst,tokenrd,useridst,channelid,progress1,progress2))
                            do_quest_4.start
                            if (("pray" or "curse") in aquests) and (("pray" or "curse") in bquests):
                                progress = int(progress2) - int(progress1)
                                time.sleep(progress * 60 * 5)
                                do_quest_4_1 = threading.Thread(target=doquest, args=(aquests,tokenst,tokenrd,useridst,channelid,aprogress1,aprogress2))
                                do_quest_4_1.start
                            else:
                                do_quest_4_2 = threading.Thread(target=doquest, args=(aquests,tokenst,tokenrd,useridst,channelid,aprogress1,aprogress2))
                                do_quest_4_2.start
                else:
                    if (("pray" or "curse") in aquests) and (("pray" or "curse") in bquests):
                        do_quest1 = threading.Thread(target=doquest, args=(aquests,tokenst,tokenrd,useridst,channelid,aprogress1,aprogress2))
                        do_quest1.start()
                        aprogress = int(aprogress2) - int(aprogress1)
                        if cquests != "":
                            do_quest3 = threading.Thread(target=doquest, args=(cquests,tokenst,tokenrd,useridst,channelid,cprogress1,cprogress2))
                            do_quest3.start()
                            pass
                        time.sleep(aprogress * 60 * 5)
                        do_quest2 = threading.Thread(target=doquest, args=(bquests,tokenst,tokenrd,useridst,channelid,bprogress1,bprogress2))
                        do_quest2.start()
                    elif (("pray" or "curse") in aquests) and (("pray" or "curse") in cquests):
                        do_quest1 = threading.Thread(target=doquest, args=(aquests,tokenst,tokenrd,useridst,channelid,aprogress1,aprogress2))
                        do_quest1.start()
                        do_quest2 = threading.Thread(target=doquest, args=(bquests,tokenst,tokenrd,useridst,channelid,bprogress1,bprogress2))
                        do_quest2.start()
                        aprogress = int(aprogress2) - int(aprogress1)
                        time.sleep(aprogress * 60 * 5)
                        do_quest3 = threading.Thread(target=doquest, args=(cquests,tokenst,tokenrd,useridst,channelid,cprogress1,cprogress2))
                        do_quest3.start()
                    elif (("pray" or "curse") in bquests) and (("pray" or "curse") in cquests):
                        do_quest2 = threading.Thread(target=doquest, args=(bquests,tokenst,tokenrd,useridst,channelid,bprogress1,bprogress2))
                        do_quest2.start()
                        do_quest1 = threading.Thread(target=doquest, args=(aquests,tokenst,tokenrd,useridst,channelid,aprogress1,aprogress2))
                        do_quest1.start()
                        bprogress = int(bprogress2) - int(bprogress1)
                        time.sleep(bprogress * 60 * 5)
                        do_quest3 = threading.Thread(target=doquest, args=(cquests,tokenst,tokenrd,useridst,channelid,cprogress1,cprogress2))
                        do_quest3.start()
                    else:
                        do_quest1 = threading.Thread(target=doquest, args=(aquests,tokenst,tokenrd,useridst,channelid,aprogress1,aprogress2))
                        do_quest1.start()
                        if bquests != "":
                            do_quest2 = threading.Thread(target=doquest, args=(bquests,tokenst,tokenrd,useridst,channelid,bprogress1,bprogress2))
                            do_quest2.start()
                        elif cquests != "":
                            do_quest3 = threading.Thread(target=doquest, args=(cquests,tokenst,tokenrd,useridst,channelid,cprogress1,cprogress2))
                            do_quest3.start()
        except (KeyError, json.JSONDecodeError) as e:
            print(
                red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
                magenta(f"[{tokentype}] ") +
                red("Unable to check quest❗")
        )
    else:
        pass
#██████╗░██╗░░░██╗███╗░░██╗  ██████╗░░█████╗░████████╗
#██╔══██╗██║░░░██║████╗░██║  ██╔══██╗██╔══██╗╚══██╔══╝
#██████╔╝██║░░░██║██╔██╗██║  ██████╦╝██║░░██║░░░██║░░░
#██╔══██╗██║░░░██║██║╚████║  ██╔══██╗██║░░██║░░░██║░░░
#██║░░██║╚██████╔╝██║░╚███║  ██████╦╝╚█████╔╝░░░██║░░░
#╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝  ╚═════╝░░╚════╝░░░░╚═╝░░░
def bot_main():
    response = requests.get(
            f"https://canary.discord.com/api/v9/users/@me",
            headers={"authorization": main_token}
        )
    try:
            body = response.json()
            if (str(body) == "401: Unauthorized"):
                    print(red(f"Main Token / {str(body)}"))
                    time.sleep(5)
                    exit(0)
            else:
                print(green(f"Main Token ✅"))
                print(blue(f"[Main Token] User:{body["username"]}{body["discriminator"]}"))
                checklist(main_token, "Main Token", main_channelid)
                sleepy("Main")
                print(green("Main Token ✅"))
    except (KeyError, json.JSONDecodeError) as e:
            print(
                red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
                magenta("[Main Token]") +
                red(f"Error while checking Main Token! ⚠️")
            )
#========================================================================================================================
def bot_extra():
    global etoken
    if (extratokencheck == "true"):
        time.sleep(2)
        etoken = True
        response = requests.get(
            f"https://canary.discord.com/api/v9/users/@me",
            headers={"authorization": extra_token}
        )
        try:
                body = response.json()
                if (str(body) == "401: Unauthorized"):
                        print(red(f"Extra Token / {str(body)}"))
                        time.sleep(5)
                        exit(0)
                else:
                    print(green(f"Extra Token ✅"))
                    print(blue(f"[Extra Token] User:{body["username"]} {body["discriminator"]}"))
                    checklist(extra_token, "Extra Token", extra_channelid)
                    sleepy("Extra")
                    print(green("Extra Token ✅"))
        except (KeyError, json.JSONDecodeError) as e:
                print(
                    red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                    magenta("[Extra Token]") +
                    red(f"Error while checking Extra Token! ⚠️")
                )
    else:
        etoken = False
#▒█▀▀█ █▀▀█ █░░ █░░ 　 █░░ █▀▀█ █▀▀█ █▀▀█ 
#▒█░░░ █▄▄█ █░░ █░░ 　 █░░ █░░█ █░░█ █░░█ 
#▒█▄▄█ ▀░░▀ ▀▀▀ ▀▀▀ 　 ▀▀▀ ▀▀▀▀ ▀▀▀▀ █▀▀▀
#========================================================================================================================
def run__bot__hunt__and__battle(tokens, tokentypes, channelids):
     while True:
        global active_bot
        if active_bot:
            timehunt = rantime()
            timebattle = timehunt + 1
            if ("true" in hunt):
                time.sleep(timehunt)
                timehunts = round(timehunt, 3)
                bot_hunt(tokens, timehunts, tokentypes, channelids)
                if (inventorycheck == "true"):
                    time.sleep(1)
                    checkinv(tokens, channelids, tokentypes)
            if ("true"in battle):
                time.sleep(timebattle + 5)
                timebattles = round(timebattle, 3)
                bot_battle(tokens, timebattles, tokentypes, channelids) 
        else:
            break
        time.sleep(15)
#========================================================================================================================
def run__bot__animal(tokens, tokentypes, channelid, a_types):
     while True:
        global active_bot
        if active_bot:
            bot_animals(tokens, tokentypes, channelid, a_types)
        else:
            break
        time.sleep(60)
#========================================================================================================================
def run__bot__say__owo(tokens, tokentypes, channelids):
     while True:
        global active_bot
        if active_bot:
            owosay = rantime()
            if (owosay >= 3):
                owosay - 3
            time.sleep(owosay)
            bot_owo(tokens, tokentypes, channelids)
        else:
            break
        time.sleep(15)
#========================================================================================================================
def run__bot__pray(tokens, tokentypes, channelids, prays):
     while True:
        global active_bot
        if active_bot:
            bot_pray(tokens, tokentypes, channelids, prays)
        else:
            break
        time.sleep(5.1 * 60)
#========================================================================================================================
def run__bot__curse(tokens, tokentypes, channelids, curses):
     while True:
        global active_bot
        if active_bot:
            bot_curse(tokens, tokentypes, channelids, curses)
        else:
            break
        time.sleep(5.1 * 60)
#========================================================================================================================
def run__bot__upgrade(tokens, tokentypes, channelids):
     while True:
        global active_bot
        if active_bot:
            upgradeall(tokens, tokentypes, channelids)
        else: 
            break
        time.sleep(10 * 60)
#========================================================================================================================
def run__bot__gamble(tokens, tokentypes, channelids):
    while True:
        global active_bot
        if active_bot:
            if (slots_enable == "true"):
                bot_slots(tokens, tokentypes, channelids)
        else:
            break
        time.sleep(18)
#░█████╗░░█████╗░██╗░░░░░██╗░░░░░  ██████╗░░█████╗░████████╗
#██╔══██╗██╔══██╗██║░░░░░██║░░░░░  ██╔══██╗██╔══██╗╚══██╔══╝
#██║░░╚═╝███████║██║░░░░░██║░░░░░  ██████╦╝██║░░██║░░░██║░░░
#██║░░██╗██╔══██║██║░░░░░██║░░░░░  ██╔══██╗██║░░██║░░░██║░░░
#╚█████╔╝██║░░██║███████╗███████╗  ██████╦╝╚█████╔╝░░░██║░░░
#░╚════╝░╚═╝░░╚═╝╚══════╝╚══════╝  ╚═════╝░░╚════╝░░░░╚═╝░░░


def main_account():
    bot_main_thread = threading.Thread(target=bot_main)
    run__bot__hunt__and__battle_thread = threading.Thread(target=run__bot__hunt__and__battle, args=(main_token, "Main Token", main_channelid))
    run__bot__animal_thread = threading.Thread(target=run__bot__animal, args=(main_token, "Main Token", main_channelid, a_type))
    run__bot__say__owo_thread = threading.Thread(target=run__bot__say__owo, args=(main_token, "Main Token", main_channelid))
    run__bot__pray_thread = threading.Thread(target=run__bot__pray, args=(main_token, "Main Token", main_channelid, pray))
    run__bot__curse_thread = threading.Thread(target=run__bot__curse, args=(main_token, "Main Token", main_channelid, curse))
    run__bot__upgrade_thread = threading.Thread(target=run__bot__upgrade, args=(main_token, "Main Token", main_channelid))
    run__bot__gamble_thread = threading.Thread(target=run__bot__gamble, args=(main_token, "Main Token", main_channelid))
    run__bot__getquests_thread = threading.Thread(target=getquests, args=(main_token, extra_token, main_id, main_questchannelid, "Main Token"))
    bot_main_thread.start()
    time.sleep(10)
    if autoquest == "true":
        time.sleep(2)
        run__bot__getquests_thread.start() 
    run__bot__say__owo_thread.start()
    run__bot__hunt__and__battle_thread.start()
    time.sleep(5)
    run__bot__pray_thread.start()
    run__bot__curse_thread.start()
    time.sleep(5)
    run__bot__upgrade_thread.start()
    run__bot__gamble_thread.start()
    run__bot__animal_thread.start()

def extra_account():
    global etoken
    if extratokencheck == "true":
        bot_extra_thread = threading.Thread(target=bot_extra)
        extra__run__bot__hunt__and__battle_thread = threading.Thread(target=run__bot__hunt__and__battle, args=(extra_token, "Extra Token", extra_channelid))
        extra__run__bot__animal_thread = threading.Thread(target=run__bot__animal, args=(extra_token, "Extra Token", extra_channelid, a_type))
        extra__run__bot__say__owo_thread = threading.Thread(target=run__bot__say__owo, args=(extra_token, "Extra Token", extra_channelid))
        extra__run__bot__pray_thread = threading.Thread(target=run__bot__pray, args=(extra_token, "Extra Token", extra_channelid, pray))
        extra__run__bot__curse_thread = threading.Thread(target=run__bot__curse, args=(extra_token, "Extra Token", extra_channelid, curse))
        extra__run__bot__upgrade_thread = threading.Thread(target=run__bot__upgrade, args=(extra_token, "Extra Token", extra_channelid))
        extra__run__bot__gamble_thread = threading.Thread(target=run__bot__gamble, args=(extra_token, "Extra Token", extra_channelid))
        extra__run__bot__getquests_thread = threading.Thread(target=getquests, args=(extra_token, main_token, extra_id, extra_questchannelid, "Extra Token"))
        bot_extra_thread.start()
        time.sleep(10)
        if etoken:
            if autoquest == "true":
                extra__run__bot__getquests_thread.start() 
            extra__run__bot__say__owo_thread.start()
            extra__run__bot__hunt__and__battle_thread.start()
            time.sleep(5)
            extra__run__bot__pray_thread.start()
            extra__run__bot__curse_thread.start()
            time.sleep(5)
            extra__run__bot__animal_thread.start()
            extra__run__bot__upgrade_thread.start()
            extra__run__bot__gamble_thread.start()


def controller(token, channelid1, channelid2):
    def send_mess(messages):
        r1 = requests.post(f"https://discord.com/api/v9/channels/{channelid1}/messages",
        headers={"authorization": token},
        json={
            "content": messages,        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                }
        )
        r2 = requests.post(f"https://discord.com/api/v9/channels/{channelid2}/messages",
        headers={"authorization": token},
        json={
            "content": messages,        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                }
        )
    while True:
        global task_bot_active, active_bot, captcha_check_var , main_thread, extra_thread, capcha_flag
        response = requests.get(
            f"https://discord.com/api/v9/channels/{channelid1}/messages?limit=1",
            headers={"authorization": token},
            ) 
        response_ = requests.get(
            f"https://discord.com/api/v9/channels/{channelid2}/messages?limit=1",
            headers={"authorization": token},
            )
        body = response.json()
        author = body[0]["author"]
        id = author["id"]
        main_id_mess_ = body[0]["id"]

        body_ = response_.json()
        author_ = body_[0]["author"]
        id_ = author_["id"]
        extra_id_mess_ = body_[0]["id"]
        with open(file_cache, 'r', encoding='utf-8') as u:
            data = json.load(u)
        id_mess_main = data["activate_bot_id_main"]
        id_mess_extra = data["activate_bot_id_extra"]
        if (((id == main_id) or (id == extra_id) or (id_ == main_id) or (id_ == extra_id)) and
            (main_id_mess_ != id_mess_main) and
            (extra_id_mess_ != id_mess_extra)
            ):
            content_ = body_[0]["content"]
            content = body[0]["content"]
            data["activate_bot_id_main"] = main_id_mess_
            data["activate_bot_id_extra"] = extra_id_mess_
            with open(file_cache, "w", encoding="utf-8") as i:
                json.dump(data, i)
            if (content == f"{bot_prefix}stop") or (content_ == f"{bot_prefix}stop"):
                send_mess('Bot stopped!')
                active_bot = False
                task_bot_active = False
                
                main_thread.join()
                extra_thread.join()
            elif (content == f"{bot_prefix}run") or (content_ == f"{bot_prefix}run"):
                if task_bot_active == False:
                    send_mess('Bot is Runing!')
                    main_thread = threading.Thread(target=main_account)
                    extra_thread = threading.Thread(target=extra_account)

                    main_thread.start()
                    extra_thread.start()
                    captcha_check_var = False
                    task_bot_active = True
                    capcha_flag = False
                    active_bot = True
                else:
                    send_mess('Bot has already runned!')
            elif (content == f"{bot_prefix}reset") or (content_ == f"{bot_prefix}reset"):
                send_mess('Bot resetted!')
                active_bot = True
                capcha_flag = False
                time.sleep(1)

                main_thread.join()
                extra_thread.join()
                time.sleep(1)
                main_thread = threading.Thread(target=main_account)
                extra_thread = threading.Thread(target=extra_account)

                main_thread.start()
                extra_thread.start()
        time.sleep(0.01)    


if __name__ == '__main__':
    run__bot__captcha_thread = threading.Thread(target=run__bot__captcha, args=(main_token, "Main Token", main_channelid, main_owodmchannelid))
    run__bot__captcha_thread.start()
    if etoken:
        extra__run__bot__captcha_thread = threading.Thread(target=run__bot__captcha, args=(extra_token, "Extra Token", extra_channelid, extra_owodmchannelid))
        extra__run__bot__captcha_thread.start()

    
    main_thread = threading.Thread(target=main_account)
    extra_thread = threading.Thread(target=extra_account)

    main_thread.start()
    extra_thread.start()
    
    controller_thread = threading.Thread(target=controller, args=(main_token, main_channelid, extra_channelid))
    controller_thread.start()
    while True:
        time.sleep(1)

