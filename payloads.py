import random
import string

def get_payloads():
    return [
        "A" * 10000,
        "' OR 1=1 --",
        "!@#$%^&*()",
        "",
        None,

        str(-999999999),
        str(999999999999999),
        "0",

        "../../etc/passwd",
        "../admin",

        "{invalid:json}",
        "null",
        "undefined",

        "'; DROP TABLE users; --",
        "<script>alert(1)</script>",

        ''.join(random.choices(string.ascii_letters + string.digits, k=50))
    ]