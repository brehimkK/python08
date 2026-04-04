import sys
import os


def is_venv() -> bool:
    #      current env != globale system Python
    return sys.prefix != sys.base_prefix


def get_python_info() -> str:
    return sys.executable  # full path to the Python interpreter


def get_env_name() -> str:
    return os.path.basename(sys.prefix)  # extracts the last part of the path


def get_env_path() -> str:
    return sys.prefix  # Where is this Python environment located on the system


def get_python_version() -> str:
    return f"python{sys.version_info.major}.{sys.version_info.minor}"


def get_site_packages() -> str:
    return os.path.join(
        sys.prefix,
        "lib",
        get_python_version(),
        "site-packages"
    )


def handle_outside() -> None:
    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {get_python_info()}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")

    env_placeholder = get_env_name()

    print(f"python -m venv {env_placeholder}")
    print(f"source {env_placeholder}/bin/activate # On Unix")
    print(f"{env_placeholder}\\Scripts\\activate # On Windows")


def handle_inside() -> None:
    env_name = get_env_name()

    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {get_python_info()}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {get_env_path()}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")
    print("Package installation path:")
    print(get_site_packages())


if __name__ == "__main__":
    if is_venv():
        handle_inside()
    else:
        handle_outside()
