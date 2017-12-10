import requests
from bs4 import BeautifulSoup
import json
from industry_code_mapping import *
from zuaba_corp_details import *
from django.core.cache import cache

class McaDetails :
    def mca_details_fetch(self,company_name) :
        company_details_data = []

        headers = {'content-type': 'application/json'}
        response = requests.post("http://www.mca.gov.in/mcafoportal/checkCompanyName.do?counter=1&name1="+company_name+"&name2=&name3=&name4=&name5=&name6=&activityType1=&activityType2=&displayCaptcha=false",headers=headers)

        soupObject = BeautifulSoup(response.content, 'html.parser')
        table = soupObject.find_all('table')
        result_forms_table = soupObject.find('table', {'class': 'result-forms'})
        # key = company_name.replace(" ","_")
        # print key
        # if cache.get(company_name) != None :
        #     print "caching"
        #     return cache.get(company_name)
        # else :
        if result_forms_table != None :
            print result_forms_table
            for th in result_forms_table.find_all('tr',{'class': 'table-row'}) :
                td = th.find_all('td')
                cin_details = {}
                cin_number = td[0].text
                company_response_name = td[1].text
                if str(cin_number[0]).lower() == 'u' :
                    list_type = "Not Listed"
                else :
                    list_type = "Listed"
                zuaba_object = ZuabaDetails()
                zuaba_details = zuaba_object.zuaba_company_details_fetch(company_name, cin_number)

                cin_details['listed_or_not'] = list_type
                try :
                    cin_details['roc'] = zuaba_details['roc']
                    cin_details['company_type'] = zuaba_details['company_type']
                    cin_details['address'] = zuaba_details['address']
                except :
                    cin_details['company_type'] = industry_type_mapping(cin_number[1:6])

                cin_details['state'] = cin_number[6:8]
                cin_details['year'] = cin_number[8:12]
                cin_details['companyName'] = company_response_name

                company_details_data.append(cin_details)
                print company_details_data
        # cache.set(key,company_details_data,60)
        return json.dumps(company_details_data)
