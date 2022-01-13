import requests
from pyrundeck import Rundeck
from icecream import ic
import yaml

with open( "./secret.yml", "r") as configFile:
    config = yaml.safe_load(configFile)

snd_rundeck = Rundeck('http://manager.snd.rundeck.cloud',
                  token=config['creds']['snd'],
                  api_version=32 )

stg_rundeck = Rundeck('http://manager.stg.rundeck.cloud',
                  token=config['creds']['stg'],
                  api_version=32 )

proj = 'ClusterManager'

j1 = snd_rundeck.get_job( name='Create or Update Customer Rundeck Instance', project='ClusterManager' )

j1 = yaml.safe_load(snd_rundeck.get_job_def( job_id=j1['id'], format='yaml'))

snd_headers = { 'X-Rundeck-Auth-Token': config['creds']['snd'] }
myidlist = [ j1[0]['id'] ]
myparams = { 'format': 'yaml', 'idlist': myidlist }
ic(myparams)
r = requests.get(f'https://{config["host"]["snd"]}/api/14/project/{proj}/jobs/export', headers=snd_headers, params=myparams)
j2 = yaml.safe_load(r.text)
ic(j1,j2)
