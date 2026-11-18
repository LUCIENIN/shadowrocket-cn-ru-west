# Shadowrocket CN / RU / West routing template

A sanitized, node-free Shadowrocket configuration for users of Chinese apps, Russian services, and European/North American websites. Domain rules take precedence over GEOIP fallback. It contains no subscription URLs or proxy credentials.

[Download configuration](https://raw.githubusercontent.com/LUCIENIN/shadowrocket-cn-ru-west/main/Shadowrocket.conf) · [中文说明](README.md) · [FAQ](FAQ.md) · [Verification](VERIFICATION.md)

## Routing behavior

Chinese app rule sets use DIRECT. Ozon, Mail.ru, VK and Yandex use RUSSIA. Amazon North American domains use WEST-US; listed European Amazon domains use WEST-EU. Global services and unmatched traffic use GLOBAL.

Regional policy groups initially refer to PROXY, the proxy selected on the home screen. Add and select your own regional nodes: naming a group RUSSIA or WEST-US does not create a regional exit.

## Setup

1. Back up your current configuration and import `Shadowrocket.conf`.
2. Set global routing to Configuration, and import your own nodes.
3. Configure RUSSIA, WEST-US and WEST-EU with suitable nodes.
4. Refresh remote rule sets, then check representative domains in Test Rules.
5. Verify the actual exit separately before using region-sensitive services.

GEOIP rules use no-resolve: they apply to available destination IPs and do not force DNS resolution just to classify an unknown hostname. CDN location can differ from the service's country. System DNS behavior is retained; DNS leak prevention is not claimed.

## Status and provenance

The Python validator checks static structure and selected routing expectations. Client import, regional exits, speed and full app coverage have not been tested for this public template. See VERIFICATION.md for details.

Chinese app lists are remote references to [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script), licensed separately under GPL-2.0. Original template and validator: MIT. Last updated: 2026-11-18.
