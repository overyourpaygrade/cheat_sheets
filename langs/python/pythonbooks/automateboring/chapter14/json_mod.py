print "\nExample 1 - Reading JSON with the loads() function"

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
import json
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print jsonDataAsPythonValue
print jsonDataAsPythonValue.__class__
'''
{u'miceCaught': 0, u'isCat': True, u'felineIQ': None, u'name': u'Zophie'}
'''

print "\nExample 2 - Writing JSON with the dumps() function" 

pythonValue  = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
stringOfJsonData = json.dumps(pythonValue)
print stringOfJsonData
print stringOfJsonData.__class__
'''
"{\"name\": \"Zophie\", \"isCat\": true, \"miceCaught\": 0, \"felineIQ\": null}"
'''