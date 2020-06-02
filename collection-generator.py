#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:22:51 2020

@author: zehl
"""
import json
import inspect
import warlock
import collections

class CollectionGenerator:
#    """
#    Class for generating an openMINDS conform metadata collection.
#    
#    The CollectionGenerator class dynamically reads the openMINDS schemas of a 
#    given version for generating, validating, and storing corresponding json-LD 
#    metadata files in an openMINDS conform metadata collection. 
#        
#    Attributes
#    ----------
#    version2use : str
#        Used version of openMINDS schemas.
#    store2 : str
#        Absolute file path to where the openMINDS metadata collection is going 
#        to be stored. 
#        
#    Methods
#    -------
#    """
    _class_docstring_temp = " ". join(
            ["Class", "for", "generating", "an", "openMINDS", "conform", 
             "metadata", "collection.", "\n\nThe", "CollectionGenerator",
             "class", "dynamically", "reads", "the", "openMINDS", "schemas", 
             "of", "a", "\ngiven", "version", "for", "generating,", 
             "validating,", "and", "storing", "corresponding", "json-LD",
             "\nmetadata", "files", "in", "an", "openMINDS", "conform", 
             "metadata", "collection", "\n\nAttributes", "\n----------",
             "\nversion2use : str", "\n    Used", "version", "of", "openMINDS",
             "schemas.", "\nstore2 : str", "\n    Absolute", "file", "path", 
             "to", "where", "the", "openMINDS", "metadata", "collection", 
             "is", "going", "\n    to", "be", "stored.", "\n\nMethods",
             "\n-------"])
    _method_docstring_temp = " ".join(
            ["Generates", "a", "dictionary", "that", "is", "conform", "with", 
             "\nthe", "openMINDS", "({version2use})", "schema", "{sn}.", 
             "\n\nParameters\n----------", "\n    DYNAMINCALLY-BUILT", 
             "\n\nReturns\n-------", "\n    Dictionary", "conform", "with", 
             "the", "openMINDS", "\n    ({version2use})", "schema", "{sn}."])
    
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
        
        # transpose schema attributes to schema subclasses
        method_desc = ""
        for sn in schema_names:
            # define relative path to openMINDS schema
            rp2s = '/'.join([rpv, 
                             definitions['definitions'][sn]['$id'].replace(
                                     '#', '') + '.schema.json'])
                    
            # open openMINDS json-schema to find out it's properties
            with open(rp2s, 'r') as fp:
                jschema = json.load(fp)
            fp.close()
            
            # replace '@type' and '@id' with python compatible arguments terms
            jschema['properties']['at_type'] = jschema['properties'].pop('@type')
            jschema['properties']['at_id'] = jschema['properties'].pop('@id')
            jschema['required'].remove('@type')
            jschema['required'].append('at_type')
            jschema['required'].remove('@id')
            jschema['required'].append('at_id')
            
            # create method from schema using warlock
            setattr(self.schemas, sn, warlock.model_factory(jschema))
            
            # create dynamic docstring for each schema method
            method_params = ""
            for p, d in jschema['properties'].items():
                method_params += " ".join(
                        ["\n   ", p, ":", d['type']])
                for k, v in d.items():
                    if k == 'type':
                        continue
                    elif k == 'items':
                        method_params += " ".join(
                                ["\n\texpects -", str(v)])
                    else:
                        method_params += " ".join(
                                ["\n       ", k, "-", str(v)])
            temp_docstr = self._method_docstring_temp.format(
                    version2use=version2use, sn=sn)
            
            # update method docstring
            sm = getattr(self.schemas, sn)
            sm.__name__ = sn
            sm.__doc__ = temp_docstr.replace(
                    "\n    DYNAMINCALLY-BUILT", method_params)
                
            # collect method description
            method_desc += "".join(["\n    ", sn, "(",
                    ", ".join(sorted(list(jschema['properties'].keys()))), ")"])

        self.__doc__ = self._class_docstring_temp + method_desc
        inspect.cleandoc(self)