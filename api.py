from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
import requests
from bs4 import BeautifulSoup
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

app = Flask(__name__)
auth = HTTPBasicAuth()
URL = "http://www.bcv.org.ve/estadisticas/tipo-cambio-de-referencia-smc"

USERS = {
    "TasaVE": 'pbkdf2:sha256:260000$uDAaEwXpgfBSMe6P$e8af0093fd2608e349c5a8a74b0c2d0ef01f08601e43a63b8eeac195e1bfbb1c'
}

@auth.verify_password
def verify_password(username, password):
    # Autenticates users in the API
    if username in USERS and check_password_hash(USERS.get(username), password):
        return username

@auth.error_handler
def auth_error(status):
    # Returns an empty response in case of 
    return {"rate": 0, "rate-date": None, "date-acquired": None, "hour-acquired": None, "code": status}, status

def BCVRate():
    try:
        # Try to retrieve data from source.
        r = requests.get(URL)

    except:
        # In case of failure, return error response.
        return {"rate": 0, "rate-date": None, "date-acquired": None, "hour-acquired": None, "code": 503}

    # If the retrieval is successful, build and return the response.
    time = datetime.datetime.now()
    date_acquired = time.strftime("%m/%d/%Y")
    hour_acquired = time.strftime("%H:%M:00")
    soup = BeautifulSoup(r.text, "html.parser")
    tasa = float(soup.select("#dolar")[0].select(".centrado")[0].strong.contents[0].replace(",","."))
    date = soup.select(".date-display-single")[0].contents[0]
    return {"rate": tasa, "rate-date": date, "date-acquired": date_acquired, "hour-acquired": hour_acquired, "code": 200}

@app.route("/", methods=["GET"])
@auth.login_required
def index():
    return BCVRate()

if __name__ == "__main__":
    app.run(threaded=True, port=5000)