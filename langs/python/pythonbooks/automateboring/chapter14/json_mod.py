stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
import json
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print jsonDataAsPythonValue
print jsonDataAsPythonValue.__class__
'''
{u'miceCaught': 0, u'isCat': True, u'felineIQ': None, u'name': u'Zophie'}
'''

pythonValue  = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
stringOfJsonData = json.dumps(pythonValue)
print stringOfJsonData
print stringOfJsonData.__class__
'''
"{\"name\": \"Zophie\", \"isCat\": true, \"miceCaught\": 0, \"felineIQ\": null}"
'''