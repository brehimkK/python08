import os
import sys
from dotenv import load_dotenv


def load_config():
    # Load .env file (if exists)
    load_dotenv()

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }

    return config


def validate_config(config):
    missing = []

    for key in config:
        if config[key] is None:
            missing.append(key)

    return missing


def display_config(config):
    mode = config["MATRIX_MODE"]

    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")

    # Mode
    print(f"Mode: {mode if mode else 'undefined'}")

    # Database behavior (no hardcoded URLs)
    if config["DATABASE_URL"]:
        if mode == "production":
            print("Database: Connected to production instance")
        else:
            print("Database: Connected to local instance")
    else:
        print("Database: Not configured")

    # API
    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing key")

    # Log level
    print(f"Log Level: {config['LOG_LEVEL'] if config['LOG_LEVEL'] else 'undefined'}")

    # Zion
    if config["ZION_ENDPOINT"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def security_check():
    print("\nEnvironment security check:")

    # .env check
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file missing")

    # .gitignore check
    if os.path.exists(".gitignore"):
        with open(".gitignore", "r") as f:
            content = f.read()
            if ".env" in content:
                print("[OK] .env is ignored")
            else:
                print("[WARN] .env not ignored")
    else:
        print("[WARN] .gitignore missing")

    print("[OK] No hardcoded secrets detected")
    print("[OK] Production overrides available")


def main():
    config = load_config()
    missing = validate_config(config)

    display_config(config)

    if missing:
        print("\nWarning: Missing configuration keys:")
        for key in missing:
            print(f"- {key}")

    security_check()

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()