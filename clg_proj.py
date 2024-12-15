import requests
from bs4 import BeautifulSoup

link_education=[]
link_sports =[]
link_entertainment=[]
link_health=[]
link_economy=[]
link_opinion=[]
# def scrap_ratopati():
#     # urls=[]
#     # url="https://www.onlinekhabar.com/content/news/rastiya"
#     # web=requests.get(url)
#     # print(web.content)
#     # soup= BeautifulSoup(web.content,"html.parser")
#     # print(soup.html.prettify())f
#     # ok-grid-12
#     # news=soup.find("div",class_="ok=grid-12")
#     # # print(news.prettify)
#     # ff=news.find_all("div",class_="ok-news-post")
#     # print(ff)
#     # # for link in news.find_all('a',class_="ok-grid-12"):
#     #     print(link)
#     #     print(link.get("href"))
#     web= requests.get("https://www.ratopati.com/category/education?page=1")
#     soup=BeautifulSoup(web.content,"html.parser")
#     required_div_list=soup.find_all("div",class_="columnnews mbl-col col3")
#     for one_div in required_div_list:
#         link=one_div.find("a")
#         # print(link)
#         one_link=link.get("href")
#         # print(one_link)
#         link_education.append(one_link)
    
#     # print(links)



        
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
            link_education.append(one_link)
    # print(link_education)
    # print(len(link_education))
    web=requests.get("https://www.ratopati.com/story/462257/from-now-on-there-will-be-only-phd-teachers-in-kirtipur-campus")
    
    soup=BeautifulSoup(web.content,"html.parser")
    a=soup.find('h2',class_ = "heading" )
    print(a.text)
    b=soup.find('div',class_ = "the-content" )
    print(b.text)
def showdata():
    for link in link_education :
        web=requests.get(link)
        print(web.status_code)
        
        
     
def scrap_multiple_pages_sports_news():
     for i in range(1,2):
        url =f"https://www.ratopati.com/category/sports?page={i}"
        web = requests.get(url)
        # print(web.status_code)
        soup=BeautifulSoup(web.content,"html.parser")
        required_div_list=soup.find_all("div",class_="columnnews mbl-col col3")
        for one_div in required_div_list:
            link=one_div.find("a")
            # print(link)
            one_link=link.get("href")
            # print(one_link)
            link_sports.append(one_link)
        print(link_sports)
        print(len(link_sports))
def scrap_multiple_pages_entertainment_news():
     for i in range(1,2):
        url =f"https://www.ratopati.com/category/entertainment?page={i}"
        web = requests.get(url)
        # print(web.status_code)
        soup=BeautifulSoup(web.content,"html.parser")
        required_div_list=soup.find_all("div",class_="columnnews mbl-col col3")
        for one_div in required_div_list:
            link=one_div.find("a")
            # print(link)
            one_link=link.get("href")
            # print(one_link)
            link_entertainment.append(one_link)
        print(link_entertainment)
        print(len(link_entertainment))
def scrap_multiple_pages_health_news():
     for i in range(1,2):
        url =f"https://www.ratopati.com/category/health?page={i}"
        web = requests.get(url)
        # print(web.status_code)
        soup=BeautifulSoup(web.content,"html.parser")
        required_div_list=soup.find_all("div",class_="columnnews mbl-col col3")
        for one_div in required_div_list:
            link=one_div.find("a")
            # print(link)
            one_link=link.get("href")
            # print(one_link)
            link_health.append(one_link)
        print(link_health)
        print(len(link_health))
def scrap_multiple_pages_economy_news():
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
def scrap_multiple_pages_opinion_news():
     for i in range(1,2):
        url =f"https://www.ratopati.com/category/opinion?page={i}"
        web = requests.get(url)
        # print(web.status_code)
        soup=BeautifulSoup(web.content,"html.parser")
        required_div_list=soup.find_all("div",class_="columnnews mbl-col col3")
        for one_div in required_div_list:
            link=one_div.find("a")
            # print(link)
            one_link=link.get("href")
            # print(one_link)
            link_opinion.append(one_link)
        print(link_opinion)
        print(len(link_opinion))

def main():
    # scrap_ratopati()
    # showdata()
    # scrap_multiple_pages_education_news()
    # showdata()
    # scrap_multiple_pages_sports_news()
    # scrap_multiple_pages_entertainment_news()
    # scrap_multiple_pages_health_news()
    scrap_multiple_pages_opinion_news()
   
if __name__ == "__main__":
    main()