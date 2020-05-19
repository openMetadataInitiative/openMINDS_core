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
        Úsed version of openMINDS schemas.
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
            
            # extract properties from schema
#            schema_props = list(jschema['properties'].keys())
            
            # replace '@type' and '@id' with valid identifiers in schema_props
            
            # create class attributes for properties for the schema
            for pn, pd in jschema['properties'].items():
                print(pn, pd)
                if '@' in pn:
                    pnattr = 'at_' + pn[1:]
                print(self.schemas.__dict__[sn], type(self.schemas.__dict__[sn]))
#                self.schemas.__dict__[sn] = collections.namedtuple(pnattr, pnattr)     
        
