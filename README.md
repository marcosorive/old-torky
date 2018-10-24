# Torky

Torky is a videogame price comparator between Spanish stores. You can try it  [here.](https://teorky.herokuapp.com) It's not perfect and sometimes it doesn't find the prices or get the wrong games, but it will get better with every iteration.

![torky-img](https://raw.githubusercontent.com/marcosorive/marcos.orive.me/master/images/torky.png
)



## Getting Started

I'll try to give instructions to download and get a copy of Troky running locally. For deployment check the documentation in Flask's website. 



### Prerequisites

1. Python 3.6 and and pipenv installed. The rest of the python dependecies will be installed when iniciating pipenv.
2. For scraping Game.es you need Firefox installed and the geckodriver binaries in the PATH. You can use chrome and chromedriver instead.
3. Finally, for searching amazon PA API credentials are required. 


### Installing

First off install Python 3.6 (minimum) and pipenv.

Clone the repository and move to the directory.

```
git clone https://github.com/marcosorive/torky.git
cd torky
```
Once inside the directory type `pipenv install` to install all python dependencies.

Continue typing the following command to enter the virtualenv and run the flask development server.

```
pipenv shell
export FLASK_APP=index.py
flask run
```
Open a web browser and type http://127.0.0.1:5000. You will have Torky running in your machine :)

Remember that for Game.es you need to install Firefox with geckodriver or Chrome with Chromedriver. The drivers should be in the PATH variable. Also remember to get API credentials for searching in amazon.es.

## Deployment

Check [here](http://flask.pocoo.org/docs/1.0/deploying/) for deployment options and tutorials.<br> 
You can try a deployed version running [here](https://teorky.herokuapp.com)


## Authors

**Marcos Orive Izarra** - [marcos.orive.me](https://marcos.orive.me)



# Torky

Torky is a videogame price comparator between Spanish stores. You can try it  [here.](https://teorky.herokuapp.com) It's not perfect and sometimes it doesn't find the prices or get the wrong games, but it will get better with every iteration.

![torky-img](https://raw.githubusercontent.com/marcosorive/marcos.orive.me/master/images/torky.png
)



## Getting Started

I'll try to give instructions to download and get a copy of Troky running locally. For deployment check the documentation in Flask's website. 



### Prerequisites

1. Python 3.6 and and pipenv installed. The rest of the python dependecies will be installed when iniciating pipenv.
2. For scraping Game.es you need Firefox installed and the geckodriver binaries in the PATH. You can use chrome and chromedriver instead.
3. Finally, for searching amazon PA API credentials are required. 


### Installing

First off install Python 3.6 (minimum) and pipenv.

Clone the repository and move to the directory.

```
git clone https://github.com/marcosorive/torky.git
cd torky
```
Once inside the directory type `pipenv install` to install all python dependencies.

Continue typing the following command to enter the virtualenv and run the flask development server.

```
pipenv shell
export FLASK_APP=index.py
flask run
```
Open a web browser and type http://127.0.0.1:5000. You will have Torky running in your machine :)

Remember that for Game.es you need to install Firefox with geckodriver or Chrome with Chromedriver. The drivers should be in the PATH variable. Also remember to get API credentials for searching in amazon.es.

## Deployment

Check [here](http://flask.pocoo.org/docs/1.0/deploying/) for deployment options and tutorials.<br> 
You can try a deployed version running [here](https://teorky.herokuapp.com)


## Authors

**Marcos Orive Izarra** - [marcos.orive.me](https://marcos.orive.me)



