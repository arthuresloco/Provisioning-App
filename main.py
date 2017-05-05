import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
import requests



class GetOrg(BoxLayout):
	search_input = ObjectProperty()
	search_results = ObjectProperty()


	def get_org(self):
		url = "https://dashboard.meraki.com/api/v0/organizations"

		headers = {
    		'content-type': "application/json",
    		'x-cisco-meraki-api-key': "3145297b03d779c37a04297dc91544a30b316fdf",
    		'cache-control': "no-cache",
    		'postman-token': "bd89db47-3ecf-47dc-327f-5aa2c34e6b25"
    		}

		response = requests.request("GET", url, headers=headers)
		print(response.text)
		
		
	def found_org(self, response, data):
		print(response.text)
		
		

class GetOrg(App):
	pass

if __name__ == '__main__':
	GetOrg() .run()


