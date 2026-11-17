## Returns a 4 digit pin code as a string for user to guess
def engine_rnd():
    import random

    pin = "".join(random.choices("0123456789", k=4))
    return pin
