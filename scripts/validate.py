from pathlib import Path
import ipaddress
import re

root = Path(__file__).resolve().parents[1]
text = (root / 'Shadowrocket.conf').read_text()
section = ''
groups = {'DIRECT', 'PROXY', 'REJECT'}
rules = []
for raw in text.splitlines():
    line = raw.strip()
    if not line or line.startswith('#'):
        continue
    if line.startswith('['):
        section = line
    elif section == '[Proxy Group]':
        groups.add(line.split('=', 1)[0].strip())
    elif section == '[Rule]':
        rules.append(line.split(','))
assert sum(r[0] == 'FINAL' for r in rules) == 1
assert rules[-1] == ['FINAL', 'GLOBAL']
for r in rules:
    policy = r[1] if r[0] == 'FINAL' else r[2]
    assert policy in groups, r
    if r[0] in ('IP-CIDR', 'IP-CIDR6'):
        network = ipaddress.ip_network(r[1])
        assert (network.version == 6) == (r[0] == 'IP-CIDR6'), r
    if r[0] == 'GEOIP':
        assert len(r) == 4 and r[3] == 'no-resolve', r
        assert r[1] != 'EU'
assert next(i for i,r in enumerate(rules) if r[1] == 'ozon.ru') < next(i for i,r in enumerate(rules) if r[0] == 'GEOIP')
for host, expected in {'ozon.ru':'RUSSIA','mail.ru':'RUSSIA','amazon.de':'WEST-EU','amazon.com':'WEST-US','chatgpt.com':'GLOBAL','b.4px.com':'DIRECT'}.items():
    matches = [r[2] for r in rules if r[0] == 'DOMAIN-SUFFIX' and (host == r[1] or host.endswith('.' + r[1]))]
    assert matches[0] == expected, (host, matches)
for file in root.rglob('*'):
    if not file.is_file() or '.git' in file.parts:
        continue
    data = file.read_text()
    if file.name == 'validate.py':
        continue
    assert not re.search(r'(?:trojan|vmess|vless|ss)://|password\s*=|token\s*=|private[-_]?key\s*=|/Users/|HLK-Russia|Home-TLS', data, re.I), file
    assert not re.search(r'https?://[^\s,]+[?&](?:key|token|auth)=', data, re.I), file
print(f'PASS: {len(rules)} rules; policy, precedence, IPv6, representative routes, and privacy-pattern checks')
