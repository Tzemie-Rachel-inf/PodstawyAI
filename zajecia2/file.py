import json

with open("database.json", encoding="utf-8") as f:
    model = json.load(f)

odpowiedzi = {}

for klucz, pytanie in model.items():
    if klucz.startswith("Q"):
        print(pytanie["text"])
        for i, odp in enumerate(pytanie["answers"], 1):
            print(f"  {i}. {odp}")
        while True:
            wybor = input("Wybierz numer: ").strip()
            if wybor.isdigit() and 1 <= int(wybor) <= len(pytanie["answers"]):
                odpowiedzi[klucz] = pytanie["answers"][int(wybor) - 1]
                break
            print("Nieprawidłowy wybór, spróbuj ponownie.")
        print()

pasujace = 0
for regula in model.get("rules", []):
    if all(odpowiedzi.get(q) == wartosc for q, wartosc in regula["if"].items()):
        pasujace += 1
        print("Diagnoza:", regula["then"]["diagnosis"])
        print("Akcja:", regula["then"]["action"])
        print()

if pasujace == 0:
    print("Brak rozwiązania skontaktuj się z agentem.")