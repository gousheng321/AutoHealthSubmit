# AutoHealthSubmit
Automatic submit daily health data
# 如何使用
**此分支在成功打卡的情况下不会发送邮件，仅在`打卡失败`时Github会发送一封邮件到你`Github账号关联的邮箱`**
<details>
<summary>配置</summary>

1. **点击右上角的`Fork`复制一份你的副本**
![Fork](https://github.com/Windmill-City/AutoHealthSubmit/blob/no-mail/Docs/Fork.png)

**你要切换分支来使用no-mail模式**
![切换默认分支](https://github.com/Windmill-City/AutoHealthSubmit/blob/no-mail/Docs/切换默认分支.png)
2. 然后在`Settings->Secrets`里面添加你的账号密码

在 New Secret 的 Name 填下面`大写`的变量名称，不能变
- `USERID` -- 学号
- `USERPASS` -- 密码
![操作流程](https://github.com/Windmill-City/AutoHealthSubmit/blob/no-mail/Docs/操作流程.png)
3. **点`Action`，里面会提示你Action是`关闭(Disabled)`的，你要`Enable`它**
   ![开启Action](https://github.com/Windmill-City/AutoHealthSubmit/blob/no-mail/Docs/开启Action.png)
   ![开启Action2](https://github.com/Windmill-City/AutoHealthSubmit/blob/no-mail/Docs/开启Action2.png)
</details>

<details>
<summary>手动运行</summary>

**这个脚本每天6：00自动触发**

点击右上角的Star测试运行，运行一次之后要UnStar再Star才会再运行
![运行](https://github.com/Windmill-City/AutoHealthSubmit/blob/no-mail/Docs/运行.png)

点`Action`看运行状态
![运行状态](https://github.com/Windmill-City/AutoHealthSubmit/blob/no-mail/Docs/运行状态.png)
</details>

<details>
<summary>脚本失效后如何更新</summary>

1. 首先点击`compare`
![比较](https://github.com/Windmill-City/AutoHealthSubmit/blob/no-mail/Docs/比较.png)
2. 然后选择仓库和分支，左边是你的右边是我的
![选择分支](https://github.com/Windmill-City/AutoHealthSubmit/blob/no-mail/Docs/选择分支.png)
**如果你切换了默认分支为`no-mail`，你要在左右两边都选`no-mail`**
3. 点`Create pull request`两次
![创建pr](https://github.com/Windmill-City/AutoHealthSubmit/blob/no-mail/Docs/创建pr.png)
![创建pr2](https://github.com/Windmill-City/AutoHealthSubmit/blob/no-mail/Docs/创建pr2.png)
4. 点`Merge pull request`
![merge](https://github.com/Windmill-City/AutoHealthSubmit/blob/no-mail/Docs/merge.png)
</details>

<details>
<summary>如何停止自动打卡</summary>

在`Settings->Action`里面选择`Disable Action`
![停止打卡](https://github.com/Windmill-City/AutoHealthSubmit/blob/no-mail/Docs/停止打卡.png)
</details>

# 参考文献
https://github.com/Saujyun/AutoAction
