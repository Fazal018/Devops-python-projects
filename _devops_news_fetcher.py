import requests

url="https://newsapi.org/v2/everything?q=devops&sortBy=publishedAt&apiKey=177d5087b4ff47aeaadb39cdb33aa15a"

try:
    response = requests.get(url)
    response.raise_for_status()
    
    data = response.json()
    
    with open("Devops_news_report.txt","w",encoding='utf-8') as file :
        for article in data["articles"][:5]:
            title=article["title"]
            source=article["source"]["name"]
            file.write(f"{title} - ({source})\n\n")
    print("Latest Devops News Saved in Devops_news_report.txt ")
    
except requests.exceptions.HTTPError as e:
    print("API Error :",e)

except Exception as e :
    print("Unexpected Error",type(e).__name__ , "-", e)
    
finally :
    print("Devops News fetch Task Completed ")
    
        
