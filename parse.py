

def parse_input(user_input: str) -> str | list:
    """
    splits string into 2 parts: cmd and *args
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args





