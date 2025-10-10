import random
import string


def random_lower_string(leng=32) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=leng))
