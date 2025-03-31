import requests
import json



newAimodel = {"id": 1, "name": "lekat", "price": 45}
response = requests.post("http://localhost:5283/api/AIModels", json=newAimodel)
print(response)
response = requests.get("http://localhost:5283/api/AIModels")
aimodels = response.json()
print("get all")
print(response)

for aimodel in aimodels:
    print(aimodel)

update = {"id": 1, "name": "Updated", "price": 500}
response = requests.put("http://localhost:5283/api/AIModels/4", json=update)
print("opdaterer")
print(response)
print(response.json())

response = requests.get("http://localhost:5283/api/AIModels/4")
print("get 1")
print(response)
print(response.json())

response = requests.delete("http://localhost:5283/api/AIModels/7")
print(response)
print("delete")


response = requests.get("http://localhost:5283/api/AIModels")
afterdelete = response.json()
print("get all")
print(response)

for aimodel in afterdelete:
    print(aimodel)


