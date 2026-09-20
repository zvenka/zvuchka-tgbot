import json

def create_user(userID: str):
    with open("users.json", "r") as f:
        users = json.load(f)

    default_settings = {
        "activated": False,
        "default_mode": "mp3",
        "downloads": 0
    }

    users[userID] = default_settings

    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)


def user_exists(userID: str):
    with open("users.json", "r") as f:
        return userID in json.load(f)


def is_user_activated(userID: str):
    with open("users.json", "r") as f:
        users = json.load(f)
        user = users[userID]
        return user["activated"]

def delete_key(key: str):
    try:
        with open("keys.txt", "r") as f:
            lines = f.readlines()
        
        # Rewrite the file keeping only the keys that do not match the used one
        with open("keys.txt", "w") as f:
            for line in lines:
                if line.strip() != key:
                    f.write(line)
    except FileNotFoundError:
        pass

def activate_user(userID: str, key: str) -> bool:
    try:
        key_valid = False
        with open("keys.txt", "r") as f:
            for line in f:
                if key == line.strip():
                    key_valid = True
                    break
        
        if not key_valid:
            return False

        with open("users.json", "r") as f:
            users = json.load(f)
        
        if userID in users:
            users[userID]["activated"] = True
            with open("users.json", "w") as f:
                json.dump(users, f, indent=4)
            
            delete_key(key=key)
            return True
            
    except FileNotFoundError:
        print("Error: 'keys.txt' or 'users.json' file is missing.")
        
    return False