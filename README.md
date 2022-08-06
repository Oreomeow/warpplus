# WARP+ 推荐奖励 Telegram Bot

![warpplus](https://socialify.git.ci/Oreomeow/warpplus/image?description=1&descriptionEditable=Get%20WARP%2B%20referral%20quota%20and%20notify%20users%20with%20Telegram%20Bot&font=Raleway&forks=1&issues=1&language=1&logo=https%3A%2F%2Fraw.githubusercontent.com%2FOreomeow%2Fwarpplus%2Fmain%2FLogo.png&pattern=Floating%20Cogs&pulls=1&stargazers=1&theme=Light)

> 利用 **Telegram Bot** 获取 **WARP+** 推荐奖励流量并通知用户

## 功能 (Functions)

- [x] 刷取一定次数
  - [x] 不指定次数按 +∞ 刷取
  - [x] 指定次数刷取
  - [x] 刷取结果统计
- [x] 添加管理命令
- [x] 支持他人刷取
- [x] 查询当前流量
- [ ] 设置定时任务
- [ ] 支持多种语言

## 部署 (Deploy)

> **Warning** 需要 Python >= 3.7

### 克隆仓库

```bash
git clone --depth=1 https://github.com/Oreomeow/warpplus && cd warpplus
```

### 安装依赖

```bash
pip3 install -r requirements.txt
```

### 配置参数

- 通过 [@BotFather](https://t.me/botfather) 获取 Bot API Token

- 通过 WARP APP 获取 ID

  [![WARP APP 图示](https://user-images.githubusercontent.com/62703343/136070323-47f2600a-13e4-4eb0-a64d-d7eb805c28e2.png)](https://github.com/fscarmen/warp)

- 根据 `config.example.json` 在同目录生成 `config.json` 配置文件

  ```json
  {
      "TOKEN": "# Telegram bot API Token (可在 @botfather 获取，如 10xxx4:AAFcqxxxxgER5uw)",
      "USER_ID": "# Telegram 用户 ID (给 @getidsbot 发送 /start 获取到的纯数字 ID，如 1434078534)",
      "GIFT_LIMIT": "# 限制其他用户单次刷取次数，如 10，不限制则输入 0",
      "REFERRER": "# WARP 应用 (如 1.1.1.1) 内的设备 ID",
  }
  ```

### 运行测试

```bash
python3 warpplus.py
```

`Ctrl + C` 退出

### 持久化运行

从以下方法中任选其一即可，或参考 [Linux 守护进程的启动方法](https://www.ruanyifeng.com/blog/2016/02/linux-daemon.html)

- [Systemd](https://www.ruanyifeng.com/blog/2016/03/systemd-tutorial-commands.html) (推荐)

  一键脚本

  ```bash
  bash install.sh
  ```

  查看 `warpplus` 状态

  ```bash
  systemctl status warpplus
  ```

  查看 `warpplus` 日志

  ```bash
  journalctl -u warpplus
  ```

  启动 `warpplus`

  ```bash
  systemctl start warpplus
  ```

  停止 `warpplus`

  ```bash
  systemctl stop warpplus
  ```

  重启 `warpplus`

  ```bash
  systemctl restart warpplus
  ```

  杀死 `warpplus` 所有子进程
  
  ```bash
  systemctl kill warpplus
  ```

- [nohup](https://www.runoob.com/linux/linux-comm-nohup.html)

  ```bash
  nohup python3 warpplus.py > warpplus.log 2>&1 &
  ```

  查看日志

  ```bash
  tail -f warpplus.log
  ```

- [Screen](https://www.runoob.com/linux/linux-comm-screen.html)

  1. 创建会话

     ```bash
     screen -S warpplus
     python3 warpplus.py
     ```

     然后，按下 `Ctrl + A` 和 `Ctrl + D` ，回到原来的会话

  2. 如果要查看日志，可以使用 `screen -r warpplus` ；如果要停掉会话，按下 `Ctrl + C` 和 `Ctrl + D`

- [Tmux](http://www.ruanyifeng.com/blog/2019/10/tmux.html)

  1. 安装

     ```bash
     # Debian or Ubuntu
     apt install -y tmux

     # CentOS or RedHat
     yum install -y tmux
     ```

  2. 新建会话

     ```bash
     tmux new -s warpplus
     python3 warpplus.py
     ```

  3. 分离会话

     ```bash
     tmux detach
     ```

     或键盘按下 `Ctrl + B D` 即可将当前会话与窗口分离

  4. 如果要查看日志，可以使用 `tmux attach -t warpplus` ；如果要杀死会话 `tmux kill-session -t warpplus`

### `/bind` 命令说明

```text
/bind <referrer> - 绑定 WARP 应用 (如 1.1.1.1) 内的设备 ID
/bind t <access_token> - 绑定 wgcf-account.toml 中的 access_token
/bind i <device_id> - 绑定 wgcf-account.toml 中的 device_id
/bind <access_token> <device_id> - 绑定成对
```

其中 `<referrer>` 和 `<device_id>` 其实是同一个，只是 `<referrer>` 可以在手机 APP `1.1.1.1` 中找到，而从 `wgcf-account.toml` 提取的 `<access_token>` 和 `<device_id>` 必须绑定成对，否则无法进行流量查询

在安装了 [wgcf](https://github.com/ViRb3/wgcf) 的机器上可以使用 `Scripts/get.sh` 进行快捷提取

也可以运行以下命令提取

```bash
if ! [ -f '/etc/wireguard/wgcf-account.toml' ]; then
    echo "wgcf-account.toml 文件不存在，请查看是否已安装 wgcf。相关仓库 https://github.com/fscarmen/warp"
else
    ACCESS_TOKEN=$(grep 'access_token' /etc/wireguard/wgcf-account.toml | cut -d \' -f2)
    DEVICE_ID=$(grep 'device_id' /etc/wireguard/wgcf-account.toml | cut -d \' -f2)

    echo "====================== 请复制以下内容 (不包括此行) ======================"
    echo "${ACCESS_TOKEN} ${DEVICE_ID}"
    echo "====================== 请复制以上内容 (不包括此行) ======================"
fi
```

## 命令 (Commands)

```text
start - 开始使用
query - 查询流量
plus - (<n>) 💂‍♂️管理员账号添加流量，不输入次数视为 +∞
bind - [点击查看具体用法] 绑定账号
unbind - 解除绑定
gift - (<n>) 获取流量，不输入次数视为 +∞
stop - 💂‍♂️管理员停止运行中的任务
```

## 贡献 (Contributors)

- [Silentely](https://github.com/Silentely)

## 鸣谢 (Thanks)

- [ALIILAPRO/warp-plus-cloudflare](https://github.com/ALIILAPRO/warp-plus-cloudflare)

- [fscarmen/warp](https://github.com/fscarmen/warp)
