import json
from pathlib import Path
import datetime

path = Path("worldcup26.json")

with path.open(encoding="utf-8") as f:
    wc26_results = json.load(f)



i = 1;
d = ""
for result in wc26_results:
    if d != result["date"]:
        d = result["date"]
        print(f"\n{d}")

    print(f"\tMatch {i}", end=" - ")
    print(f'{result["home"]} {result["home_score"]}-{result["away_score"]}{" " + result["notes"] if result["notes"] else ""} {result["away"]}', end = " ")
    print("- " + f'{result["studium"]}')
    i+= 1;
