#!/usr/bin/python
import sys
import xmlrpclib
import datetime    

api_url = "http://localhost:8000/RPC2"
client = xmlrpclib.Server(api_url, verbose=0)

hubKey = client.Hub.Login("admin", "admin" )
print hubKey

serverIds = client.Hub.ListServerIds(hubKey)

print serverIds

client.Hub.AttachToServers(hubKey, serverIds)

usernames = ["admin" for s in serverIds]

systemsPerServer = client.system.listUserSystems(hubKey, serverIds, [usernames])
print systemsPerServer