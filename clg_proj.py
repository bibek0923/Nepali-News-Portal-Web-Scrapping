import requests
from bs4 import BeautifulSoup
import pandas as pd
link_education=[]
link_sports =[]
link_entertainment=[]
link_health=[]
link_economy=[]
link_opinion=[]



def scrap_multiple_pages_education_news():
    link_education = []
    
    # Scraping links to education news
    for i in range(1, 80):
        url = f"https://www.ratopati.com/category/education?page={i}"
        web = requests.get(url)
        soup = BeautifulSoup(web.content, "html.parser")
        required_div_list = soup.find_all("div", class_="columnnews mbl-col col3")
        for one_div in required_div_list:
            link = one_div.find("a")
            if link:
                one_link = link.get("href")
                link_education.append(one_link)
        
        print(f"Processed page {i}")
    
    news_article = []
    headlines = []
    
    # Scraping individual news articles
    for one_edu_link in link_education:
        try:
            web = requests.get(one_edu_link)
            soup = BeautifulSoup(web.content, "html.parser")
            
            # Extracting headline
            a = soup.find('h2', class_="heading")
            if not a:
                print(f"Skipping {one_edu_link}: No headline found.")
                continue
            headline = a.text
            headlines.append(headline)
            
            # Extracting article content
            b = soup.find('div', class_="the-content")
            if not b:
                print(f"Skipping {one_edu_link}: No content found.")
                continue
            all_p = b.find_all('p')
            combined_paragraph = ' '.join(p.get_text(strip=True) for p in all_p)
            news_article.append(combined_paragraph)
        
        except Exception as e:
            print(f"Error processing {one_edu_link}: {e}")
    
    # Creating DataFrame and saving to CSV
    df = pd.DataFrame({
        "URL": link_education[:len(news_article)], 
        "news_article": news_article, 
        "headline": headlines
    })
    
    print(df)
    df.to_csv("news.csv", index=False)


        


def scrap_multiple_pages_sports_news():
    link_sports = []
    valid_links = []  # List to store only valid links
    news_article = []
    headlines = []
    
    # Scraping links to sports news
    for i in range(1, 80):
        url = f"https://www.ratopati.com/category/sports?page={i}"
        web = requests.get(url)
        soup = BeautifulSoup(web.content, "html.parser")
        required_div_list = soup.find_all("div", class_="columnnews mbl-col col3")
        for one_div in required_div_list:
            link = one_div.find("a")
            if link:
                one_link = link.get("href")
                link_sports.append(one_link)
        
        print(f"Processed page {i}")
    
    # Scraping individual sports news articles
    for one_sports_link in link_sports:
        try:
            web = requests.get(one_sports_link)
            soup = BeautifulSoup(web.content, "html.parser")
            
            # Extracting headline
            a = soup.find('h2', class_="heading")
            if not a:
                print(f"Skipping {one_sports_link}: No headline found.")
                continue
            headline = a.text
            
            # Extracting article content
            b = soup.find('div', class_="the-content")
            if not b:
                print(f"Skipping {one_sports_link}: No content found.")
                continue
            all_p = b.find_all('p')
            combined_paragraph = ' '.join(p.get_text(strip=True) for p in all_p)
            
            # Append only valid data
            valid_links.append(one_sports_link)
            headlines.append(headline)
            news_article.append(combined_paragraph)
        
        except Exception as e:
            print(f"Error processing {one_sports_link}: {e}")
    
    # Creating DataFrame and saving to CSV
    df = pd.DataFrame({
        "URL": valid_links,
        "news_article": news_article,
        "headline": headlines
    })
    
    print(df)
    df.to_csv("sports_news.csv", index=False)

     

        
        
        
