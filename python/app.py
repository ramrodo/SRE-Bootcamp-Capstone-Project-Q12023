""" Module to define routes for the API client. """
from flask import Flask, request, jsonify, abort
from api.networking import CidrMaskConvert, IpValidate
from api.login import Token, Restricted

app = Flask(__name__)
login = Token()
protected = Restricted()
convert = CidrMaskConvert()
validate = IpValidate()


@app.route("/")
def url_root():
    """ Root endpoint that returns a single OK message. """
    return "OK"

@app.route("/_health")
def url_health():
    """ Health endpoint that returns a single OK message. """
    return "OK"

@app.route("/login", methods=["POST"])
def url_login():
    """ Login endpoint that authenticates a user.
        Form fields:
            - username: String
            - password: String

        Example: http://127.0.0.1:8000/login
    """
    username = request.form["username"]
    password = request.form["password"]
    res = {
        "data": login.generate_token(username, password)
    }
    return jsonify(res)

@app.route("/cidr-to-mask")
def url_cidr_to_mask():
    """ Endpoint that verifies the authorization token and returns the mask from the CIDR given.
        Args:
            - value: String

        Example: http://127.0.0.1:8000/cidr-to-mask?value=8
    """
    authorization_token = request.headers.get("Authorization")
    if not protected.access_data(authorization_token):
        abort(401)

    cidr = request.args.get("value")

    response = {
        "function": "cidrToMask",
        "input": cidr,
        "output": convert.cidr_to_mask(cidr)
    }

    return jsonify(response)

@app.route("/mask-to-cidr")
def url_mask_to_cidr():
    """ Endpoint that verifies the authorization token and returns the CIDR from the mask given.
        Args:
            - value: String

        Example: http://127.0.0.1:8000/mask-to-cidr?value=255.0.0.0
    """
    token = request.headers.get("Authorization")
    if not protected.access_data(token):
        abort(401)
    mask = request.args.get("value")

    response = {
        "function": "maskToCidr",
        "input": mask,
        "output": convert.mask_to_cidr(mask)
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 8000)
