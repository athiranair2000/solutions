import requests
from bs4 import BeautifulSoup
import time
USER_AGENT={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:46.0 Gecko/20100101 Firefox/46.0'}
in_file = open("game.py", "rt") 
contents = in_file.read()          
in_file.close()                   
print(contents)
with open ('game.py', 'rt') as in_file:  
    for line in in_file: 
        (in_file(line.rstrip('/n')for line in in_file)
def fetch_results(word,name):
    assert isinstance(word,str),'word must be a str'
    assert isinstance(number,int),'number must be an integer'
    escape_word=word.replace('-','+')
    google_url="http://www.google.com/search?q={}&num={}&h1={}".format(escaped_word,number)
    response=requests.get(google_url,headers=USER_AGENT)
    responses.raise_for_status()
    return word,responses.txt
def parse_results(html,keyword):
    soup=BeautifulSoup(html,'html.parser')
    found_results=[]
    flag=1
    results_block=soup.find_all('div',attrs={'class':'g'})
for results in result_block:
    link=result.find('a',href=true)
    title=result.find('h3',attrs={'class':'st'})
    if link and title:
        link=link['href']
        title=title.get_text()
    if description:
      description=description.get_text()
    if link!='#':
      found_results.append({'keyword':keyword,'rank':rank,'title':title,'description':description,'link':link})
        flag ==1
return found_results
           
        
def scrape_google(word,number):
    try:
    keyword,html=fetch_results(word,number)
    results=parse_results(html,keyword)
    return results
    except  AssertionError:
     raise Exception("incorrect arguments parsed to functon")
    except requests.HTTPError:
     raise Exception("you appear to have been blocked by google")
    except requests.RequestException:
     raise Exception("Appears an issue with conection")
if __name__ == "__main__":
     keywords=[]
     data=[]
     for key in keywords:
       try:
       results=scrape_google(keyword,4)
       for result in results:
            data.append(result)
       except Exception as e:
            print(e)
       finally:
            time.sleep(10)
       print(data)


   

		          
