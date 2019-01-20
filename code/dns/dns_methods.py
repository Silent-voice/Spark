# -*- coding: utf-8 -*-
import json

def extract_id_domain(x):
    pk = json.loads(x)
    return (pk['id'], pk['domain'])



def domain_to_vec(x):
    static = __import__('static')
    static._init()
    charList = static.get_value('charList')
    domain = x[1]
    vec = []

    for char in domain:
        try:
            vec.append(charList[char])
        except:
            print ('unexpected char' + ' : ' + char)
            vec.append(0)

    return (domain,vec)