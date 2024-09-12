def check_first_letter(word: str, letter: str) -> bool:
    if word[0] == letter:
        print("match!")
        return True
    else:
        print("no match!")
        return False


def get_weather_report() -> str:
    weather: str = input("What is the weather?")
    if (weather == "rainy") or (weather == "cold"):
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather
