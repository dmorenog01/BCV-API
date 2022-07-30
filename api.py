from flask import Flask, request
import requests
from bs4 import BeautifulSoup
import datetime

app = Flask(__name__)
URL = "http://www.bcv.org.ve/estadisticas/tipo-cambio-de-referencia-smc"

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
def index():
    return BCVRate()

if __name__ == "__main__":
    app.run(threaded=True, port=5000)