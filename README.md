# WARP+ 推荐奖励 Telegram Bot

![warpplus](https://socialify.git.ci/Oreomeow/warpplus/image?description=1&descriptionEditable=Get%20WARP%2B%20referral%20quote%20and%20notify%20users%20with%20Telegram%20Bot&font=Raleway&forks=1&issues=1&language=1&logo=https%3A%2F%2Fraw.githubusercontent.com%2FOreomeow%2Fwarpplus%2Fmain%2FLogo.png&pattern=Floating%20Cogs&pulls=1&stargazers=1&theme=Light)

> 利用 **Telegram Bot** 获取 **WARP+** 推荐奖励流量并通知用户

## 功能 (Functions)

- [x] 刷取一定次数
  - [x] 不指定次数按 10～99 次刷取
  - [x] 指定次数刷取
  - [x] 刷取结果统计
- [ ] 设置定时任务
- [ ] 查询当前流量
- [ ] 支持他人刷取
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

- 修改 `config.json`

  ```json
  {
      "TOKEN": "# Telegram bot API Token (可在 @botfather 获取)",
      "REFERRER": "# WARP 应用内的设备 ID"
  }
  ```

### 运行测试

```bash
python3 warpplus.py
```

`Ctrl + C` 退出

### 持久化运行

使用 `tmux` 或者 `screen` 运行。例如 `tmux` 安装：

```bash
# Debian or Ubuntu
apt install tmux

# CentOS or RedHat
yum install tmux
```

`tmux` 使用：

```bash
tmux new -s warpplus
cd warpplus
python3 warpplus.py
```

然后键盘按下 `Ctrl + B D` 即可 detach 当前窗口。

## 命令 (Commands)

```text
plus - 输入正整数指定刷取次数，否则随机刷取 10~99 次
```

## 鸣谢 (Thanks)

- [ALIILAPRO/warp-plus-cloudflare](https://github.com/ALIILAPRO/warp-plus-cloudflare)

- [fscarmen/warp](https://github.com/fscarmen/warp)
