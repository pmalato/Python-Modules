from sys import prefix, base_prefix
from os import getenv


def get_env_var(key: str) -> str | None:
    try:
        value = getenv(key)
        return value
    except KeyError as error:
        print("Error: ", error)
        return None


def main() -> None:
    is_venv = prefix != base_prefix
    if is_venv:
        print("\nORACLE STATUS: Reading the Matrix...")
        try:
            from dotenv import load_dotenv  # type: ignore
        except ImportError as error:
            print("Import error: ", error)
            print(
                "Install dotenv...\n"
                "command: 'pip install python-dotenv'")
            return None
        try:
            load_dotenv()
        except Exception as error:
            print("Error: ", error)
        matrix_mode = get_env_var("MATRIX_MODE")
        url = get_env_var("DATABASE_URL")
        api_key = get_env_var("API_KEY")
        log_level = get_env_var("LOG_LEVEL")
        zion_endpoint = get_env_var("ZION_ENDPOINT")
        if not matrix_mode or\
                not url or not api_key or\
                not log_level or not zion_endpoint:
            return None
    else:
        print("You forgot to enter the venv, bruh")


if __name__ == "__main__":
    main()
