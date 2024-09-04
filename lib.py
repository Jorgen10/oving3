def parseFloat(message):
    answer = input(message)
    try:
        return float(answer)
    except ValueError:
        print(f"{answer} er ikke et godkjent tall. Prøv igjen!")
        parseFloat(message)