import pyshorteners
import time

type_bitly = pyshorteners.Shortener(api_key='****************************************')

def loading(seconds):
    print("Loading, please wait...")
    time.sleep(seconds)
    

def url_shortner(original_url):
    loading(5)
    try:
        tiny_url = type_bitly.bitly.short(original_url)    
        return "The shortened url is: " + tiny_url

    except:
        return "Please enter a valid long URL"

def click_counts(url):
    loading(8)
    try:
        count = str(type_bitly.bitly.total_clicks(url))
        if count == '0':
            return "You haven't gotten any click on this url"
        else:
            return "Your URL " + url + " has " + count + " clicks."

    except:
        return "Please enter a valid short URL"

def url_expander(url):
    loading(5)
    try:
        expanded_url = type_bitly.bitly.expand(url)
        return "Your exopanded URL is: " + expanded_url 

    except:
        return "Please enter a valid short URL"