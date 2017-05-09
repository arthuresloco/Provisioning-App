import json
import requests

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton


class GetOrg(BoxLayout):
	
	search_results = ObjectProperty()
	
	def get_org(self):
		org_file = {}
		url = "https://dashboard.meraki.com/api/v0/organizations"

		headers = {
    		'content-type': "application/json",
    		'x-cisco-meraki-api-key': "<Your API Key",
    		'cache-control': "no-cache",
    		}

		search_response = requests.request("GET", url, headers=headers)
		request = self.found_org(search_response, org_file)
		
	def found_org(self, search_response, org_file):
		org_file = search_response.json()
		output_org = ['Organization:  {}   ID:  {}' .format(d['name'], d['id']) for d in org_file]
		self.search_results.item_strings = org_file
		self.search_results.adapter.data.clear()
		self.search_results.adapter.data.extend(output_org)
		self.search_results._trigger_reset_populate()
		
class Provision(App):
	pass

if __name__ == '__main__':
	Provision() .run()


 
