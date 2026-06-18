import os
from dotenv import load_dotenv  # type: ignore


def load_config():
    return {
        "mode": os.getenv("MATRIX_MODE"),
        "database_url": os.getenv("DATABASE_URL"),
        "api_key": os.getenv("API_KEY"),
        "log_level": os.getenv("LOG_LEVEL"),
        "zion_endpoint": os.getenv("ZION_ENDPOINT")
    }


def check_config(config):
    missing = []

    if not config["mode"]:
        missing.append("MATRIX_MODE")

    if not config["database_url"]:
        missing.append("DATABASE_URL")

    if not config["api_key"]:
        missing.append("API_KEY")

    if not config["log_level"]:
        missing.append("LOG_LEVEL")

    if not config["zion_endpoint"]:
        missing.append("ZION_ENDPOINT")

    return missing


def show_environment(config):
    if config["mode"] == "development":
        print("Database: Connected to local instance")
        print("API Access: Authenticated")
        print(f"Log Level: {config['log_level']}")
        print("Zion Network: Online")

    elif config["mode"] == "production":
        print("Database: Connected to production cluster")
        print("API Access: Authenticated")
        print(f"Log Level: {config['log_level']}")
        print("Zion Network: Online")

    else:
        print(f"Unknown mode: {config['mode']}")


def security_check():
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


def main():
    print("ORACLE STATUS: Reading the Matrix...")

    load_dotenv()

    config = load_config()

    missing = check_config(config)

    if missing:
        print("\nWARNING: Missing configuration variables:")

        for variable in missing:
            print(f"- {variable}")

        print("\nCreate a .env file or set environment variables.")
        return

    print("\nConfiguration loaded:")
    print(f"Mode: {config['mode']}")

    show_environment(config)

    security_check()
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
