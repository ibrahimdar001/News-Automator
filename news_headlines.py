from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from datetime import date
import pandas as pd

website = "https://www.thesun.co.uk/sport/football/"


options = Options()
options.add_argument("headless")
driver = webdriver.Chrome(options=options)

driver.get(website)

news_container = driver.find_elements(By.XPATH, "//div[@class='teaser__copy-container']")
news_heading = "teaser__kicker"
news_text = "teaser__subdeck"
news_link = ".//a"

news_titles = list()
news_subtitles = list()
news_links = list()

print(news_container)

for news in news_container:
    try:
        news_title = news.find_element(By.CLASS_NAME, news_heading).text
        print(news_title)
        news_subtitle = news.find_element(By.CLASS_NAME, news_text).text 
        print(news_subtitle)
        news_lnk = news.find_element(By.XPATH, news_link).get_attribute('href')
        print(news_lnk)

        news_titles.append(news_title)
        news_subtitles.append(news_subtitle)
        news_links.append(news_lnk)
    
    except:
        continue
    

news_dict = {'Title':news_titles, 'Subtitle':news_subtitles, 'Link':news_links}

headlines_df = pd.DataFrame(news_dict)
headlines_df.to_csv('headlines.csv' + str(date.today()))

driver.close()


