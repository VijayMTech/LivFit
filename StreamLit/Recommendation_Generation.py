import requests
import json

class Generator:
    def __init__(self,nutrition_input:list,ingredients:list=[],params:dict={'n_neighbors':5,'return_distance':False}):
        self.nutrition_input=nutrition_input
        self.ingredients=ingredients
        self.params=params

    def set_request(self,nutrition_input:list,ingredients:list,params:dict):
        self.nutrition_input=nutrition_input
        self.ingredients=ingredients
        self.params=params

    def generate(self,):
        request={
            'nutrition_input':self.nutrition_input,
            'ingredients':self.ingredients,
            'params':self.params
        }
        try:
            response = requests.post(url='http://localhost:8000/predict/', data=json.dumps(request))
            #response_data = response.json()
            #print("Response:", response_data)
            return response
        except json.JSONDecodeError as e:
            print("JSON Decode Error:", e)
            return None
