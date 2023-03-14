import argparse
import requests
import ga_helperFunctions as funcs

#TODO: generelize as template-method pattern

#region Helper functions
# ---------------------------------

def _verifyRequiredFields(data):
    funcs.verifyFieldInData('SerialNumber', data)
    #TODO: any else field?

# --------------------------------
#endregion Helper functions

# ---------------------------------
# Define the command line parameters
# ---------------------------------
parser = argparse.ArgumentParser(prog='ga_createPatient.py', description='Create (or updates) a patient in Geneyx Analysis')
# Patient data Json file
parser.add_argument('--data','-d', help = 'data JSON file', default='templates\patient.json')
# commands (optional)
parser.add_argument('--config','-c', help = 'configuration file', default='ga.config.yml')
args = parser.parse_args()

#read the config file
config = funcs.loadYamlFile(args.config)
print(config)

#prepare the data to send
data = funcs.loadDataJson(args.data)
_verifyRequiredFields(data)
# add user connection fields
data['ApiUserKey'] = config['apiUserKey']
data['ApiUserID'] = config['apiUserId']
print(data)

# send request
api = config['server']+'/api/CreatePatient'
print('Creating patient')
r = requests.post(api, json = data)
print(r)
print(r.content)