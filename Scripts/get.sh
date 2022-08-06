#!/usr/bin/env bash

if ! [ -f '/etc/wireguard/wgcf-account.toml' ]; then
    echo "wgcf-account.toml 文件不存在，请查看是否已安装 wgcf。相关仓库 https://github.com/fscarmen/warp"
else
    ACCESS_TOKEN=$(grep 'access_token' /etc/wireguard/wgcf-account.toml | cut -d \' -f2)
    DEVICE_ID=$(grep 'device_id' /etc/wireguard/wgcf-account.toml | cut -d \' -f2)

    echo "====================== 请复制以下内容 (不包括此行) ======================"
    echo "${ACCESS_TOKEN} ${DEVICE_ID}"
    echo "====================== 请复制以上内容 (不包括此行) ======================"
fi
