# Sift

Wouldn't it be convenient if we could compare prices and reviews of every online product sold on competing platforms such as Amazon or eBay?

Well, you can now!

Sift is a project that:

1. Uses a python scraper to fetch data from different e-commerce websites.

2. Summarizes the product along with the overall sentiment value across all shopping platforms by training an e-commerce review data set. The Machine learning model is trained using simple Logistic Regression

3. The model is deployed as a REST API as a python flask app where Sift is a Chrome extension which will call the REST API to get the product summarizations and recommendations for every product viewed.

Sift simplifies online shopping and helps customers make informed purchasing decisions. 
