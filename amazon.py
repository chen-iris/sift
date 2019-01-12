import amazonscraper
import requests
import sys
from json import dump,loads
from lxml import html
import re


def getReviews(url, product):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    response = requests.get(url, headers = headers, verify=False, timeout=30)
    cleaned_response = response.text.replace('\x00', '')
    parser = html.fromstring(cleaned_response)
    reviewlists = []
    headerlists = []
    reviews = parser.xpath('//div[contains(@id,"reviews-summary")]')
    header_path = './/a[@data-hook="review-title"]//text()'
    XPATH_REVIEW_TEXT_1 = './/div[@data-hook="review-collapsed"]//text()'
    XPATH_REVIEW_TEXT_3 = './/div[contains(@id,"dpReviews")]/div/text()'
    XPATH_REVIEW_TEXT_2 = './/div//span[@data-action="columnbalancing-showfullreview"]/@data-columnbalancing-showfullreview'
    for review in reviews:
        raw_review_header = review.xpath(header_path)
        full_review_text = ""
        review_header = ' '.join(' '.join(raw_review_header).split())
        review_text = ' '.join(' '.join(raw_review_text1).split())
        raw_review_text1 = review.xpath(XPATH_REVIEW_TEXT_1)
        raw_review_text2 = review.xpath(XPATH_REVIEW_TEXT_2)
        raw_review_text3 = review.xpath(XPATH_REVIEW_TEXT_3)
        # Grabbing hidden comments if present
        if raw_review_text2:
            json_loaded_review_data = loads(raw_review_text2[0])
            json_loaded_review_data_text = json_loaded_review_data['rest']
            cleaned_json_loaded_review_data_text = re.sub('<.*?>', '', json_loaded_review_data_text)
            full_review_text = review_text+cleaned_json_loaded_review_data_text
        else:
            full_review_text = review_text
        if not raw_review_text1:
            full_review_text = ' '.join(' '.join(raw_review_text3).split())
        headerlists.append(review_header)
        reviewlists.append(full_review_text)
        
    data =  {
                'headerlists' : headerlists,
                'reviewlists' : reviewlists
            }
    return data
        
    

def main():
    product = sys.argv[1] #product name
    choice = sys.argv[2]
    num = choice # how many items you want
    results = amazonscraper.search(product, max_product_nb=num)
    lst = list(results)
    lst.sort(key=lambda item: item.rating, reverse=True)
    top_ten = lst[1:10]
    urls = (item.url for item in top_ten)
    # print(top_ten)

    for result in top_ten:
        
        print("{}".format(result.title))
        # print("  - ASIN : {}".format(result.asin))
        # print("  - {} out of 5 stars, {} customer reviews".format(result.rating, result.review_nb))
        # print("  - {}".format(result.url))
        # print("  - Image : {}".format(result.img))
        # print()

        # get product image
        # url = result.url
        # img_data = requests.get(url).content
        # with open(result.asin, 'wb') as handler:
        #     handler.write(img_data)

if __name__ == "__main__":
    main()