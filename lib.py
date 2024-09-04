def parseFloat(message: str) -> float:
    answer = input(message)
    try:
        return float(answer)
    except ValueError:
        print(f"{answer} er ikke et godkjent tall. Prøv igjen!")
        return parseFloat(message)