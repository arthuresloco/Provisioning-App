import json
import requests

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListView




class GetOrg(BoxLayout):
	#search_input = ObjectProperty()
	search_results = ObjectProperty()
	
	
	def get_org(self):
		org_file = {}
		url = "https://dashboard.meraki.com/api/v0/organizations"

		headers = {
    		'content-type': "application/json",
    		'x-cisco-meraki-api-key': "3145297b03d779c37a04297dc91544a30b316fdf",
    		'cache-control': "no-cache",
    		}

		search_response = requests.request("GET", url, headers=headers)
		request = self.found_org(search_response, org_file)
		
	def found_org(self, search_response, org_file):
		org_file =search_response.json()
		for org in org_file:
			print('Name: ', org['name'])
			print('ID: ' , org['id'])
		


			

class GetOrg(App):
	pass

if __name__ == '__main__':
	GetOrg() .run()


