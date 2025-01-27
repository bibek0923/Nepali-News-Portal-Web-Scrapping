
import requests
from bs4 import BeautifulSoup
import pandas as pd
link_education=[]

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













def main():
    scrap_multiple_pages_education_news()
    
    
   
if __name__ == "__main__":
    main()