def scrap_multiple_pages_entertainment_news():
    link_entertainment = []
    valid_links = []  # List to store only valid links
    news_article = []
    headlines = []
    
    # Scraping links to entertainment news
    for i in range(1, 80):  # Adjust the range based on the number of pages to scrape
        url = f"https://www.ratopati.com/category/entertainment?page={i}"
        try:
            web = requests.get(url)
            soup = BeautifulSoup(web.content, "html.parser")
            required_div_list = soup.find_all("div", class_="columnnews mbl-col col3")
            for one_div in required_div_list:
                link = one_div.find("a")
                if link:
                    one_link = link.get("href")
                    link_entertainment.append(one_link)
            
            print(f"Processed page {i}, found {len(required_div_list)} articles.")
        except Exception as e:
            print(f"Error fetching page {i}: {e}")
    
    # Scraping individual entertainment news articles
    for one_ent_link in link_entertainment:
        try:
            web = requests.get(one_ent_link)
            soup = BeautifulSoup(web.content, "html.parser")
            
            # Extracting headline
            a = soup.find('h2', class_="heading")
            if not a:
                print(f"Skipping {one_ent_link}: No headline found.")
                continue
            headline = a.text
            
            # Extracting article content
            b = soup.find('div', class_="the-content")
            if not b:
                print(f"Skipping {one_ent_link}: No content found.")
                continue
            all_p = b.find_all('p')
            combined_paragraph = ' '.join(p.get_text(strip=True) for p in all_p)
            
            # Append only valid data
            valid_links.append(one_ent_link)
            headlines.append(headline)
            news_article.append(combined_paragraph)
        
        except Exception as e:
            print(f"Error processing {one_ent_link}: {e}")
    
    # Creating DataFrame and saving to CSV
    df = pd.DataFrame({
        "URL": valid_links,
        "news_article": news_article,
        "headline": headlines
    })
    
    print(f"Scraping complete. Total articles fetched: {len(valid_links)}")
    df.to_csv("entertainment_news.csv", index=False)




def scrap_multiple_pages_health_news():
    link_health = []
    valid_links = []  # List to store only valid links
    news_article = []
    headlines = []
    
    # Scraping links to health news
    for i in range(1, 80):  # Adjust the range based on the number of pages to scrape
        url = f"https://www.ratopati.com/category/health?page={i}"
        try:
            web = requests.get(url)
            soup = BeautifulSoup(web.content, "html.parser")
            required_div_list = soup.find_all("div", class_="columnnews mbl-col col3")
            for one_div in required_div_list:
                link = one_div.find("a")
                if link:
                    one_link = link.get("href")
                    link_health.append(one_link)
            
            print(f"Processed page {i}, found {len(required_div_list)} articles.")
        except Exception as e:
            print(f"Error fetching page {i}: {e}")
    
    # Scraping individual health news articles
    for one_health_link in link_health:
        try:
            web = requests.get(one_health_link)
            soup = BeautifulSoup(web.content, "html.parser")
            
            # Extracting headline
            a = soup.find('h2', class_="heading")
            if not a:
                print(f"Skipping {one_health_link}: No headline found.")
                continue
            headline = a.text
            
            # Extracting article content
            b = soup.find('div', class_="the-content")
            if not b:
                print(f"Skipping {one_health_link}: No content found.")
                continue
            all_p = b.find_all('p')
            combined_paragraph = ' '.join(p.get_text(strip=True) for p in all_p)
            
            # Append only valid data
            valid_links.append(one_health_link)
            headlines.append(headline)
            news_article.append(combined_paragraph)
        
        except Exception as e:
            print(f"Error processing {one_health_link}: {e}")
    
    # Creating DataFrame and saving to CSV
    df = pd.DataFrame({
        "URL": valid_links,
        "news_article": news_article,
        "headline": headlines
    })
    
    print(f"Scraping complete. Total articles fetched: {len(valid_links)}")
    df.to_csv("health_news.csv", index=False)



def scrapp_multiple_pages_economy_news():
     for i in range(1,2):
        url =f"https://www.ratopati.com/category/economy?page={i}"
        web = requests.get(url)
        # print(web.status_code)
        soup=BeautifulSoup(web.content,"html.parser")
        required_div_list=soup.find_all("div",class_="columnnews mbl-col col3")
        for one_div in required_div_list:
            link=one_div.find("a")
            # print(link)
            one_link=link.get("href")
            # print(one_link)
            link_economy.append(one_link)
        print(link_economy)
        print(len(link_economy))

