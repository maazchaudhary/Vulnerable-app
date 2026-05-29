"""
security.py
Provides password hashing utilities used during user registration and authentication.
"""
import bcrypt


def hash_password(password: str) -> str:
    """Return the bcrypt hash of the given password string."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()


def verify_password(password: str, hashed: str) -> bool:
    """Verify if the given password matches the stored bcrypt hash."""
    return bcrypt.checkpw(password.encode(), hashed.encode())
