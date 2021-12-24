import random, math

entrants = ["Enter",
            "Your",
            "Entrants",
            "Here"]

keys = ["Enter",
        "Your",
        "Keys",
        "Here"]


def gen():
    results = {}

    for i in range(0, len(entrants)):
        results[entrants[i]] = []

    for key in keys:
        winner = random.choice(entrants)
        results[winner].append(key)

    minkeys = 100000
    maxkeys = 0
    for k, v in results.items():
        keycount = len(v)
        if keycount > maxkeys:
            maxkeys = keycount
        if keycount < minkeys:
            minkeys = keycount

    keydiff = maxkeys - minkeys

    if keydiff < 4:
        print("\n\n\n\n\n\n\n\n\nACCEPTABLE ROLL FOUND!")
        for k, v in results.items():
            print(k)
            for j in v:
                print("\t" + j)
        return True
    else:
        print("Roll not deemed acceptable - too large of a difference between the most and least keys won. Rerolling...")
        return False


acceptable = False
while acceptable == False:
    acceptable = gen()
