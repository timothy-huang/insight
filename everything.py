from bs4 import BeautifulSoup
import requests
import urllib.parse
import urllib.request

from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV3
from flask import Flask, url_for, jsonify, json
from collections import OrderedDict
from itertools import islice
app = Flask(__name__)


@app.route('/companies/<company_name>')
def outer_function(company_name):
    def get_first_url(input_string):
        new_url = "http://www.google.com/search?&q=" + urllib.parse.quote_plus(input_string)
        redirected_html = requests.get(new_url)
        link_soup = BeautifulSoup(redirected_html.text, 'lxml')
        links = link_soup.find_all('cite')
        current_contents = links[0].contents
        current_url_string = ""
        for i in current_contents:
        	current_url_string = current_url_string + i.string
        return current_url_string

    company_url_string = get_first_url(company_name + " official website")
    thing_string = company_name + " company core values site" + company_url_string
    company_core_values_url = get_first_url(thing_string)
    response = urllib.request.urlopen(company_core_values_url)
    profile_html = response.read()

    """
    Watson pipeline below.
    """
    url = "https://gateway.watsonplatform.net/personality-insights/api"
    username = "96e5a015-c7cc-4a04-b367-22b7960820a6"
    password = "cHWmBJpvvmjN"
    profile = 0
    # Getting the webpage, creating a Response object.

    personality_insights = PersonalityInsightsV3(
        version='2016-10-20',
        username=username,
        password=password)

    profile = personality_insights.profile(profile_html,
    content_type='text/html',raw_scores=True,
    consumption_preferences=True)
    traits_list = {}
    for i in profile["personality"]:
        for j in i["children"]:
            traits_list.update({j["name"]: j["percentile"]})
    o = OrderedDict(sorted(traits_list.items(), key=lambda x: x[1], reverse=True))
    sliced = islice(o.items(), 5)  # o.iteritems() is o.items() in Python 3
    sliced_o = OrderedDict(sliced)
    return json.dumps(sliced_o)

    """
    End Watson pipeline.
    """
if __name__ == '__main__':
    app.run(host= '0.0.0.0')

# # Extracting the source code of the page.
# data = response.text
#
# # Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
#
# soup = BeautifulSoup(data, 'lxml')
#
# # Extracting all the <a> tags into a list.
# tags = soup.find_all("a", "ga_job")
#
# company_list = []
# company_url_list = []
#
# # Extracting URLs from the attribute href in the <a> tags.
# for tag in tags:
#     current_url = base_url + tag.get("href")
#     this_response = requests.get(current_url)
#     this_soup = BeautifulSoup(this_response.text, 'lxml')
#     company_list.append(this_soup.find("div", class_ = "job-data-basics clearfix").find_all("span")[4].string)
#     #company_list.append(<span>H.I.M. Recruiters</span>)
# for company in company_list:
# 	new_url = 'http://www.google.com/search?&q=' + urllib.parse.quote_plus(company)
# 	redirected_html = requests.get(new_url)
# 	link_soup = BeautifulSoup(redirected_html.text, 'lxml')
# 	links = link_soup.find_all('cite')
# 	current_contents = links[0].contents
# 	current_url_string = ""
# 	for i in current_contents:
# 		current_url_string += i.string
# 	company_url_list.append(current_url_string)
#
# for i in company_url_list:
# 	api_url = "https://api.hunter.io/v2/domain-search?domain=" + i + "&api_key=5ec25a39348ec20db8456cc1abb170f55faf623d&limit=1"
# 	print(requests.get(api_url).json()["data"]["emails"][0]["value"])
