import json
import re
from itertools import chain

celebs: dict[str, list[str]] = {}
space_replacer = re.compile(r"\s+")
with open('celebs.txt', mode='tr') as f:
    for line in f.readlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        c = space_replacer.sub(' ', line)
        h = "".join(sorted(c.lower().replace('ё', 'е').strip()))
        if h in celebs:
            if c.lower() in [s.lower() for s in celebs[h]]:
                print(f"Повтор {c}")
                continue
            else:
                raise ValueError(f"Уже есть {repr(c)} в {celebs[h]}")
        else:
            celebs[h] = []
        celebs[h].append(c)

result = list(sorted(chain(*celebs.values())))

out = json.dumps(result, ensure_ascii=False)
with open("names.js", mode='tw', encoding='utf-8') as f:
    print(f"NAMES = {out}\n", file=f)