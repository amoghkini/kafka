import random
import string

user_id = list(range(1, 1000))
recipient_id = list(range(1, 1000))

def generate_message() -> dict:
    random_user_id = random.choice(user_id)
    random_recipient_id = random.choice(recipient_id)
    message = {
        "user_id": random_user_id,
        "recipient_id": random_recipient_id,
        "message": "Hello, this is a message from user " + str(random_user_id) + " to recipient " + str(random_recipient_id)
    }
    return message

if __name__ == "__main__":
    for i in range(1000):
        message = generate_message()
        print(message)