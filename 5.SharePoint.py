print("MD Parveen")
import sys
import requests
from requests_ntlm import HttpNtlmAuth
fileName = sys.argv[0]
sharePointUrl = 'https://hclo365.sharepoint.com/'
folderUrl = '/hclo365.sharepoint.com/:f:/r/sites/AutomationTeam17/Shared%20Documents/Trainings/Batch_4/Python%20Training/Evaluation?csf=1&web=1&e=yZzG2I'
requestUrl = sharePointUrl + '/_api/web/getfolderbyserverrelativeUrl(\'' + folderUrl + '\')/Files/add(Url=\'' + fileName + '\',overwrite=true)'
file = open(fileName, 'rb')
headers = {'Content-Type': 'appication\json; odata=verbose', 'accept': 'application/json; odata=verbose'}
r = requests.post(sharePointUrl + " /_api/contentinfo ", auth=HttpNtlmAuth('Domain\\username', 'password'), headers= headers)
uploadResult = requests.post(requestUrl, auth=HttpNtlmAuth('Domain\\username' , 'password'), headers=headers, data=file.read())                                                                                                                                                                                                                                                             data=file.read())