#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess # Source: https://docs.python.org/2/library/subprocess.html#popen-constructor

def initialize_robot(path:str) -> list:
     # Declare variables
    robot_file = os.path.join(path, 'robot')

     # Declare environment variables
    env = dict(os.environ)
    env['ROBOT_JAVA_ARGS'] = '-Xmx8g -XX:+UseConcMarkSweepGC'
    env['PATH'] = os.environ['PATH']
    env['PATH'] += os.pathsep + path

    return [robot_file, env]

def convert_to_json(path:str, ont:str):
    """
    This method converts owl to JSON using ROBOT and the subprocess library
    """
   
    robot_file, env = initialize_robot(path)
    input_owl = os.path.join(path, ont.lower()+'.owl')
    output_json = os.path.join(path, ont.lower()+'.json')
    if not os.path.isfile(output_json):
        # Setup the arguments for ROBOT through subprocess
        call = ['bash', robot_file, 'convert', \
                                    '--input', input_owl, \
                                    '--output', output_json, \
                                    '-f', 'json']

        subprocess.call(call, env=env)
    
    return None

def extract_convert_to_json(path:str, ont_name:str, terms:str, mode:str):
    """
    This method extracts all children of provided CURIE
    """
    robot_file, env = initialize_robot(path)
    input_owl = os.path.join(path, ont_name.lower()+'.owl')
    output_json = os.path.join(path, ont_name.lower()+'.json')
    output_owl = os.path.join(path, ont_name.lower()+'_extracted_subset.owl')

    if ':' in terms:
        call = ['bash', robot_file, 'extract', \
                                    '--method', mode,
                                    '--input', input_owl, \
                                    '--output', output_owl, \
                                    '--term', terms, \
                                    'convert', \
                                    '--output', output_json, \
                                    '-f', 'json']
    else:
        call = ['bash', robot_file, 'extract', \
                                    '--method', mode, \
                                    '--input', input_owl, \
                                    '--output', output_owl, \
                                    '--term', terms, \
                                    'convert', \
                                    '--output', output_json, \
                                    '-f', 'json']

        subprocess.call(call, env=env)

    return None

def remove_axiom(path:str, ont_name:str, structuraltautologies):
    robot_file, env = initialize_robot(path)
    input_owl = os.path.join(path, ont_name.lower()+'.owl')
    output_owl = os.path.join(path, ont_name.lower()+'_reduced.owl')
    call = ['bash', robot_file, 'remove', \
                                '--input', input_owl, \
                                '--axioms', structuraltautologies, \
                                '--output', output_owl]
    return None