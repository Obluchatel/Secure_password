import random, string
def secure_password():
    return  ''.join(random.sample(string.ascii_lowercase + string.digits + string.punctuation, 16))


if __name__ == "__main__":
    print(secure_password())
