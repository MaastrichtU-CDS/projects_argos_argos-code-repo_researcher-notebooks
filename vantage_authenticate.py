from vantage6.client import Client
import pandas as pd
import os
import sys

def authenticate():
    from vantage6.client import Client
    # authenticate
    client = Client("https://mdw-vantage6-argos.azurewebsites.net", 443, "/api")
    value = client.authenticate("maastro-jasper", "M6FgLyD4uNBQ52A8")
    client.setup_encryption("privkey_Maastro.pem")
    
    return client

def get_collab(client):
    organization_details = {'organization_id':[],'organization_name':[],'node_id':[], 'status':[], 'last_seen':[]}
    collab = client.collaboration.get(10)
    #print(len(collab['organization'])
    for organizations in collab['organizations']:        
        name = client.organization.get(organizations['id'])['name']
        node_details = client.organization.get(organizations['id'])['nodes']
        for nodes in node_details:
            organization_details['organization_id'].append(organizations['id'])
            organization_details['organization_name'].append(name)             
            node_id = nodes['id']            
            organization_details['node_id'].append(node_id)
            status = client.node.get(node_id)['status']
            last_seen = client.node.get(node_id)['last_seen']
            organization_details['status'].append(status)
            organization_details['last_seen'].append(last_seen)      
    details = pd.DataFrame(organization_details)
    return details
        

