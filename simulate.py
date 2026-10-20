import json,sys
from hud_core import normalize
if len(sys.argv)!=2:
    raise SystemExit('usage: python3 simulate.py examples/yandex.json')
with open(sys.argv[1],encoding='utf-8') as f: event=json.load(f)
for profile in ('green_prefacelift','extended_hud'):
    print(profile, json.dumps(normalize(event,profile),ensure_ascii=False,indent=2))
