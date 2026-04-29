import json, os

def start_genesis():
    print("🔱 SUPREME ENTITY: GENESIS PROTOCOL 🔱")
    key = input("Enter Master Key to activate: ")
    if key == "shree harivansh":
        os.makedirs("/root/supreme_core/vault", exist_ok=True)
        with open("/root/supreme_core/vault/creator.json", "w") as f:
            json.dump({"name": "Nemi Sir", "level": 0}, f)
        print("Sovereignty Claimed. System Initialized.")
        return True
    return False
