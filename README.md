# ReviewScraper
Starterhacks 2019

This is the project which is designed and developed as the part of StarterHacks 2019.

The repository has code for a chrome extention that can summarize a product on the screen from a e-commerce site and provides comparision and recommendations for the user at a single place.

This uses a python scraper to fetch data from different e-commerce website and summerises the product along with the overall sentiment value for the product across all shopping platforms.

Sentimental analysis done by training a ecommerce review data set. The Machine learning model is trained using simple Logistc Regression.

The model is deployed as REST Api as python flask app. The chrome extention will call the rest apis to get product summarization and recommendations for the product you are looking on the screen.
