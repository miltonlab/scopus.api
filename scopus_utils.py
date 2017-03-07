from elsapy.elsclient import ElsClient
from elsapy.elsprofile import ElsAuthor, ElsAffil
from elsapy.elsdoc import FullDoc, AbsDoc
from elsapy.elssearch import ElsSearch
import json

## Load configuration
conf_file = open("scopus_config.json")
CONFIG = json.load(conf_file)
conf_file.close()

def query_by_affiliation(institution):
    ## Initialize client
    client = ElsClient(CONFIG['apikey'])

    ## Initialize affiliation search object and execute search
    #aff_srch = ElsSearch('affil(institution)','affiliation')
    aff_srch = ElsSearch('affil("'+institution+'")','affiliation')
    aff_srch.execute(client)
    print ("aff_srch has", len(aff_srch.results), "results.")
    return aff_srch.results

def result_to_file(result):
    with open('scopus_result.txt', mode='wt', encoding='utf-8') as f:
        for lines in result:
            print(lines, file = f)
    f.close()


# def get_affiliation(id):
#     # s_id=record['dc:identifier'].split(':')[1]
#     ## Initialize client
#     client = ElsClient(CONFIG['apikey'])
#     # Initialize affiliation with ID as string
#     my_aff = ElsAffil(affil_id = id)
#     if my_aff.read(client):
#         print ("my_aff.name: ", my_aff.name)
#         my_aff.write()
#     else:
#         print ("Read affiliation failed.")
#     return my_aff


def get_affiliation(id_aff):
    ## Initialize client
    client = ElsClient(CONFIG['apikey'])
    # Initiate affiliation object
    #my_aff = ElsAffil(affil_id = '60101411')
    my_aff = ElsAffil(affil_id = id_aff)
    # read all the documents for this affiliation. NOTE: requires elevated APIkey permissions
    my_aff.read_docs(client)
    # print, for each document read in the previous statement, Scopus ID and list of authors (list of authors
    #for doc in my_aff.doc_list:
        #print (doc['dc:title'], doc['dc:identifier'], doc['authors'])    
    #  apparently being what you are after)
    return my_aff


def test():
    results = query_by_affiliation('Universidad Nacional de Loja')
    ##record_aff = results[0]
    #print(record_aff)
    for record_aff in results:
        id_aff = record_aff['dc:identifier'].split(':')[1]
        print(id_aff)
        aff = get_affiliation(id_aff)
        print (aff)
        print(aff.doc_list)
        #for doc in aff.doc_list:
            #print (doc['dc:title'], doc['dc:identifier'], doc['authors'])
            
if __name__=='__main__':
    test()
    
