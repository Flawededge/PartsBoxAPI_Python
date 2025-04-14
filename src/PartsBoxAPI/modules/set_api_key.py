import os
from pathlib import Path
from loguru import logger

ENV_FILE: str = ".env"


def set_api_key() -> None:
    """
    Prompt the user for an API key and save it in a .env file.
    """
    api_key: str = input("Enter your PartsBox API key: ").strip()
    
    if not api_key:
        logger.error("No API key provided. Exiting without updating .env.")
        return

    env_path: Path = Path(ENV_FILE)
    env_contents: str = ""

    if env_path.exists():
        env_contents = env_path.read_text()

    # Remove any existing PARTSBOX_API_KEY variable.
    new_env_lines = []
    key_already_set: bool = False
    for line in env_contents.splitlines():
        if line.startswith("PARTSBOX_API_KEY="):
            new_env_lines.append(f"PARTSBOX_API_KEY={api_key}")
            key_already_set = True
        else:
            new_env_lines.append(line)

    if not key_already_set:
        new_env_lines.append(f"PARTSBOX_API_KEY={api_key}")

    # Write the updated contents back to the .env file.
    with env_path.open("w") as file:
        file.write("\n".join(new_env_lines))

    logger.info(f"API key saved successfully to {ENV_FILE}")


if __name__ == "__main__":
    set_api_key()
