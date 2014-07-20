import json
import requests
from exceptions import Exception

import Logging
from State import State

import subprocess


class VMProxy:
    #proxy object corresponding to a VM 
    vmproxy_list=[]
    def __init__(self, vm_ip, vm_id, lab_id):
        self.vm_ip=vm_ip
        self.vm_id=vm_id
        self.lab_id=lab_id
        self.status = "None"

    def get_VMProxy_list():
        vmproxy_list.append(self.vm_ip)
        vmproxy_list.append(self.vm_id)
        vmproxy_list.append(self.lab_id)
        return vmproxy_list

    def health_check():
       cmd = subprocess.Popen(['ping' , '-c1' , self.vm_ip] , stdout = subprocess.PIPE)
       output = cmd.communicate()[0]
       if "errors" in output :
           self.status = "DOWN"
       else :
           self.status = "UP"

