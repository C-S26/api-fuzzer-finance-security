import requests

def send_request(url, payload):
    try:
        safe_payload = "" if payload is None else payload

        data = {
            "account_id": str(safe_payload),
            "amount": str(safe_payload)
        }

        response = requests.post(url, json=data, timeout=3)
        return response

    except Exception as e:
        return f"Request Failed: {str(e)}"