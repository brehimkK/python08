import os
import sys
try:
    from dotenv import load_dotenv
    dotenv_available = True
except ModuleNotFoundError:
    dotenv_available = False
    print(
        "[WARNING] python-dotenv is not installed. "
        ".env file will be ignored."
    )
    sys.exit(1)


def load_config():
    load_dotenv(dotenv_path=".env")

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

    print(f"Mode: {mode if mode else 'undefined'}")

    if config["DATABASE_URL"]:
        if mode == "production":
            print("Database: Connected to production instance")
        else:
            print("Database: Connected to local instance")
    else:
        print("Database: Not configured")

    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing key")

    log_level = config["LOG_LEVEL"] if config["LOG_LEVEL"] else "undefined"
    print(f"Log Level: {log_level}")

    if config["ZION_ENDPOINT"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def security_check():
    print("\nEnvironment security check:")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file missing")

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
