#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/07/27
# @Author  : Oreomeow
# @File    : warpplus.py
# @Software: PyCharm
import datetime
import json
import random
import string
import time
import urllib.request

from telegram.ext import CommandHandler, Updater

# Telegram bot API Token (可在 @botfather 获取)
TOKEN = ""
# WARP 应用内的设备 ID
REFERRER = ""


def genString(num):
    c = string.ascii_letters + string.digits
    return "".join(random.choice(c) for i in range(num))


def digitString(num):
    d = string.digits
    return "".join(random.choice(d) for i in range(num))


def randomSleep(mu=20.220727, sigma=0.3):
    return random.gauss(mu, sigma)


def run():
    try:
        install_id = genString(22)
        body = {
            "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
            "install_id": install_id,
            "key": "{}=".format(genString(43)),
            "locale": "es_ES",
            "referrer": REFERRER,
            "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
            "type": "Android",
            "warp_enabled": False,
        }
        data = json.dumps(body).encode("utf8")
        headers = {
            "Connection": "Keep-Alive",
            "Content-Type": "application/json; charset=UTF-8",
            "Host": "api.cloudflareclient.com",
            "User-Agent": "okhttp/3.12.1",
        }
        req = urllib.request.Request(
            f"https://api.cloudflareclient.com/v0a{digitString(3)}/reg", data, headers
        )
        with urllib.request.urlopen(req) as response:
            return 1 if '"referral_count":1' in response.read().decode("utf8") else 0
    except Exception as e:
        return e


def plus(update, context):
    chat_id = update.message.chat_id
    n = "".join(context.args)
    if not n:
        n = random.randint(10, 99)
        print(f"[!] 未输入数字，随机刷 {n} 次")
        context.bot.send_message(
            chat_id=chat_id,
            text=f"🎲 未输入数字，随机刷 {n} 次",
        )
    elif not n.isdigit() or n == "0":
        print("[!] 请输入一个正整数！")
        return context.bot.send_message(
            chat_id=chat_id,
            text="⚠️ 请输入一个正整数！",
        )
    else:
        n = int(n)
    g = 0
    b = 0
    start = time.time()
    while True:
        result = run()
        if result == 1:
            g += 1
            retry = randomSleep()
            print(f"[:)] {g} GB 流量已成功添加到你的账户！")
            context.bot.send_message(
                chat_id=chat_id,
                text=f"🍺 {g} GB 流量已成功添加到您的账户！",
            )
        elif result == 0:
            b += 1
            retry = randomSleep()
            print("[:(] 分享失败")
            context.bot.send_message(
                chat_id=chat_id,
                text="👻 分享失败",
            )
        else:
            b += 1
            retry = randomSleep(22.727153)
            print(result)
            context.bot.send_message(
                chat_id=chat_id,
                text=f"⛔️ {result}",
            )
        if g + b >= int(n):
            break
        print(f"[*] 等待 {retry} 秒，下一个请求即将发出")
        time.sleep(retry)
    end = time.time()
    context.bot.send_message(
        chat_id=chat_id,
        text=f"📊 WARP+ 推荐奖励统计\n📟 总次数：{g} 次成功 {b} 次失败\n🎉 成功率：{round(g / n * 100, 2)}%\n⏳ 总耗时：{round((end - start) / 60, 2)} min",
    )


if __name__ == "__main__":
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    plus_handler = CommandHandler("plus", plus)

    dispatcher.add_handler(plus_handler)

    updater.start_polling()
    updater.idle()
