<br>
<h1 align="center">OwO Farm Bot V0.0.0.1 </h1>

</p>

[❗・Important](#important)<br>
[👑・Features](#features)<br>
[⚙・data.json example](#configjson-example)<br>
[💎・Get Token](#get-token)<br>
[📍・OwO DM channel id](#owo-dm-channel-id)<br>
[⚠️・Captcha Alert](#captcha-alert)<br>
[🔗・Required Links](#required-links)<br>
[🎈・Usage](#usage)<br>


## ❗・Important
-   You should use 2 account for access dual auto quest
-   Use of this farm bot may lead to actions being taken against your OwO profile and/or your Discord account. I am not responsible for them.
-   DO NOT USE ONE CHANNEL FOR TWO ACCOUNTS, USE IT FOR 1 ACCOUNT ONLY.
-   Discord may restart as a result of discord rpc overload.
-   It can detect virus due to captcha(ban) bypasser please turn off your antivirus(not really).

## 👑・Features

-   Auto Hunt
-   Auto Battle
-   Inventory Check
    -   Auto Gem Use (beta)
    -   Auto Lootbox Use
    -   Auto Fabled Lootbox Use
    -   Auto Crate Use
    -   Auto Eventbox Use (like anniversary present or valentine's day)
-   Auto Gamble
    -   Auto Coinflip
    -   Auto Slots
-   Auto Animals Sell OR Sacrifice,
-   Auto Upgrade Autohunt
-   Auto Pray
-   Auto CheckList
    -   Auto Quest
    -   Auto Daily
    -   Auto Cookie
-   Captcha(Ban) Protection v0.0.0 (beta)
-   Discord-RPC
-   **Extra Token**
    -   All Main Token Features
    -   Auto Pray for Main Token

## ⚙・data.json example

```
{
    "settings": {
        "prefix": "owo",
        "bot_prefix": "! or any prefix this use to run bot like !run, !reset, !stop",
        "owo": "true or false",
        "pray": "true or false, main for pray to main or extra for pray to extra",
        "curse": "true or false,  main for curse to main or extra for curse to extra",
        "hunt": "true or false",
        "battle": "true or false",
        "autoquest": "true or false",
        "randommess": "true or false",
        "banbypass": "true or false",
        "extratoken": "true or false",
        "presence": "true or false",
        "auto_update": "true or false",
        "inventory": {
            "inventorycheck": "true or false",
            "gemcheck": "true or false",
            "lootboxcheck": "true or false",
            "fabledlootboxcheck": "true or false",
            "cratecheck": "true or false"
        },
        "animals": {
            "enable": "true or false",
            "type": "sell or sac",
            "animaltype": {
                "common": "true or false",
                "uncommon": "true or false",
                "rare": "true or false",
                "epic": "true or false",
                "mythical": "true or false",
                "patreon": "true or false",
                "cpatreon": "true or false",
                "legendary": "true or false",
                "gem": "true or false",
                "bot": "true or false",
                "distorted": "true or false",
                "fabled": "true or false",
                "special": "true or false",
                "hidden": "true or false"
            }
        },
        "upgradeautohunt": {
            "enable": "true or false",
            "upgtype": "efficiency, duration, cost, gain, exp or radar"
        },
        "gamble": {
            "coinflip": {
                "enable": "true or false",
                "amount": "any amount"
            },
            "slots": {
                "enable": "true or false",
                "amount": "any amount"
            }
        }
    },
    "main":{
        "token":"main token",
        "userid":"token user id",
        "channelid":"channel id for main token",
        "owodmchannelid":"owo bot dm channel id",
        "autoquestchannelid": "auto quest channel id" 
    },
    "extra":{
        "token":"extra token", 
        "userid":"extra token user id", 
        "channelid":"channel id for extra token", 
        "owodmchannelid":"extra token owo bot dm channel id",
        "autoquestchannelid": "auto quest channel id" 
    },

    "custom_presence": { you can watch how to create custom_presence 
        "client_id": "", https://www.youtube.com/watch?v=o-XdyzYijNw
        "state": "",
        "large_image": "",
        "small_image": "",
        "large_text": "",
        "small_text": "",
        "label1": "",
        "label2": "",
        "label_link1": "",
        "label_link2": ""
    }
}

```

## 💎・Get Token

```js
(webpackChunkdiscord_app.push([
    [""],
    {},
    (e) => {
        m = [];
        for (let c in e.c) m.push(e.c[c]);
    },
]),
m)
    .find((m) => m?.exports?.default?.getToken !== void 0)
    .exports.default.getToken();
```

## 📍・OwO DM channel id

![](https://raw.githubusercontent.com/HoshinoTsukiMio/OwO-farm-bot/main/images/owochannelid.jpg)

## ⚠️・Captcha Alert
!!! If you want the captcha alert to work properly, turn off do not disturb

![](https://raw.githubusercontent.com/HoshinoTsukiMio/OwO-farm-bot/main/images/captchaalert.png)



## 🔗・Required Links

[Python](https://www.python.org/downloads/)<br>
[Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701)<br>
[Farm Bot Zip File](https://github.com/HoshinoTsukiMio/OwO-farm-bot/archive/refs/heads/Main.zip)

## 🎈・Usage

```
> YOU NEED LATEST PYTHON !
> edit data.json it in data folder
```
