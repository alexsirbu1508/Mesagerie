


def int_to_binary(val):
    return str(val).encode("utf-8")


def binary_to_int(val):
    return int(val.decode("utf-8"))


def binary_to_str(val):
    return val.decode("utf-8")

def get_host():
    HOST = '10.152.5.14'
    return HOST