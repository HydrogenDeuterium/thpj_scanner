# -*- coding: utf-8 -*-
"""
Created on 2020/2/2 19:45
版权所有（c）<2020> 11598
github:https://github.com/HydrogenDeuterium
反996许可证版本1.0
在符合下列条件的情况下，特此免费向任何得到本授权作品的副本（包括源代码、文件和/或相关内容，以下统称为“授权作品”）的个人和法人实体授权：被授权个人或法人实体有权以任何目的处置授权作品，包括但不限于使用、复制，修改，衍生利用、散布，发布和再许可：
1. 个人或法人实体必须在许可作品的每个再散布或衍生副本上包含以上版权声明和本许可证，不得自行修改。
2.
个人或法人实体必须严格遵守与个人实际所在地或个人出生地或归化地、或法人实体注册地或经营地（以较严格者为准）的司法管辖区所有适用的与劳动和就业相关法律、法规、规则和标准。如果该司法管辖区没有此类法律、法规、规章和标准或其法律、法规、规章和标准不可执行，则个人或法人实体必须遵守国际劳工标准的核心公约。
3.
个人或法人不得以任何方式诱导或强迫其全职或兼职员工或其独立承包人以口头或书面形式同意直接或间接限制、削弱或放弃其所拥有的，受相关与劳动和就业有关的法律、法规、规则和标准保护的权利或补救措施，无论该等书面或口头协议是否被该司法管辖区的法律所承认，该等个人或法人实体也不得以任何方法限制其雇员或独立承包人向版权持有人或监督许可证合规情况的有关当局报告或投诉上述违反许可证的行为的权利。
该授权作品是"按原样"提供，不做任何明示或暗示的保证，包括但不限于对适销性、特定用途适用性和非侵权性的保证。在任何情况下，无论是在合同诉讼、侵权诉讼或其他诉讼中，版权持有人均不承担因本软件或本软件的使用或其他交易而产生、引起或与之相关的任何索赔、损害或其他责任。
"""
import csv
import json
import time

import requests

ur = r"https://api.bilibili.com/x/web-interface/view?aid="


def crawl_rawdata(aid):
    url = ur + aid
    rawdata = requests.get(url)
    retry = 0
    while rawdata.status_code != 200 | retry < 3:
        rawdata = requests.get(url)
        retry += 1
    return rawdata.content


def encode_bin(content):
    return json.loads(content)


def encode_data(dct):
    # 会有删除稿件
    if dct["code"] != 0:
        return -1
    # 以下说明数据正常，继续获取数据
    data = dct["data"]
    # 视频av号
    aid = data["aid"]
    # 投稿时间（1970年1月1日后经过的秒数）
    pubdate = data["pubdate"]
    # 作者uid、名字
    oid = data['owner']["mid"]
    onm = data['owner']['name']
    statdata = data["stat"]
    view = statdata["view"]
    danmaku = statdata["danmaku"]
    reply = statdata["reply"]
    collection = statdata["favorite"]
    coin = statdata["coin"]
    datalist = [aid, pubdate, oid, onm, view, danmaku, reply, collection, coin]
    return datalist


def unit(id: str):
    rtun = encode_data(encode_bin(crawl_rawdata(id)))
    if rtun == -1:
        return [id, "0", "0", "0", "0", '0', '0', '0', '0']
    else:
        return rtun

t=time.time()
with open(r"th_videos.csv", "r")as f, open(r"th_video_data.csv", "w",encoding="utf-8", newline="")as g:
    csv_writer = csv.writer(g)
    for lines in f:
        print(lines[:-1])
        data = unit(lines[:-1])
        csv_writer.writerow(data)
t2=time.time()
abs_time=t2-t
print("abslutetime:",abs_time)

input()
