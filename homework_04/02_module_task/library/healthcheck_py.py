#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule
import sys
import json
from urllib.request import urlopen # For Python 3 env
#from urllib import urlopen # For Python 2.7 env

### Declaring of get_http_status function: #############################################
def get_http_status(strVal):
 
  try:
    
    statusCode = (urlopen(strVal)).getcode()

    if (statusCode == 200):
      str_status_code = "OK. Web Node is alive! Status code is : " + str(statusCode)

    else:
      str_status_code = "ERROR. Something is wrong! Status code is : " + str(statusCode)

  except:

    str_status_code = "Failed to connect to : " + strVal + "!"
    
  return (str_status_code)
########################################################################################

def main():
  ### Declaring Module arguments: ########
  module_args = dict(
    addr=dict(required=True, type='str')
    #tls=dict(type='bool', default="True")
  )
  
  ### Creating an Object > Module: #######
  module = AnsibleModule(
    argument_spec=module_args,
    supports_check_mode=False # We will make a potentional changes on remote systems
  )
  
  ### Getting all necessary arguments: ###
  addr = module.params["addr"]
  #tls = module.params["tls"]

  output = get_http_status(addr)
  
  print ("{\"msg\" : \"" + output + "\"}")
  
  sys.exit(0)

if __name__ == "__main__":
    main()
