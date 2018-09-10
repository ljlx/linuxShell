豆豆微服务简要介绍
==
用户服务user
--
 

群组服务group
--
聊天服务chat 
调用了 message服务
--


**1.chat服务，包含群聊和单聊，公众号**
*2.用户和组织机构服务*
~~3.群服务（group)~~
4.

verify 
code 验证码服务
box 加好友时显示的验证框

buddy 好友服务
加好友，看好友信息

filter 我们无法使用的接口

badword已废弃，移到了ap里面了
cache 音影视频，聊天时 客户端需要的 

cloud 云盘。
collection 客户端收藏文件的服务，利用cloud的接口

ibs 面对面建群，近距离添加联系人和群。

online 在线用户服务，可以使用这个接口来查看在线的用户情况

operationlog.thrift操作日志服务，我们不应该使用

PCMar pc打包用的，我们不需要

Photo 图片资源，相册服务。

Recommend 推荐邀请码，推荐好友来使用，业务相关，需要写个具体的流程demo

routecenter 消息服务使用的，路由用户的打洞服务器

setting app和pc端 ，用户个人设置的服务 app->我-> 设置页面

share 朋友圈,只关注的是分享的内容,没有点赞和评论信息,里面关于评论类型的接口已废弃
commentCenter 是朋友圈的点赞和评论信息，不关注内容
（comment.thrift sharecomment.thrift 完全已废弃）

statistics 后台管理端， 统计的服务。

timestamp 时间stamp服务， 用于设备同步记录 版本控制用

vrvxin 公众平台，web平台调用的公众接口 和ddio调用的资源是互通
note：公众平台和聊天信息 最终都会保存到消息表，该表定时清理（运维配置清楚周期和策略）
公众平台发送时处理的逻辑是：图，影音媒体文件等,以素材的形式单独保存,

subkey.thrift 不需要
ThirdParty 第三方登陆接口，肯定不需要，这是项目定制开发留下来的。

platform 服务， 是ddio接口调用的服务

Emoticon 表情包服务



