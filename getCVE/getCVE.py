import vulnerable
import requests 
from bs4 import BeautifulSoup 
from packaging.version import parse  

'''
get number of pages  
return number of pages and page_url 
'''
def get_number_pages(soup) :  
    
    '''
    get all page url  
    '''
    pagingb = soup.find('div', id='pagingb') 
    pages = pagingb.find_all('a') 
    page_url = [] 
    for page in pages : 
        url = page.attrs['href']
        page_url.append('https://www.cvedetails.com' + url)  
    return len(pages), page_url 

'''
get all rows in main table in one page 
'''
def get_rows_table(page_url) : 
    page_rsp = requests.get(page_url)
    page_soup = BeautifulSoup(page_rsp.text, 'lxml')
    table = page_soup.find('table', attrs={'class' : 'listtable'}) 
    table_row = table.find_all('tr')[1:] 
    return table_row   


'''
get vulnerable by url  
'''
def get_vulnerable_url (page_url) : 
    vuln_list = []
    page_rsp = requests.get(page_url)
    page_soup = BeautifulSoup(page_rsp.text, 'lxml')
    table = page_soup.find('table', attrs={'id' : 'vulnslisttable'})  
    rows = table.find_all('tr')[1:]
    for i in range(0, len(rows), 2) : 
        cols = list(map(lambda x : x.string , rows[i].find_all('td')))
        vuln = vulnerable.vulnerable(cols[1], cols[4].strip(), cols[5], cols[7], cols[9], rows[i+1].text.strip()) 
        vuln_list.append(vuln) 
    return vuln_list 


'''
get vulnerable by version 
'''
def get_vulnerable_ver(check_version, url) : 
    rsp = requests.get(url) 
    soup = BeautifulSoup(rsp.text, 'lxml') 
    num_pages, pages_url = get_number_pages(soup) 
    for i in range(num_pages) : 
        rows = get_rows_table(pages_url[i]) 
        for r in rows : 
            colums = r.find_all('td') 
            vuln_version = colums[0].string.strip()
            if (vuln_version == check_version) or vuln_version in ["-", ""]: 
                vuln_url = 'https://www.cvedetails.com' + colums[5].find_all('a')[1].attrs['href'] 
                return get_vulnerable_url(vuln_url)  

            if parse(vuln_version) < parse(check_version) : 
                return []
            
if __name__ == '__main__' : 
    url = 'https://www.cvedetails.com/version-list/26/50646/1/Microsoft-Visual-Studio-Code.html' 
    vuln_list = get_vulnerable_ver('69.0', url)  
    if len(vuln_list) == 0 : 
        print("No vulnerable")
    else : 
        for vuln in vuln_list : 
            vuln.get_info() 