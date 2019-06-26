# Visualizing Open Data using Python and D3.jsd -- PYTHON REPO

This repo contains Python code to extract data for a data visualization project (find it [here](https://github.com/iankameron/cc8-techtalk-d3js)).

A presentation of these materials can be found on [Youtube](https://youtu.be/9T32qNmWg8E?t=6225).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7
- virtualenv
- node.js or other JS engine (if you want to run post-processing scripts written in JS)

### Installing/how to use

** Under Construction **
- Confirm prerequisites
- Clone to local
- Initiate virtualenv
- source bin/activate
- python xxxx.py
- deactivate

## What's in the Repository

### HTML files

#### Scripts
- "latlong*" - Latitude- and Longitude-related
  - latlong.py
    - Extracts latitudes and longitudes for municipalities in Fukushima.
  - latlong_util.py
    - Util script
- "pop*" - Population-related
  - pop_download.py
    - Downloads population data files from the Fukushima Website
  - pop_extract.py
    - Uses xlrd library to extract relevant total population figures from the files downloaded with the above script. Outputs **population.dat**
  - pop_process.js
    - **JavaScript** program to get the population figures in a better format. Outputs file that becomes **population.js**.
  - pop_util.py
    - Utility functions used by the download scripts when running **pop_download**
- "rad*" - Radiation-related
  - rad_download.py
    - Downloads from Safecast API over time and space using nested loops
  - rad_util.py
    - Utility file for rad_download script.

#### Data folders
- data-latlong
  - Stores data extracted for the latitudes and longitudes of Fukushima cities (seems to be based on the location of their city halls). Created using the latlong.py script in the root.
- data-pop
  - Sample population data (raw file) downloaded from Fukushima web site. One left for reference. These files can be downloaded by using the pop-download python script in the root.
- data-rad
  - Sample radiation data (processed), created by running the rad-download python script in the root. Quarterly data for eastern Fukushima has been left for reference.
- data-rad-monthly
  - Similar to above, but monthly and retrieved on a finer grid. Due to an error in prep, most months only cover north-eastern Fukushima.

## Deployment

This repository is stand-alone and currently contains no functionality that is ready to be deployed.

## Built With

* [Visual Studio Code](https://code.visualstudio.com/) - IDE

## Contributing

Please post to the issues in the repository with ideas or improvements. Thank you!

## Authors

* **Ian Cameron** - *Initial work* - [iankameron](https://github.com/iankameron)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* SAFECAST organization (makers of radiation detectors and curators of worldwide radiation data)
* Code Chrysalis - This project was created for the tech talk part of the Code Chrysalis immersive bootcamp curriculum.