def scrap_multiple_pages_economy_news():
    link_economy = []
    valid_links = []  # List to store only valid links
    news_article = []
    headlines = []
    
    # Scraping links to economy news
    for i in range(1, 80):  # Adjust the range based on the number of pages to scrape
        url = f"https://www.ratopati.com/category/economy?page={i}"
        try:
            web = requests.get(url)
            soup = BeautifulSoup(web.content, "html.parser")
            required_div_list = soup.find_all("div", class_="columnnews mbl-col col3")
            for one_div in required_div_list:
                link = one_div.find("a")
                if link:
                    one_link = link.get("href")
                    link_economy.append(one_link)
            
            print(f"Processed page {i}, found {len(required_div_list)} articles.")
        except Exception as e:
            print(f"Error fetching page {i}: {e}")
    
    # Scraping individual economy news articles
    for one_economy_link in link_economy:
        try:
            web = requests.get(one_economy_link)
            soup = BeautifulSoup(web.content, "html.parser")
            
            # Extracting headline
            a = soup.find('h2', class_="heading")
            if not a:
                print(f"Skipping {one_economy_link}: No headline found.")
                continue
            headline = a.text
            
            # Extracting article content
            b = soup.find('div', class_="the-content")
            if not b:
                print(f"Skipping {one_economy_link}: No content found.")
                continue
            all_p = b.find_all('p')
            combined_paragraph = ' '.join(p.get_text(strip=True) for p in all_p)
            
            # Append only valid data
            valid_links.append(one_economy_link)
            headlines.append(headline)
            news_article.append(combined_paragraph)
        
        except Exception as e:
            print(f"Error processing {one_economy_link}: {e}")
    
    # Creating DataFrame and saving to CSV
    df = pd.DataFrame({
        "URL": valid_links,
        "news_article": news_article,
        "headline": headlines
    })
    
    print(f"Scraping complete. Total articles fetched: {len(valid_links)}")
    df.to_csv("economy_news.csv", index=False)


def scrap_multiple_pages_opinion_news():
    link_opinion = []
    valid_links = []  # List to store only valid links
    news_article = []
    headlines = []
    
    # Scraping links to opinion news
    for i in range(1, 80):  # Adjust the range based on the number of pages to scrape
        url = f"https://www.ratopati.com/category/opinion?page={i}"
        try:
            web = requests.get(url)
            soup = BeautifulSoup(web.content, "html.parser")
            required_div_list = soup.find_all("div", class_="columnnews mbl-col col3")
            for one_div in required_div_list:
                link = one_div.find("a")
                if link:
                    one_link = link.get("href")
                    link_opinion.append(one_link)
            
            print(f"Processed page {i}, found {len(required_div_list)} articles.")
        except Exception as e:
            print(f"Error fetching page {i}: {e}")
    
    # Scraping individual opinion news articles
    for one_opinion_link in link_opinion:
        try:
            web = requests.get(one_opinion_link)
            soup = BeautifulSoup(web.content, "html.parser")
            
            # Extracting headline
            a = soup.find('h2', class_="heading")
            if not a:
                print(f"Skipping {one_opinion_link}: No headline found.")
                continue
            headline = a.text
            
            # Extracting article content
            b = soup.find('div', class_="the-content")
            if not b:
                print(f"Skipping {one_opinion_link}: No content found.")
                continue
            all_p = b.find_all('p')
            combined_paragraph = ' '.join(p.get_text(strip=True) for p in all_p)
            
            # Append only valid data
            valid_links.append(one_opinion_link)
            headlines.append(headline)
            news_article.append(combined_paragraph)
        
        except Exception as e:
            print(f"Error processing {one_opinion_link}: {e}")
    
    # Creating DataFrame and saving to CSV
    df = pd.DataFrame({
        "URL": valid_links,
        "news_article": news_article,
        "headline": headlines
    })
    
    print(f"Scraping complete. Total articles fetched: {len(valid_links)}")
    df.to_csv("opinion_news.csv", index=False)




def main():
    scrap_multiple_pages_education_news()
    scrap_multiple_pages_sports_news()
    scrap_multiple_pages_entertainment_news()
    scrap_multiple_pages_health_news()
    scrap_multiple_pages_opinion_news()
    scrap_multiple_pages_economy_news()
   
if __name__ == "__main__":
    main()