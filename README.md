# [ PROJECT: CRAWLING TIKI WEBSITE ](/9lRMLcbMR--joBvR84z5KA)
---
## [ 1. OVERVIEW ](/9lRMLcbMR--joBvR84z5KA)

[ **- About Tiki**: ](/9lRMLcbMR--joBvR84z5KA) Tiki is one of the top ecommerce website in Vietnam with a large amount of products.

[ **- Purpose of the project**: ](/9lRMLcbMR--joBvR84z5KA) crawl 2000 products on Tiki and try to reproduct the page on flask app.
![](https://i.imgur.com/4CbDh7D.png)

---
## [ 2. THE APPROACH ](/9lRMLcbMR--joBvR84z5KA)

### [2.1 Code approach](/lH2ryznwTJa4oKA092dkkA)
- There are 3 main parts for code in this project:

| Crawling Data | Store in database | Create flask app |
| -------- | -------- | -------- |

#### [2.1.1 Database connection](/lH2ryznwTJa4oKA092dkkA)

**- 1st: import libraries for crawling website and connect to database on python.**
``` 
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import psycopg2
```
**- 2nd: Using python to connect database and data togther, create a database table.**

##### Connect to database
```
conn = psycopg2.connect('dbname=khanhdb user=postgres password=123456')
conn.autocommit = True
cur = conn.cursor()
```
##### Define function to create table
```
def create_table():
    query ='''
        CREATE TABLE IF NOT EXISTS Tiki (id SERIAL PRIMARY KEY,
        category TEXT,
        url TEXT,
        parent_id INT,
        brand TEXT,
        product TEXT,
        img TEXT,
        fprice TEXT,
        rprice TEXT,
        installment TEXT,
        tikinow TEXT,
        reviews TEXT);
    '''
    try:
        cur.execute(query)
    except Exception as err:
        print(f'ERROR: {err}')
```

#### [2.1.2 Function to crawl data from the web](/lH2ryznwTJa4oKA092dkkA)

##### Get all information in the web and beautify them using BeautifulSoup
```

def load_web(url):
    try:
        response = requests.get(url).text
        response = BeautifulSoup(response, 'html.parser')
        return response
    except Exception as err:
        print(f'ERROR: {err}')
```
##### Get all main cate igory on Tiki main page and store them into database and list to dump json later
```

def crawlling_mainpage(url, db_name):
    soup = load_web(url)

    # scrape the website and store their cate and link in a list
    categories = soup.findAll('a', {'class', "MenuItem__MenuLink-tii3xq-1 efuIbv"})
    cat, link = [], []
    for cate in categories:
        category = cate.text
        url = cate['href']
        cat.append(category)
        link.append(url)
        
        # save into database
        query = f'''INSERT INTO {db_name} (category, url)
        VALUES ('{category}','{url}');
        '''
        
        cur.execute(query)

    return list(zip(cat, link))
```
##### Get all the information in the 1st sub page and store them directly to database and a list
```
def crawling_subpage(main_page, db_name):
    b_list, p_list, img_list, fprice_list, rprice_list, i_list, tikinow_list, reviews_list, url_list, cat_list = [], [],[],[],[],[],[],[],[],[]
    
    for sub_page in main_page:
        page = load_web(sub_page[1])
        items = page.findAll('div', {'class':"product-item"})

        for item in items:
            try:
                brand = item['data-brand'].replace("'", " ")
                product = item['data-title']
                image = item.img['src']
                final_price = item('span', {'class': 'final-price'})[0].text.strip().split(' ')[0]
                regular_price = item('span', {'class': 'price-regular'})[0].text.strip().split(' ')[0]
                installment = ['NO' if item('span', {'class': 'installment-price'}) == [] else item('span', {'class': 'installment-price'})[0].text][0] 
                tikinow = ['NO' if item('i',{"class":"tikicon icon-tikinow-20"}) == [] else 'YES'][0]
                reviews = item('p', {'class':'review'})[0].text
                url = item.a['href']
                category = main_page[0]

                #store into json file
                b_list.append(brand)
                p_list.append(product)
                img_list.append(image)
                fprice_list.append(final_price)
                rprice_list.append(regular_price)
                i_list.append(installment)
                tikinow_list.append(tikinow)
                reviews_list.append(reviews)
                url_list.append(url)
                cat_list.append(category)

                #save into database
                query = f"""INSERT INTO {db_name} (
                url, brand, product, img, fprice, rprice, installment, tikinow, reviews)
                VALUES ('{url}', '{brand}', '{product}', '{image}', '{final_price}', '{regular_price}', '{installment}', '{tikinow}', '{reviews}');
                """
                cur.execute(query)
            except Exception as err:
                print('err')
        
    return list(zip(b_list, p_list, img_list, fprice_list, rprice_list, i_list, tikinow_list, reviews_list, url_list, cat_list))
```
##### Store one more version in json file.
```
with open('main_cate.json', 'w') as file:
    json.dump(main_page, file)
    
with open('sub_cate.json', 'w') as file:
    json.dump(json_file, file)
```
#### [2.1.3 Connect the database to flask app and format HTML file](/lH2ryznwTJa4oKA092dkkA)
 - HTML : see templates folder
 - Code: we break into 3 python files: 
     - app.py: flask app 
     - create_data.py: create object and information that needed to show on the HTML file
     - config.py: store the database address


---

## [3. THE RESULT ](/-iz_-FrPQ3SPbl7WJxdocg)

### 3.1 The result:

**3.1.1 This is how our flask app look like**
![Alt Text](https://i.imgur.com/VjJFKxH.png)

**3.1.2 Database flow:**
![](https://i.imgur.com/bdoKS5w.png)


**3.1.3 Categories table**![](https://i.imgur.com/2OtIxTp.png)

### 3.2 Data analysis:
**1. How many products that we crawled on Tiki?**
  - We crawled about 3700 sub categories on Tiki.
![](https://i.imgur.com/8GqzZls.png)

**Products table**![](https://i.imgur.com/yKLSftl.png)

**2. How many main categories that we scrawl?**
- We have about 4 main categories:


**3. How many products with tikinow are there?**
- We have 6000/18600 items ( 30% of the total items)
![](https://i.imgur.com/xRK5I8Z.png)

