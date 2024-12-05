import requests
from bs4 import BeautifulSoup

links=[]
def scrap_ratopati():
    # urls=[]
    # url="https://www.onlinekhabar.com/content/news/rastiya"
    # web=requests.get(url)
    # print(web.content)
    # soup= BeautifulSoup(web.content,"html.parser")
    # print(soup.html.prettify())
    # ok-grid-12
    # news=soup.find("div",class_="ok=grid-12")
    # # print(news.prettify)
    # ff=news.find_all("div",class_="ok-news-post")
    # print(ff)
    # # for link in news.find_all('a',class_="ok-grid-12"):
    #     print(link)
    #     print(link.get("href"))
    web= requests.get("https://www.ratopati.com/category/education?page=1")
    soup=BeautifulSoup(web.content,"html.parser")
    required_div_list=soup.find_all("div",class_="columnnews mbl-col col3")
    for one_div in required_div_list:
        link=one_div.find("a")
        # print(link)
        one_link=link.get("href")
        # print(one_link)
        links.append(one_link)
    
    # print(links)


def showdata():
    for link in links :
        web=requests.get(link)
        print(web.status_code)
        
def scrap_multiple_pages_education_news():
    for i in range(1,2):
        url =f"https://www.ratopati.com/category/education?page={i}"
        web = requests.get(url)
        # print(web.status_code)
        soup=BeautifulSoup(web.content,"html.parser")
        required_div_list=soup.find_all("div",class_="columnnews mbl-col col3")
        for one_div in required_div_list:
            link=one_div.find("a")
            # print(link)
            one_link=link.get("href")
            # print(one_link)
            links.append(one_link)
    # print(links)
    print(len(links))

def scrap_multiple_pages_sports_news():
    pass

def main():
    # scrap_ratopati()
    # showdata()
    scrap_multiple_pages_education_news()
   
if __name__ == "__main__":
    main()