# bd_wenku_cookie_qiandao
**百度文库签到**

需要的三方库：
```
pip install requests schedule
```

 VPS上执行：
`git@github.com:gyje/bd_wenku_cookie_qiandao.git`

修改`bdwenku_qiandao.py`中的cookie为自己的百度cookie

执行:
`nohup python3 bdwenku_qiandao.py > bdwk_qd.log 2>&1 &`
