from random import randint

from zxcvbn import zxcvbn


def generate_password(options: dict) -> dict:
    """Function recieves options for generate password.
    Generates password using the options, returns it
    """
    length: str = validate_options(options)
    settings: list = options.get("options")
    password: str = ""
    for _ in range(length):
        setting = settings[randint(0, len(settings) - 1)]
        if setting == "1":
            password += chr(randint(65, 90))
        elif setting == "2":
            password += chr(randint(97, 122))
        elif setting == "3":
            password += str(randint(0, 9))
        elif setting == "4":
            password += chr(randint(33, 47))

    score = zxcvbn(password=password).get("score")
    return {"password": password, "score": score}


def validate_options(options: dict) -> int:
    """Function validates options
    Returns password length
    """
    length = options.get("length")
    if not length.isdigit():
        raise ValueError("Error: length must contains numbers from 0 to 9")
    elif not 4 <= int(length) <= 50:
        raise ValueError("Error: min = 4 : max = 50 length")
    elif not options.get("options"):
        raise ValueError("Error: you have to choose one of the options")
    return int(length)
