def analyze(response):
    if isinstance(response, str):
        return "Request Failed"

    if response.status_code >= 500:
        return "Server Crash Detected"

    if response.status_code == 400:
        return "Input Validation Detected"

    text = response.text.lower()

    if "negative transfer accepted" in text:
        return "Logic Flaw: Negative Amount Accepted"

    if "large transfer processed" in text:
        return "Missing Limit Validation"

    if "unauthorized account access" in text:
        return "Potential IDOR"

    if "possible injection" in text:
        return "Injection Attempt Detected"

    if "script detected" in text:
        return "XSS-like Payload Detected"

    if "invalid amount" in text:
        return "Input Validation Detected"

    if "missing account id" in text:
        return "Improper Input Validation"

    return "No obvious issue"