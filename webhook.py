from flask import Flask, jsonify, request
from requests import Response

app = Flask(__name__)


@app.route("/on_scan_assigned", methods=["POST"])
def webHook():
    body = request.get_json()
    data = body["data"]
    assignment_created = data["created"]

    print("Part was assigned on: %s" % assignment_created)

    response = jsonify({"success": True})
    response.status_code = 200
    return response


if __name__ == "__main__":
    app.run(debug=False, port=5000, host="0.0.0.0")
