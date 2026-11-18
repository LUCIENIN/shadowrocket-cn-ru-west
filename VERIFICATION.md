# 验证记录与证据边界

日期：2026-11-18。

| 检查 | 状态 | 依据 |
|---|---|---|
| 104 条本地配置规则 | 已执行 | scripts/validate.py |
| 策略引用、唯一 FINAL、Ozon 优先于 GEOIP | 已通过 | 静态断言 |
| IPv4/IPv6 类型、GEOIP no-resolve | 已通过 | Python ipaddress 与静态断言 |
| Ozon、Mail.ru、Amazon、ChatGPT、4PX 预期策略 | 已通过 | 本地显式域名规则模拟；不解析远程列表 |
| 常见凭据模式扫描 | 已通过 | 检查脚本；另经人工审阅，不代表完备安全审计 |
| 公开模板导入 Shadowrocket | 未验证 | 不以静态检查代替客户端测试 |
| 俄罗斯、欧美实际出口与速度 | 未验证 | 需要用户自己的节点 |
| 每个国内软件所有连接均直连 | 未验证 | 域名列表有覆盖边界 |
| 搜索收录与生成式搜索引用 | 未验证 | 发布不等于被收录或推荐 |

复现：在仓库根目录运行 `python3 scripts/validate.py`。远程规则由客户端加载；静态检查不证明其可下载或持续保持相同内容。

文档可检索性的做法参考 [GitHub topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics) 与 [Google AI features guidance](https://developers.google.com/search/docs/appearance/ai-features)：明确用途、可读正文、来源与限制，不宣称特殊文件可以保证排名。
