import requests

response = requests.get("http://localhost:5283/api/AIModels")
aimodels = response.json()
print(response)
print(aimodels)

for aimodel in aimodels:
    print(aimodel)