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
* [Bootstrap](https://getbootstrap.com)
* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Html](https://html.com/)
* [Css] (https://css-tricks.com/)
## Getting Started

In order to successfully run our webpage, you must follow these steps and adhere to the prerequisites. This will ensure you establish a correct running environment. For the sake of good practice, we recommend using a virtual environment and will thus be showing how to set that up in the following sub-sections!

### Prerequisites 
* [Bash](https://www.gnu.org/software/bash/manual/html_node/Installing-Bash.html)
* [Python](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu)
* _pip3_ or _pip_
* _virtualenv_
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
Once _pip3_ is installed, we can now install virtualenv packages.

* Virtualenv: 
```sh
python3 -m pip install --user virtualenv
```
* Verify installation:
```sh 
virtualenv --version
```
Once that completes, download or clone this repository and using the bash shell navigate into the _../app/_ folder. From here we are ready to set up our virtual environmment.

* Set up virtual environmment:
```sh
virtualenv env
```

* Activate virtual environment:
```sh
source /env/bin/activate
```

From there you should see a _(environment)_ indicator appear in your shell. If this does not appear, please retrace your steps. The next item needed is Flask. 

* Install Flask:
```sh
pip3 install Flask
```

From here your environment should be ready to go! Congrats 🎊 

## Usage
To run the app you have to follow the next commandlines:
```ssh
git clone git@github.com:S4ND1X/oh_team2.git
cd oh_team2
pip3 install -r requirements.txt
flask run
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

