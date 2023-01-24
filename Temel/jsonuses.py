# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 01:37:36 2023

@author: erkan
"""

import json 

data='{"firstName":"engin","lastName":"demiroğ"}'

y= json.loads(data)

print(y["firstName"])
print(y["lastName"])



customer = {
    "firstName":"Engin",
    "email":"engindemirog@gmail.com"
    }

customerJson=json.dumps(customer)
print(customer)
print(json.dumps("Engin"))

