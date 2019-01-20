# Sift

Wouldn't it be convenient if we could compare prices and reviews of every online product sold on different platforms?

Sift is a project that:

1. Uses a python scraper to fetch data from different e-commerce websites.

2. Summarizes the product along with the overall sentiment value across all shopping platforms by training an e-commerce review data set. The Machine learning model is trained using simple Logistic Regression

3. The model is deployed as a REST Api as a python flask app and Sift is a chrome extension which will call the REST Apis to get the product summarizations and recommendations for every product viewed.


