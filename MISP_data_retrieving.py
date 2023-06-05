# @Author: Gillard Sébastien <gillard>
# @Date:   2021-07-09 11:03:19
# @Email:  sebastien.gillard@milak.ethz.ch
# @Last modified by:   gillard
# @Last modified time: 2021-10-16 15:37:05


from pymisp import ExpandedPyMISP
from keys import misp_url, misp_key, misp_verifycert
import time
from datetime import date, timedelta #, datetime
import os
import os.path
from os import path
import csv
import numpy as np
from Python_Function import save_file
# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__ == "__main__":

    # Initialisation
    today = date.today()

    misp = ExpandedPyMISP(misp_url, misp_key, misp_verifycert)

    stats_report = misp.users_statistics(context='data')
    stats_report = stats_report['stats']
    nb_of_pages = int(np.ceil(float(stats_report['event_count'])/2000.))

    """
    if path.exists("/home/gillard/Bureau/MISP_Analysis/Back-up/Events_created") == False:

        # Retrieving all events
        for k in range(1,nb_of_pages):
            res = misp.search(controller='events',return_format='json', limit=2000, page=k)
            for event in res:
                event_id = event['Event']['id']
                print(event_id)
                save_file(event,
                    "/home/gillard/Bureau/MISP_Analysis/Back-up/Events_created/" + str(today),
                    "event_" + event_id)
            time.sleep(60)
            print('timesleep ok')

        New_or_updated_events = 0
        New_or_updated_attributes = 0
        time_delta_str = str()

    else:

        # Definition of timedelta between last retrieving and the new
        modified = os.path.getmtime("/home/gillard/Bureau/MISP_Analysis/Back-up/Events_created")
        modificationTime = date.fromtimestamp(modified)

        time_delta = today - modificationTime
        print(today-time_delta)
        time_delta_str = str(time_delta.days)+"d"
        
        
        # Retrieving of the last created events
        res = misp.search(controller='events',return_format='json', date_from=str(today-time_delta), date_to=str(today))
        for event in res:
            event_id = event['Event']['id']
            print(event_id)
            save_file(event,
                      "/home/gillard/Bureau/MISP_Analysis/Back-up/Events_created/" + str(today),
                      "event_" + event_id)
        
        # Retrieving of the last created or modified events
        res1 = misp.search(controller='events',return_format='json', last=time_delta_str)
        for event in res1:
            event_id = event['Event']['id']
            print(event_id)
            save_file(event,
                      "/home/gillard/Bureau/MISP_Analysis/Back-up/Events_modified/" + str(today),
                      "event_" + event_id)
        New_or_updated_events = len(res1)
        print(len(res1))
      
        # Retrieving of the organisation on the instance
        res2 = misp.organisations(scope='all')
        for org in res2:
            org_id = org['Organisation']['id']
            print(org_id)
            save_file(org,
                    "/home/gillard/Bureau/MISP_Analysis/Back-up/Organisations/"+ str(today),
                    "org_" + org_id)
        print(len(res2))
    """
    # Statistics Report of Data

    # Retrieving the number of the last created or modified attributes
    res_attr = misp.search(controller='attributes',return_format='json', last=time_delta_str)
    New_or_updated_attributes = len(res_attr['Attribute'])

    new_stats_report = {'Retrieving Date': date.today() ,'MISP Version': str(misp.misp_instance_version['version'])}
    data_update = {'New or updated events': New_or_updated_events, 'New or updated attributes': New_or_updated_attributes}

    stats_report = {**new_stats_report, **stats_report, **data_update}

    stats_file = open("/home/gillard/Bureau/MISP_Analysis/Back-up/MISP_stats_file.csv","a+")
    if os.stat("/home/gillard/Bureau/MISP_Analysis/Back-up/MISP_stats_file.csv").st_size == 0:
        w = csv.DictWriter(stats_file, stats_report.keys())
        w.writeheader()
        w.writerow(stats_report)
    else:
        w = csv.DictWriter(stats_file, stats_report.keys())
        w.writerow(stats_report)





# Retrieve my own instance and check the differences
# Check galaxies to obtain the malware name -> Targeted Country

# LDS -> Prediction on Threat Level as 1st use case -> To improve and adapt with new event
#     -> Connect with MISP Instance to evaluate associated risk in real time
#     -> Count of malwares
#     -> Create geographical map of events, type of malwares, which country or org is infected by particular
#     -> Threat Level -> Analyse de l'importance de chaque attributs (pondération sur les attributs -> plus l'attribut est réutilisé, plus il a d'importance, plus sa pondération est grande)
#     -> Prédiction du tag, attribut et event
# Qui sont les data analysts et que font

# When we go on the DSL we have to change the files path for the save
