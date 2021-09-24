[![Contributors][contributors-shield]][contributors-url]

          
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/S4ND1X/oh_team2">
    <img src="app/static/img/MLH_Logo.svg" alt="Logo" width="200" height="100">
  </a>

  <h3 align="center">Pod 4.0.3 Team 2 Portfolio</h3>

  <p align="center">
    A great kickoff to the MLH Production Engineering Fellowship!
    <br />
    <a href="dhttps://github.com/S4ND1X/oh_team2"><strong>Explore the repo »</strong></a>
    <br />
    <br />
    <a href="https://www.youtube.com/watch?v=0uzl_n4a7Hw&ab_channel=CarlosRicoveri">View Demo</a>
    ·
    <a href="dhttps://github.com/S4ND1X/oh_team2/issues">Report Bug</a>
    ·
    <a href="dhttps://github.com/S4ND1X/oh_team2/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributors">Contributors</a></li>
     <ul>   
         <li><a href="#github">Github</a></li>
         <li><a href="#linkedin">LinkedIn</a></li> 
     </ul>
    <li><a href="#devpost">Devpost</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

## About the Project

### Built With
* [Python](https://www.python.org/)
* [Pysa](https://pyre-check.org/docs/pysa-basics/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Heroku](https://www.heroku.com/)
* [Html](https://html.com/)
* [Css](https://css-tricks.com)
* [ScrollReveal](https://scrollrevealjs.org/)
* [Bootstrap](https://getbootstrap.com)
## Getting Started

In order to successfully run our webpage, you must follow these steps and adhere to the prerequisites. This will ensure you establish a correct running environment. For the sake of good practice, we recommend using a virtual environment and will thus be showing how to set that up in the following sub-sections!

### Prerequisites 
* [Bash](https://www.gnu.org/software/bash/manual/html_node/Installing-Bash.html)
* [Python 3.7 or later](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu)
* _pip3_ or _pip_
* Flask

### Installation

To install _pip3_ run the following commands in your bash terminal:

* Update your system:
```sh
sudo apt-get update
```

* Pip3 install:
```sh
sudo apt-get -y install python3-pip
```

* Verify installation:
```sh
pip3 --version
```

* Install Flask:
```sh
pip3 install Flask
```

* `setuptools` and `wheel` install:
```sh
python3.8 -m pip install --upgrade setuptools
pip3 install wheel
```

* Set up the virtual environment: 
```sh
python3.8 -m venv ~/.venvs/pysa
```

* Activate virtual environment for Pysa:
```sh
source ~/.venvs/pysa/bin/activate
```

From there you should see a _(pysa)_ indicator appear in your shell. If this does not appear, please retrace your steps. 

* Install dependencies
```sh
ls ~/.venvs/pysa/lib/python3.8/site-packages
```

* Install Pyre and SAPP in the virtual environment
```sh
pip install pyre-check fb-sapp
```

* Create Pyre configuration file in the root directory which Pysa runs on
```sh
cd /path/to/your/repo
pyre init
```
Now you should be able to see `.pyre_configuration` file in the root directory

* Add type annotations automatically to your project
```sh
pyre infer -i
```

* Run Pysa
```sh
pyre analyze --no-verify --save-results-to ./pysa-runs
```

* Run SAAP
```sh
sapp analyze ./pysa-runs/taint-output.json
sapp server # web UI
```

From here your environment should be ready to go! Congrats 🎊 

## Usage
To run the app you have to follow the next commandlines:
```ssh
git clone git@github.com:S4ND1X/oh_team2.git
cd oh_team2
pip3 install virtualenv
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
python wsgi.py
```

## Contributors
This team is composed of 3 members. Below are their Github and LinkedIn accounts.

### Github
[Jorge Sanchez](https://github.com/S4ND1X)

[Vũ Long Phan](https://github.com/vulongphan)

[Onyemowo Agbo](https://github.com/Onyiee)

### LinkedIn
[Jorge Sanchez](https://www.linkedin.com/in/jorgesanchezdiaz/)

[Vũ Long Phan]()

[Onyemowo Agbo](http://linkedin.com/in/onyemowo-agbo)

## Devpost
[Check it out]()

## License
[LICENSE](dhttps://github.com/S4ND1X/oh_team2/LICENSE)

## Acknowledgements
[GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)

[Img Shields](https://shields.io)

[Pip3 Install](https://www.educative.io/edpresso/installing-pip3-in-ubuntu)

[Readme Template](https://github.com/othneildrew/Best-README-Template)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: dhttps://github.com/S4ND1X/oh_team2/blob/main/images/Contributors.svg
[contributors-url]: dhttps://github.com/S4ND1X/oh_team2/graphs/contributors
[product-screenshot]: images/landingpage.png

