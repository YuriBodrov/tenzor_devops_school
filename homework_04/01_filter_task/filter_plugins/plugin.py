#!/usr/bin/python

import re # We can use a RegExp Python module (PE). A task with star (*). :-)

def filter_function(initValue):

  str_initValue = str(initValue) # Convert all potential variable values to string

  pattern = re.compile("[A-Fa-f0-9]+") # MAC Address pattern format!
  
  ### 1st check : If a variable has a String type ###########################################################
  ### 2d check  : If a variable has a Even-numbered lenght ##################################################
  ### 3d check  : MAC Address pattern format ################################################################
  if ((type(str_initValue) == str) and (len(str_initValue) % 2 == 0) and (pattern.fullmatch(str_initValue))):
    
    splitList = re.findall('[0-9, a-f, A-F]{2}', str_initValue) # Division by 2 Bytes
    
    delimiter = ":" # Initializing a delimiter

    # Joining a new split_list with a delimiter as a result:
    resValue = "Result is " + delimiter.join(splitList)

  else:
    resValue = "Error! There is(are) some error(s) with initial value : " + str_initValue
  ###########################################################################################################

  return resValue

class FilterModule(object):
  def filters(self):
    return {
      'filter_function': filter_function
    }