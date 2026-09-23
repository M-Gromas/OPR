import requests
from pprint import pprint
import html
import random
vpr = int(input("koliko vprašanj želiš?"))
url = f"https://opentdb.com/api.php?amount={vpr}&category=23&difficulty=hard&type=multiple"
klic = requests.get(url).json()

vprašanja = klic["results"]
točke = 0
for v in vprašanja:
    prav = v["correct_answer"]
    odgovori = v["incorrect_answers"] + [prav]
    random.shuffle(odgovori)
    print("-"*80)
    print(html.unescape(v["question"]))
    for i, o in enumerate(odgovori):
        print(f"{i+1} - {o}")

    odgovor = int(input("Odgovor: "))
    print(prav == odgovori[odgovor-1])
    if odgovor == prav:
        točke+1
    if odgovor == v["incorrect_anwsers"]
