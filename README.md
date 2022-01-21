# IPL-Score-Predictor
[![Flask](https://camo.githubusercontent.com/31dfe5f167d56ccab3ca37634bf1d396e48231856b25576b5dafbc934bd327e9/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f7374796c653d666f722d7468652d6261646765266d6573736167653d466c61736b26636f6c6f723d303030303030266c6f676f3d466c61736b266c6f676f436f6c6f723d464646464646266c6162656c3d)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)


# Score Master

Score Master is an application which uses machine learning algorithms to predict the score of the T20 cricket match
A Ridge regression model is trained on IPL matches dataset from 2008 to 2019.

Application is live here :- https://ipl-score-master.herokuapp.com/


# Demo

https://user-images.githubusercontent.com/46680697/150517395-f537a2de-8b57-49e4-821f-0f928678e5bb.mp4


## Screenshots
![Home Page](/screenshots/3.png?raw=true "Optional Title")

![Enter the match situation](/screenshots/4.png?raw=true "Optional Title")

![Predicted Score Range](/screenshots/2.png?raw=true "Optional Title")


## Tech Stack

**Client:** Flask, Jinja2

**Server:** Ridge Regression model, Pickle module

**Languages** Python, HTML, CSS


## Installation

Install Score Master (linux)

```bash
  - fork the repo
  - clone from your account
  - change to the cloned directory
  - activate veritula environment
  - run: pip install -r requirements.txt
  - run: export set FLASK_APP=webapp
  - navigate to folder which has app.py
  - run: python -m flask run

```

See the project running on localhost :)

    
## Features

- All stadiums available
- All teams available
- Changing Banner UI



## Deployment

The Application has been deployed on heroku.
Every new push to main branch automatically deploys the newer version.
 
pull from main, add changes, commit and push

```bash
    git pull origin main
    git add .
    git commit -m "your comment"
    git push origin main
```

* note connect to your own heroku account.
## Authors

- [@iota-008](https://www.github.com/iota-008)
