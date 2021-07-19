# Final Project

## Goal

Use sentiment analysis to allow a user to enter a custom review and predict whether it is negative or positive.

## Technologies used

- AWS buckets
- Flask
- Heroku
- sklearn
- VADER
- Jupyter Notebooks
- HTML/CSS

## Overview

Using sci-kit learn, we trained two seperate models. One using Naive Bayes, and the other Support Vector Machine. After comparing the preformance of both models on the same testing dataset, we found that the SVM model was the most accurate, at about 89.5% accurate. To further support our choice, we also tested a rules based sentiment analysis and compared its results to the same test dataset, which were significantly lower than the machine learning approach, at about 69.5%. Once we found our model, we saved it and implemented it into a web-page that allows a user to test their own custom review. The model is loaded and used in the 'detect_sentiment.py' file, it contains a simple function that takes a string, and returns a prediciton. This fucntion is called from within app.py, which contains the rest of our flask app. The html is rendered using Flask's render templates, and the app itself is hosted on heroku. 

***Datasource***: https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

### Framework

1. Front End
    - HTML/CSS/BOOTSTRAP
    - JavaScript
2. Back End
    - Flask
3. Preperation
    - AWS
    - Jupyter Notebooks
    - sklearn 
    - VADER


## Link
The completed project can be viewed here: [Review Categorizer](https://movie-review-categorizer.herokuapp.com/)

