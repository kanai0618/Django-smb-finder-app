import facebook
import requests
import json
import sys
import csv
from terminaltables import AsciiTable
from beautifultable import BeautifulTable


class FbSmbDetails :

    def fb_smb_details_fetch(self,company_name) :

        token = "EAADalfptvKoBAF5ViRyCMVKqkSprleg9OI9wHJuFoRiJ1ipFRgAMQBps8jcsBtlNAZB6P7M5dfbLY0Xx8BO6GzAPlRNevqZAuZCjUV0YWbO5M9db6HNryl1ComxZABPhu9yzZAnGV8HgQZBl3ctYZANsGleUKDEOtdYw1hrjTNk0dxHiZCDq3tHw"
        headers = {'content-type': 'application/json'}
        page_details = requests.get("https://graph.facebook.com/search?access_token=" + token +  "&q=" + company_name + "&type=page",auth=('user', 'pass'))

        fb_details_data = []
        if 'data' in page_details.json().keys() :
            for page in page_details.json()['data'] :
                fb_details = {}
                fb_details['company_name'] = page['name']
                details_data = requests.get("https://graph.facebook.com/v2.6/"+page['id']+"?fields=location,phone,about,contact_address,website,category,company_overview,founded,products&access_token=EAADalfptvKoBAF5ViRyCMVKqkSprleg9OI9wHJuFoRiJ1ipFRgAMQBps8jcsBtlNAZB6P7M5dfbLY0Xx8BO6GzAPlRNevqZAuZCjUV0YWbO5M9db6HNryl1ComxZABPhu9yzZAnGV8HgQZBl3ctYZANsGleUKDEOtdYw1hrjTNk0dxHiZCDq3tHw")
                if 'website' in details_data.json().keys() :
                    fb_details['website'] = details_data.json()['website']
                else :
        		    fb_details['website'] = None

        		# company_data_list.append(website)
                if 'category' in details_data.json().keys() :
                    fb_details['category'] = details_data.json()['category']
                else :
                    fb_details['category'] = None
                if 'phone' in details_data.json().keys() :
                    fb_details['phone_number'] = details_data.json()['phone']
                else :
                    fb_details['phone_number'] = None

        		# company_data_list.append(phoneNumber)
                if 'location' in details_data.json().keys() :
                    location = details_data.json()['location']
                    try :
                        fb_details['country'] = location['country']
                        fb_details['city'] = location['city']
                        fb_details['zip'] = location['zip']
                        fb_details['street'] = location['street']
                    except :
                        print "Not Found"
                else :
                    fb_details['location'] = None

                print json.dumps(fb_details)
                fb_details_data.append(fb_details)

        return json.dumps(fb_details_data)
