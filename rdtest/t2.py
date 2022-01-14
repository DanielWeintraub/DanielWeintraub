import requests
from pyrundeck import Rundeck
from icecream import ic
import yaml
import json

with open( "./secret.yml", "r") as configFile:
    config = yaml.safe_load(configFile)

def syncJob(name, project, dest):
    #Find Job
    snd_headers = { 'X-Rundeck-Auth-Token': config['creds']['snd'], "Accept": 'application/json' }
    myparams = { 'jobExactFilter': name }
    r = requests.get(f'https://{config["host"]["snd"]}/api/14/project/{project}/jobs',
            headers=snd_headers,
            params=myparams )
    jobs = json.loads(r.text)
    if len(jobs) != 1:
        raise ValueError("Number of jobs returned is not 1")
    job = jobs[0]
    
    myidlist = [ job['id'] ]
    myparams = { 'format': 'yaml', 'idlist': myidlist }
    r = requests.get(f'https://{config["host"]["snd"]}/api/14/project/{project}/jobs/export', headers=snd_headers, params=myparams)
    jobDefs = yaml.safe_load(r.text)
    if len(jobDefs) != 1:
        raise ValueError("Number of job defs is not 1")
    jobDef = jobDefs[0]
    
    jobDef['name'] += ' (SYNCED)'
    
    ic(jobDef)
    
    dest_headers = { 'X-Rundeck-Auth-Token': config['creds'][dest], 'Content-Type': 'application/yaml', "Accept": 'application/json' }
    myparams = { 'dupeOption': 'update' }
    r = requests.post(f'https://{config["host"][dest]}/api/14/project/{project}/jobs/import', headers=dest_headers, params=myparams, data=yaml.dump([jobDef]))
    response = json.loads(r.text)
    ic(response)
    
if __name__ == "__main__":
    projName = 'ClusterManager'
    jobName = 'Apply Customer Rundeck Instance'
    syncJob(name=jobName, project=projName, dest='stg')
    #syncJob(name=jobName, project=projName, dest='prod')
