from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/transfer", methods=["POST"])
def transfer():
    try:
        data = request.get_json(silent=True) or {}

        account_id = str(data.get("account_id", ""))
        amount_raw = data.get("amount")

        # -----------------------------
        # Detect patterns FIRST
        # -----------------------------
        if "../" in account_id or ".." in account_id:
            return jsonify({"status": "unauthorized account access"})

        if "or 1=1" in account_id.lower():
            return jsonify({"status": "possible injection"})

        if "<script>" in account_id.lower():
            return jsonify({"status": "script detected"})

        # -----------------------------
        # Convert amount safely
        # -----------------------------
        try:
            amount = int(amount_raw)
        except:
            return jsonify({"status": "invalid amount input"}), 400

        # -----------------------------
        # Logic flaws
        # -----------------------------
        if amount < 0:
            return jsonify({"status": "negative transfer accepted"})

        if amount > 1000000:
            return jsonify({"status": "large transfer processed"})

        # -----------------------------
        # Missing account
        # -----------------------------
        if account_id.strip() == "":
            return jsonify({"status": "missing account id"})

        return jsonify({"status": "transfer successful"})

    except Exception as e:
        return jsonify({"status": "server error", "error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)