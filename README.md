# Elevation Based Navigation - EleNa

### Members - Github username
Eric Huang - Eric4k, Alan Zheng - alan3737, Adiba Haque - Adibahaque-lab, Jason Jermany - jasonjermany

## What is Elevation Based Navigation (EleNa)?
Elevation Based Navigation (EleNa) is form of web application that incorporates elevation data for determining optimal routes for navigation. By factoring in elevation data, EleNa can help users identify paths that are either more scenic, challenging, or easier, shortest, or longest depending on their preferences. The goal of this project is to develop a system that, given a source and a destination, determines the optimal path based on users’ preferences. We have provided users with two routing options - maximizing or minimizing elevation gain, and two modes of transportation - walking or biking. The project has scope for further extension by incorporating new modes of transportation, such as bus and car.

![](Images/app.JPG)
![](Images/demo.JPG)

## Instructions to Run EleNa

### cloning repo
`git clone https://github.com/Eric4k/Group-11-ELeNA.git`
### Quick Start

### Running frontend
In the `Frontend/elena_ui` drectory of the project instructions for running React client would be to `npm install & npm start`

### Running backend
In order to run the web application, install the required dependencies using `pip install -r requirements.txt` in the `Backend` directory.
To run the backend server, use `python3 manage.py runserver` in `Backend/elena_project`.

### Instruction on GraphML geodata files to change location
The graphML files contain the geodata for the location which is currently set to `Amherst, MA`. If a different city is desired then
a change can be made to `apps.py` in `Backend/elena_project/elena`. The `city` and `state` variables could be changed before the startup of the Django server and the appropriate biking and walking geodata for that location will be loaded and saved as a graphML file in the `dataSets` directory which will allow for a faster load up next time the same location is requested.

## Tests
The test suits have been developed to facilitate evaluating the functionality of each component.
Run the test suite `tests.py` in `Backend/elena_project` by `./manage.py test`
