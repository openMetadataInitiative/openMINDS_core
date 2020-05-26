#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:22:51 2020

@author: zehl
"""
import json
import warlock
import collections

class CollectionGenerator:
    """
    Class for generating an openMINDS conform metadata collection.
    
    The CollectionGenerator class dynamically reads the openMINDS schemas of a 
    given version for generating, validating, and storing corresponding json-LD 
    metadata files in an openMINDS conform metadata collection. 
        
    Attributes
    ----------
    version2use : str
        Used version of openMINDS schemas.
    store2 : str
        Absolute file path to where the openMINDS metadata collection is going 
        to be stored. 
        
    Methods
    -------
    
    """
    
    def __init__(self, version2use, store2):
        """
        Parameters
        ----------
        version2use : str
            Version of openMINDS schemas that should be used. Available versions
            are "v1.0", "v2.0", or "v3.0".
        store2 : str
            Absolute file path to where the openMINDS metadata collection should 
            be stored. 
        """
        self.openminds_version = version2use
        self.store2 = store2
        
        # define relative path to openMINDS version
        rpv = './%s' % version2use
        
        # open definitions.json to find out what schemas are available
        with open(rpv + '/definitions.json', 'r') as fp:
            definitions = json.load(fp)
        fp.close()
        
        # get names of all schemas within the definition.json file
        schema_names = list(definitions['definitions'].keys())
        
        # create class attributes for all available schemas
        self.schemas = collections.namedtuple('schemas', schema_names)
        
        # create class attributes for properties for each schema
        for sn in schema_names:
            # define relative path to openMINDS schema
            rp2s = '/'.join([rpv, 
                             definitions['definitions'][sn]['$id'].replace(
                                     '#', '') + '.schema.json'])
                    
            # open openMINDS json-schema to find out it's properties
            with open(rp2s, 'r') as fp:
                jschema = json.load(fp)
            fp.close()
            
            # replace '@type' and '@id' with python compatible dictionary keys
            jschema['properties']['at_type'] = jschema['properties'].pop('@type')
            jschema['properties']['at_id'] = jschema['properties'].pop('@id')
            jschema['required'].remove('@type')
            jschema['required'].append('at_type')
            jschema['required'].remove('@id')
            jschema['required'].append('at_id')
            
            # create method from schema using warlock
            setattr(self.schemas, sn, warlock.model_factory(jschema))
            
            # create docstring for each schema-method
            sm = getattr(self.schemas, sn)
            sm.__doc__ = """This is the documentation of %s""" % sn
