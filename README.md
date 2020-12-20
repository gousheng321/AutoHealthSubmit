# AutoHealthSubmit
Automatic submit daily health data
# 如何使用
**如果你仅在`打卡失败`时才要邮件通知看[这里](https://github.com/Windmill-City/AutoHealthSubmit/tree/no-mail)**

**如果你`不论打卡是否失败`都要邮件通知，看下文**
<details>
<summary>配置</summary>

0. 首先你要注册个163邮箱来发送邮件
![开通邮件服务](https://github.com/Windmill-City/AutoHealthSubmit/blob/main/开通邮件服务.png)
![授权](https://github.com/Windmill-City/AutoHealthSubmit/blob/main/授权.png)
1. 点击右上角的`Fork`复制一份你的副本
2. 然后在`Settings->Secrets`里面添加你的账号密码和邮箱信息

  在 New Secret 的 Name 填下面`大写`的变量名称，不能变
  - `USERID` -- 学号
  - `USERPASS` -- 密码
  - `MAIL_USERNAME` -- 用来发送邮件的163邮箱
  - `MAIL_PASSWORD` -- 163邮箱的授权密码(不是登录密码)
  - `MAIL_RESULT` -- 用来接收打卡情况的邮箱
![操作流程](https://github.com/Windmill-City/AutoHealthSubmit/blob/main/操作流程.png)
3. **点`Action`，里面会提示你Action是`关闭(Disabled)`的，你要`Enable`它**
</details>

<details>
<summary>手动运行</summary>

**这个脚本每天凌晨4：00自动触发**

点击右上角的Star测试运行，运行一次之后要UnStar再Star才会再运行
![运行](https://github.com/Windmill-City/AutoHealthSubmit/blob/main/运行.png)

点`Action`看运行状态
![运行状态](https://github.com/Windmill-City/AutoHealthSubmit/blob/main/运行状态.png)
</details>

<details>
<summary>脚本失效后如何更新</summary>

1. 首先点击`compare`
![比较](https://github.com/Windmill-City/AutoHealthSubmit/blob/main/比较.png)
2. 然后选择仓库和分支，左边是你的右边是我的
![选择分支](https://github.com/Windmill-City/AutoHealthSubmit/blob/main/选择分支.png)
**如果你切换了默认分支为`main`，你要在左右两边都选`main`**
3. 点`Create pull request`两次
![创建pr](https://github.com/Windmill-City/AutoHealthSubmit/blob/main/创建pr.png)
![创建pr2](https://github.com/Windmill-City/AutoHealthSubmit/blob/main/创建pr2.png)
4. 点`Merge pull request`
![merge](https://github.com/Windmill-City/AutoHealthSubmit/blob/main/merge.png)
</details>

<details>
<summary>如何停止自动打卡</summary>

在`Settings->Action`里面选择`Disable Action`
![停止打卡](https://github.com/Windmill-City/AutoHealthSubmit/blob/main/停止打卡.png)
</details>

# 参考文献
https://github.com/Saujyun/AutoAction
