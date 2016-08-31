#from util import dbconnection

#db=dbconnection.client.kms

from pymongo import MongoClient
import sys
#db connection
try:
    client = MongoClient()
    print(client)
except:
    print ("Unexpected error:", sys.exc_info()[0])
val=[]

##No of persons in one room

db=client.kms

val=db.personal_detail.aggregate([
    {"$match": { "pevz:raum": {"$exists": "true" }}},
    {"$group":{"_id":"$pevz:raum"}}
    ])
 
for x in val:
    print(x)


'''val=db.personal_detail.aggregate([
    {"$match": { "pevz:raum": {"$exists": "true" }}},
    {"$group":{"_id":"$pevz:raum", "No Of People":{"$sum":1}}}
    ])
 
for x in val:
    print(x)
# No of person in one room sorted
val=db.personal_detail.aggregate([
    {"$match": { "pevz:raum": {"$exists": "true" }}},
    {"$group":{"_id":"$pevz:raum", "No Of People":{"$sum":1}}},
    {"$sort": {"No Of People":-1}}
    
    ])
for x in val:
    print(x)
#No of people working in every organization
val=db.personal_detail.aggregate([
    {"$match": { "pevz:name": {"$exists": "true" }}},
    {"$group":{"_id":"$pevz:name", "No Of People working":{"$sum":1}}},
    {"$sort": {"No Of People working":-1}}
    
    ])
for x in val:
    print(x)
#No of Male/Female
val=db.personal.aggregate([
    {"$match": { "pevz:anrede": {"$exists": "true" }}},
    {"$group":{"_id":"$pevz:anrede", "No Of People ":{"$sum":1}}},
    {"$sort": {"No Of People ":-1}}
    
    ])
for x in val:
    print(x)
# Person having anrede as -
val=db.personal.find( { "pevz:anrede": "-" } )
for x in val:
    print(x)
#Total number of person
val=db.personal.find({"_id":{"$ne": 0}}).count()
print(val)


## TODO Implement sorting in rooms
##wHO KNOWS WHO(As per same rooms and department)
##use test set to compare queries
##gender and who knows who

#how many offices are there
#how many organisations
#average number of each organisation

##text output the data


#from pub data
#journals published by ...
#who has most publications

#discontinued organisations
#

## no of people in a building '''