from pyrundeck import Rundeck
import yaml

with open( "./t1conf.yml", "r") as configFile:
    config = yaml.safe_load(configFile)

print(config['creds'])

rundeck = Rundeck('http://manager.snd.rundeck.cloud',
                  token=config['creds']['sandbox'],
                  api_version=32,  # this is not mandatory, it defaults to 18
                 )

#run = rundeck.run_job(RUNDECK_JOB_ID, options={'option1': 'foo'})

#running_jobs = rundeck.get_executions_for_job(job_id=RUNDECK_JOB_ID, status='running')

#for job in running_jobs['executions']:
#  print("%s is running" % job['id'])
