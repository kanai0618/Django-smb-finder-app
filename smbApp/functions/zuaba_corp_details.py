import requests
from bs4 import BeautifulSoup
import json


class ZuabaDetails:

    def zuaba_company_details_fetch(self,company_name, uin_number) :
        headers = {'content-type': 'application/json'}
        response = requests.post("https://www.zaubacorp.com/company/"+company_name+"/"+uin_number,headers=headers)

        zuaba_company_details = {}

        soup = BeautifulSoup(response.content, 'html.parser')
        address_details = soup.find_all("div", class_="col-12")

        if address_details!= None :
            try :
                zuaba_company_details['address'] = address_details[0].find_all('p')[3].text
            except IndexError:
                print "List out of index"

        company_details_table = soup.find('table', {'class': 'table table-striped'})

        if company_details_table!= None :
            th = company_details_table.find_all('tr')
            td = th[3].find_all('td')
            zuaba_company_details['roc'] = td[1].text
            try :
                company_type = th[10].find_all('td')
                zuaba_company_details['company_type'] = company_type[1].text.replace("Click here to see other companies involved in same activity","")
            except :
                print "Error"    
        # print zuaba_company_details
        return zuaba_company_details
