# Shadowrocket CN / RU / West — 中国、俄罗斯与欧美分流

**Shadowrocket CN/RU/West** 是不含代理节点和订阅凭据的地区分流模板，面向同时使用中国软件、俄罗斯服务和欧美站点的用户。国内服务走 DIRECT，Ozon/Mail.ru 等走 RUSSIA，欧美业务使用独立策略组，GEOIP 只作后备判断。

[下载配置](https://raw.githubusercontent.com/LUCIENIN/shadowrocket-cn-ru-west/main/Shadowrocket.conf) · [English guide](README.en.md) · [FAQ](FAQ.md) · [验证记录与限制](VERIFICATION.md)

| 场景 | 示例 | 配置目标 | 需要用户完成 |
|---|---|---|---|
| 国内软件直连 | 网易云、抖音、微信、4PX | DIRECT | 更新远程专项规则并检查匹配 |
| 俄罗斯服务 | Ozon、Mail.ru、VK、Yandex | RUSSIA | 加入并选定自己的俄罗斯节点 |
| 北美业务 | amazon.com、amazon.ca | WEST-US | 加入并选定对应出口 |
| 欧洲业务 | amazon.de、amazon.fr、amazon.co.uk | WEST-EU | 加入并选定对应出口 |
| 全球服务 | ChatGPT、Google、GitHub、Telegram | GLOBAL | 选择可用的首页代理节点 |

策略名表示分流意图，不能证明实际出口国家。此项目不提供节点，也未完成公开模板的客户端导入和地区出口实测。

从个人使用场景整理的脱敏配置模板：国内软件直连，俄罗斯服务单独选出口，欧美业务分别选择策略组。没有节点、订阅、凭据或私人服务器信息。

## 使用

1. 在 Shadowrocket 导入 `Shadowrocket.conf`，全局路由选择「配置」。
2. 在首页导入你自己的节点。`PROXY` 使用首页当前节点。
3. `RUSSIA` 默认使用 `PROXY`。需要俄罗斯出口时，在 Shadowrocket 编辑这个组，加入并选择自己的俄罗斯节点。
4. `WEST-US`、`WEST-EU` 同样需要自行加入和选择对应地区节点。默认均使用 `PROXY`，组名不会自动改变出口国家。
5. 在「配置 → 测试规则」检查 `music.163.com`、`lf3-static.bytednsdoc.com`、`ozon.ru`、`mail.ru`、`amazon.de`、`amazon.com`、`chatgpt.com`。

不要直接用这个模板覆盖唯一的工作配置。先保留备份；本项目尚未完成端到端地区出口测试。

## 路由顺序

局域网 → 俄罗斯服务例外 → 国内软件专项列表 → 全球及欧美业务域名 → 中俄后缀 → GEOIP → GLOBAL 兜底。

- 中国：网易云音乐、抖音、微信、小红书、B站、快手、阿里、腾讯、百度、京东规则使用 DIRECT；补充 4PX、WPS、企业微信、ToDesk。
- 俄罗斯：Ozon、Mail.ru、VK、Yandex 及 `.ru`、`.su`、`.рф` 使用 RUSSIA。地区例外位于兜底之前。
- 欧美：Amazon 各站域名分别选组；已知 IP 的美国/加拿大和欧洲国家流量通过 GEOIP 分组。
- 全球：AI、Google、GitHub、Telegram 等明确域名及未匹配流量走 GLOBAL。

GEOIP 使用 `no-resolve`，避免仅为判断国家而强制解析未知域名。它仅在已有目标 IP 时补充分流，不保证未知域名一定命中国家规则。欧洲逐国列出，不假定存在 `GEOIP,EU`。CDN 所在地也不等于业务或用户所在地。

系统 DNS 沿用设备当前网络设置；未声称实现 DNS 防泄漏。域名/IP 分流也不等于按整个应用进程强制直连。

## 来源与更新

国内专项规则引用 [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script/tree/master/rule/Shadowrocket)，不将其完整规则复制进本仓库。上游许可证为 GPL-2.0，请遵循上游许可与声明。远程列表依赖网络和客户端刷新；上游变化可能改变匹配结果。没有添加定时更新服务。

本项目新增的模板与检查脚本使用 MIT 许可；此许可不覆盖第三方规则。保留原个人配置的业务意图，移除了私人出口绑定、固定私人主机映射和不明历史拦截项，因此不是原配置的逐行备份。

## 检查

运行 `python3 scripts/validate.py` 检查规则结构、策略引用、顺序、IPv6 类型和明显敏感数据；检查不替代 Shadowrocket 实测。

更新日期：2026-11-18。发布版未替换本机正在使用的配置。
