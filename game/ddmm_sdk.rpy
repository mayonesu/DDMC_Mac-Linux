
init -10 python:
    import urllib2, json
    ddmm_rpc_url = "http://127.0.0.1:41420/"
    ddmm_online = False
    try:
        request = urllib2.Request(ddmm_rpc_url, json.dumps({"method": "ping"}))
        urllib2.urlopen(request).read()
        ddmm_online = True
    except:
        ddmm_online = False

    def ddmm_make_request(payload):
        if ddmm_online:
            request = urllib2.Request(ddmm_rpc_url, json.dumps(payload))
            urllib2.urlopen(request).read()

    def ddmm_register_achievement(id, name, description):
        ddmm_make_request({"method": "register achievement", "payload": {"id": id, "name": name, "description": description}})

    def ddmm_earn_achievement(id):
        ddmm_make_request({"method": "earn achievement", "payload": {"id": id}})





label ddmm_register_achievement(id, name, description):
    $ ddmm_register_achievement(id, name, description)
    return



label ddmm_earn_achievement(id):
    $ ddmm_earn_achievement(id)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
