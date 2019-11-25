# WEEK 2 PROJECT
### Team: Vu + Khanh 

## Overview outcome
**The result:** ![Alt Text](https://i.imgur.com/VjJFKxH.png)

**Database flow:**
![](https://i.imgur.com/bdoKS5w.png)

## About the code 

**In order to be able to duplicate Tiki and show them on our site, we break the hard job into two main steps:**

   **1. Scrawl data on Tiki and stores them in Postgres SQL under 2 tables:**
   All ipynb files is database, include:
    1. TIKIW2.MAINPAGE.KHANH(work, scrawl tiki.vn by me)
    2. scrape_and_insertDB (work, scrawl fullpage)
    3. productDB (still debuging, scrawl full page by me)
    4. TIKIW2.PRODUCTS.KHANH(still debuging, scrawl full page by me)
    
    - Categories: scrawl all category on Tiki.vn
    - Products: scrawl products from 4 categorie 

**Categories table**![](https://i.imgur.com/2OtIxTp.png)

### Data analysis:
1. How many sub categories are there on Tiki?
  - There are about 3700 sub categories on Tiki.
![](https://i.imgur.com/8GqzZls.png)


**Products table**![](https://i.imgur.com/yKLSftl.png)
### Data analysis:
1. How many main categories that we scrawl?
- We have about 4 main categories:

2. How many subcate in each of these 4 categories:
- 312 / 4
![](https://i.imgur.com/zGwrt9n.png)


3. How many products with tikinow are there?
- We have 6000/18600 items ( 30% of the total items)
![](https://i.imgur.com/xRK5I8Z.png)

   **2. Connect the database to flask app and format HTML file:**

     - HTML : see templates folder
     - Code: we break into 3 python files: 
         - app.py: flask app 
         - models.py: create object and information that needed to show on the HTML file
         - config.py: store the database address

