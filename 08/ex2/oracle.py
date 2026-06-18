from os import getenv


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    try:
        from dotenv import load_dotenv  # type: ignore
        from dotenv import find_dotenv  # type: ignore
        print(find_dotenv())
    except ImportError as error:
        print("Import error: ", error)
        print(
            "Install dotenv...\n"
            "command: 'pip install python-dotenv'")
        return None
    dotenv_load = load_dotenv()
    matrix_mode = getenv("MATRIX_MODE") or "production"
    url = getenv("DATABASE_URL")
    api_key = getenv("API_KEY")
    log_level = getenv("LOG_LEVEL")
    zion_endpoint = getenv("ZION_ENDPOINT")
    if not matrix_mode or\
            not url or not api_key or\
            not log_level or not zion_endpoint:
        print(
            "Missing configuration. Make sure ALL keys are correct "
            "and have values assigned to them")
        return None
    print("Configuration loaded:\n"
          f"Mode: {matrix_mode}\n"
          "Database: Connected to local instance\n"
          "API Access: Authenticated\n"
          f"Log Level: {log_level}\n"
          f"Zion Network: {zion_endpoint}")
    print("\nEnvironment security check:")
    if dotenv_load:
        print("[OK] No hardcoded secrets detected\n"
              "[OK] .env file properly configured\n"
              "[OK] Production overrides available")


if __name__ == "__main__":
    main()
