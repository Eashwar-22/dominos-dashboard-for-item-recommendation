# Dominos Item Recommendation Dashboard

I love pizza but am genuinely tired of spending minutes trying to choose one within my budget and crave. <br>
So this dashboard app (to be created) will narrow down my options quickly. <br><br>

**Pros** : Sometimes the original app crashes for no reason. This is time saving before adding the items to the cart. <br>
**Cons** : Web Scraping was done on ```15th Dec 21```. New items may not get updated easily if there is a concern with looping XPath elements in Selenium. <br>

---

### Step 1 : Pulling the raw data from the website using Selenium

- Scraping the menu items from https://pizzaonline.dominos.co.in/
- Selecting prices for each pizza with different crusts and sizes
- _**Period of data extraction** : '2021-12-15 23:19:03'_
- _**Note** : There could be sign-in/advertisement pop up windows appearing during random periods - a few callbacks using the driver maybe required then. Currently with that assumption a few lines of codes have been added to fix such issues._

<br><br>

<img width="1374" alt="Screenshot 2021-12-15 at 11 28 08 PM" src="https://user-images.githubusercontent.com/86509452/146247662-043b66a1-d20b-4e8c-97b9-e3738bb08950.png">


<br>

_**References**_
  - [Template](https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905)
  - [XPath Cheatsheet](https://www.w3schools.com/xml/xml_xpath.asp)
  - [Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

---
