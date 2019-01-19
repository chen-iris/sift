# Sift

T#his is the project designed and developed in 24 hours in StarterHacks 2019.

The repository has code for a chrome extension that summarizes a product on the screen from a e-commerce site by comparing the reviews and prices of a similar product on competing websites for the user at a single place. 

It uses a python scraper to fetch data from different e-commerce website and summerizes the product along with the overall sentiment value for the product across all shopping platforms.

Sentimental analysis is done by training an e-commerce review data set. The Machine learning model is trained using simple Logistc Regression.

The model is deployed as a REST Api as python flask app. The chrome extension will call the REST apis to get the product summarizations and recommendations for the product you are looking on the screen.
