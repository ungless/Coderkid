#!/home1/coderkid/python/bin/python
import sys, os    

# Where /home/your_username is the path to your home directory
sys.path.insert(0, "/home1/coderkid/python")
sys.path.insert(13, "/home1/coderkid/public_html/Coderkid")

os.environ['DJANGO_SETTINGS_MODULE'] = 'Coderkid.settings'
from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")


