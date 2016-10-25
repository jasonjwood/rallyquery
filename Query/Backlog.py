#Get list of ready backlog items
import json
import requests
from pyral import Rally, rallyWorkset

rally = Rally(server="rally1.rallydev.com", apikey="apikey goes here")
print rally.subscriptionName()




response = requests.get('https://rally1.rallydev.com/slm/webservice/v2.0/HierarchicalRequirement?query=(((Iteration%20=%20null)%20AND%20(Ready%20=%20True))%20AND%20(Project.Name%20=%20%22IME%20-%20Orcavengers%22))&order=Rank&fetch=true&stylesheet=/slm/doc/webservice/browser')
print response
backlog = json.loads(response.text)

print backlog
#with open("TestResult.json") as handle:
#	backlog = json.load(handle)

#Get Dev-Ready sum
plannedSum = 0.0
for story in backlog["QueryResult"]["Results"]:
	print story["_refObjectName"]
	print story["PlanEstimate"]
	if story["PlanEstimate"] is None:
		size = 0
	else:
		size = float(story["PlanEstimate"])
	
	plannedSum = plannedSum + size

print plannedSum

#Get prioritized count

#Get unprioritized count
