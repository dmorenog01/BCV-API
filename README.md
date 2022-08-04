# BCV-API
Simple API to get the current USD/Bs exchange rate from the BCV.

## Libraries
This project uses various Python libraries to function correctly:

### Flask
  Handles the requests made to the server and builds the response dictionary.
### Requests
  Obtains the html from the Central Bank's website
### BeatifulSoup
  Parses the html to obtain the desired values.
### Flask-HTTPAuth
  Implements BasicAuth to the api.
