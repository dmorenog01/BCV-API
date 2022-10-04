# BCV-API
Simple API to get the current USD/Bs exchange rate from the BCV.

## Libraries
This project uses various Python libraries to function correctly:

### Flask
  Handles the requests made to the server and builds the coorrect response.
  Example response:
  ```
  {"code":200,"date-acquired":"08/04/2022","hour-acquired":"07:35:00","rate":5.7908,"rate-date":"Jueves, 04 Agosto  2022"}
  ```
### Requests
  Obtains the html from the Central Bank of Venezuela's website
### BeatifulSoup
  Parses the html to obtain the desired values.
### Flask-HTTPAuth
  Implements BasicAuth to the api.
