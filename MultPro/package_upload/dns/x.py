# -*- coding:utf-8 -*-

def method(x):
    import json
    from A import a
    pk = json.loads(x)
    domain = pk['domain']
    vec = a.method(domain)
    return (domain, vec)