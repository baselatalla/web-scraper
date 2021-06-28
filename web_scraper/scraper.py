
import requests

from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
url1 = 'https://en.wikipedia.org/wiki/History_of_China'


def get_citations_needed_count(URL):
    web_page = requests.get(URL)
    soup = BeautifulSoup(web_page.content, 'html.parser')
    result = soup.findAll(text='citation needed')
    return len(result) 

def get_citations_needed_report(URL):
    web_page = requests.get(URL)
    soup = BeautifulSoup(web_page.content, 'html.parser')
    result = soup.findAll('p')
    counter = 0
    report_text = ''
    report_head = '\n **These Paragraghs need Citation** \n'
    decor0 = '****************************************************************** \n'
    decor1 = '------------------------------------------------------------------ \n'
    for x in result:

        p = x.findAll('a', title="Wikipedia:Citation needed")
        if p:
            counter += 1
            report_text += '\n'
            report_text += decor1
            report_text += f'paragragh number {counter}'
            report_text += '\n'
            report_text += '\n'
            report_text += x.text
            report_text += '\n'
            report_text += decor1
                
    report = decor0 + report_head +  report_text + decor0    
    print(report)
    return report







if __name__ == "__main__":
    # get_citations_needed_count(url)
    # get_citations_needed_count(url1)
    get_citations_needed_report(url)
    # get_citations_needed_report(url1)