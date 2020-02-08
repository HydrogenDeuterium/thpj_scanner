## TODOLIST:
1.东方视频专栏的爬取（需要找到tag对应的api以确定相关专栏）

2.全站视频的数据，包含[av号，投稿日期，点击，弹幕，回复，收藏，硬币]，工作量较大

3.东方up信息，约全越好，包含投稿信息
## 前言：
参考https://docs.google.com/document/d/1qrRvYhFaQgu3yoasjF70wSuT9DSoku-NwqvnHFwZx7k/edit?usp=sharing

数据来源：霜落xss.b站tag数据.链接：https://pan.baidu.com/s/1a5VWG1ps8Sztlo-wQemOAA 密码：6q1k
内含至2018年7月19日凌晨4点以来，b站所有视频的tag信息与tag名称与tag_id的对照表。


## api：
### 视频信息（全）
https://api.bilibili.com/x/web-interface/view?aid={aid}
输出：json格式
```
{'code': 0,//0表明稿件状态正常
 'message': '0',
 'ttl': 1,
 'data': {'bvid': '',
      'aid': 12,//av号
      'videos': 1,
      'tid': 17,//分区编号
      'tname': '单机游戏',//分区名称
      'copyright': 2,//版权信息，(不确定：1=自制，2=搬运)
      'pic': 'http://i1.hdslb.com/bfs/archive/b6cfbbecb0faa3e8b56ca4ba43844f0835ec21c4.jpg',
      //似乎是封面
      'title': '音乐与弹幕同步 3.⑤',//标题
      'pubdate': 1246619416,//发布日期，unix时间
      'ctime': 1497428709,//似乎为最后编辑时间，unix时间
      'desc': '[sina]22312570[/sina]',
      //视频简历
      'state': 0,
      'attribute': 49152,
      'duration': 293,//时间,秒
      'rights': {'bp': 0,
           'elec': 0,
           'download': 1,
           'movie': 0,
           'pay': 0,
           'hd5': 0,
           'no_reprint': 0,//禁止转载
           'autoplay': 1,
           'ugc_pay': 0,
           'is_cooperation': 0,
           'ugc_pay_preview': 0,
           'no_background': 0},
      'owner': {'mid': 4694544,//up的uid
           'name': 'AR-32764',//up的名称
           'face': 'http://i0.hdslb.com/bfs/face/f896a4a9c74eb011ead1fb8e6be317146da128fa.jpg'},
           //up头像
      'stat': {'aid': 12,//视频编号
           'view': 857344,//点击
           'danmaku': 6102,//弹幕
           'reply': 6753,//评论
           'favorite': 10005,//收藏
           'coin': 1420,//硬币
           'share': 1196,//分享
           'now_rank': 0,//当前全站排名，0表示没有上排名
           'his_rank': 0,//历史最高排名
           'like': 5572,//点赞
           'dislike': 0,//点踩
           'evaluation': ''},
      'dynamic': '',
      'cid': 5925828,
      'dimension': {'width': 0, 'height': 0, 'rotate': 0},//似乎是视频分辨率信息，早期视频为0
      'no_cache': False,
      'pages': [{'cid': 5925828,
            'page': 1,
            'from': 'vupload',
            'part': '',
            'duration': 293,
            'vid': '',
            'weblink': '',
            'dimension': {'width': 0, 'height': 0, 'rotate': 0}}],
      'subtitle': {'allow_submit': False, 'list': []}}}
```


### 视频信息（精简）
https://api.bilibili.com/x/web-interface/archive/stat?aid={aid}
  输出： JSON格式如下
```
"data":
      {
            "aid": "av号",
            "view": "播放数",
            "danmaku": "弹幕数",
            "reply": "评论数",
            "favorite": "收藏数",
            "coin": "硬币数",
            "share": "分享数",
            "now_rank": "未知",
            "his_rank": "最高全站日排名（0表示未曾上榜)",
            "no_reprint": "0表示默认 1表示未经作者授权禁止转载",
            "copyright": "1表示原创 2表示搬运"
      }
```

### tag信息
https://api.bilibili.com/x/tag/archive/tags?aid={aid}
输出： JSON格式如下`
```
"data": [
    {
          "tag_id": "tag编号",
          "tag_name": "tag名称",
          "cover": "tag封面",
          "content": "tag描述",
          "type": "未知",
          "state": "未知",
          "ctime": "tag创建时间（unixtime）",
          "count": {
                "view": 0,
                "use": 0,
                "atten": 0
          },
          "is_atten": 0,
          "likes": 0,
          "hates": 0,
          "attribute": 0,
          "liked": 0,
          "hated": 0
    },
    ...
]
```

### 专栏
https://api.bilibili.com/x/article/viewinfo?id={article_id}
输出： JSON格式如下（无中文解释者为未知）
```
{
    code: 0,
    data: {
        like: 0,
        attention: false, //我是否关注
        favorite: false,  //我是否收藏
        coin: 0,  //我投币数量
        stats: {
            view: 847,
            favorite: 207, //收藏
            like: 16, //喜欢
            dislike: 0, //不喜欢
            reply: 29,//回复
            share: 1,
            coin: 2 //硬币
        },
        view: 0, // 阅读
        title: "专栏行为准则", // 标题
        banner_url: "https://i0.hdslb.com/bfs/archive/b68d74c09cc378ed0175faabe3295c14fa6b7c77.jpg@272-232-1180-701a_90p.webp",
        mid: 91221505,
        author_name: "gggwvg", // 作者
        is_author: true,
        image_urls: [
            "https://i0.hdslb.com/bfs/article/653a2847c1bdb959859edc1ff30088309e5af5de.webp"
        ],
        origin_image_urls: [ //头图
            "https://i0.hdslb.com/bfs/archive/b68d74c09cc378ed0175faabe3295c14fa6b7c77.jpg_90p.webp"
        ],
        shareable: true,
        show_later_watch: true,
        show_small_window: true,
        in_list: false
    },
    message: "0",
    ttl: 1
}
```
### 其它api:
|||
|:---:|:---:|
|https://api.bilibili.com/x/web-interface/article/early?jsonp=jsonp&aid= |可以用于获取专栏作者信息 |
|https://api.bilibili.com/x/article/more?aid= |可以用于获取作者更多专栏 |
|https://space.bilibili.com/ajax/Bangumi/getList?mid= |订阅番剧 |
|https://space.bilibili.com/ajax/tags/getSubList?mid= |订阅标签|


### 部分信息来自
 https://github.com/uupers/BiliSpider/wiki/
