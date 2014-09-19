from os.path import dirname, abspath
import os
import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))))
import pyocean

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN', '')
DROPLET_ID = '12345'

digitalocean = pyocean.DigitalOcean(ACCESS_TOKEN)
droplet = digitalocean.droplet.get(DROPLET_ID)

while True:
    try:
        droplet.destroy()
        break
    except pyocean.exceptions.DOException as e:
        print('Could not destroy droplet. Reason: %s' % e)

print('Destroyed droplet %s.' % droplet.name)
