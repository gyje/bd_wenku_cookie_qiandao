# bd_wenku_cookie_qiandao
**百度文库签到**

*没有做验证码识别,无法连续签到7天以上,待解决,现在使用没有任何意义,请放弃!*

需要的三方库：
```
pip install requests schedule
```

 VPS上执行：
`git@github.com:gyje/bd_wenku_cookie_qiandao.git`

修改`bdwenku_qiandao.py`中的cookie为自己的百度cookie

执行:
`nohup python3 bdwenku_qiandao.py > bdwk_qd.log 2>&1 &`
