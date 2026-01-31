token_blacklist: set[str] = set()

def add_token_to_blacklist(token: str) -> None:
    token_blacklist.add(token)

def is_token_blacklisted(token: str) -> bool:
    return token in token_blacklist