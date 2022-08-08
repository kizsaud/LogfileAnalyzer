import argparse
import os
import logging
from pyats.topology import loader
import sys
from ats.easypy import run

HERE = os.getcwd()

print("\nRunning the script from here:{0}\n".format(HERE))

# Parse and set the run time args - https://docs.python.org/3.3/library/argparse.html

# Creating a parser argument -
parser = argparse.ArgumentParser(description="Main job file for the DNAC Wired Client Assurance Feature test cases",
                                 usage='easypy job/dnac_ft/uniq-ft_extended_test.py -loglevel="DEBUG" --m=ef_bats')

# Define all the arguments -
# parser.add_argument('--m', action="store", required=True, help='Pass the marker name - only the tests with this '
#                                                                'marker will be executed. eg. "ef_bats"')
parser.add_argument('--controller_ip', action="store", required=True, help='IP Address of the controller')
parser.add_argument('--testbed_e2e', action="store", required=True, 
    help='Name of the testbed file. eg. bats_testbed.yaml')
parser.add_argument('--testbed', dest = 'testbed',
                        type = loader.load)
parser.add_argument('--config', action="store", required=True, help='Name of the config file. eg. '
                                                                    'northbound/config/<file>')
parser.add_argument('--device_list', action="store", required=True, help='List of devices to use as DUT')
parser.add_argument('--pdb', action="store_true", required=False, help='If the --pdb arg is passed we set pdb=True '
                                                                       'in the run() - default False')
parser.add_argument('--disable_checkout', action="store_true", required=False,
                    help='If the --disable_checkout arg is passed we dont execute the git checkout on the script.')
parser.add_argument('--input', action="store", required=True,
                        help='Name of the input file. eg. xyz_input.json')
parser.add_argument('--stop_on_traffic_failure', action="store_true", required=False,
                    help='If the --stop_on_traffic_failure arg is passed we stop on traffic failure.')

parser.add_argument('--script', action="store", required=False, help='Name of the script')

#If testbed is not underlay pre-config, script will configure underlay before discovery devices(tc3)
parser.add_argument('--underlay_config', action="store_true", required=False, help='if need script to configure underlay')

# Parse the sys.argv[1:] to get the parsed args - use vars() to convert the namespace to a dict.
run_time_args = vars(parser.parse_args())

print("The run time arguments are - \n {} \n".format(run_time_args))

#if run_time_args["script"]:
#    script_path = "{}".format(HERE, run_time_args["script"])

def main():

    # Changing the log level to debug -
    logging.getLogger('ats.aetest').setLevel('DEBUG')
    logging.getLogger('TaskLog').setLevel('DEBUG')
    script_path = "{}".format(HERE, run_time_args["script"])
    # Note - if the pdb is set to True - we enter pdb mode on assert failure -
    run(input_file=run_time_args["input"],
        script=run_time_args["script"],
        device_list=run_time_args["device_list"],
        controller_ip=run_time_args["controller_ip"], 
        testbed=run_time_args["testbed"],
        testbed_e2e=run_time_args['testbed_e2e'],
        testscript=run_time_args["script"], config=run_time_args["config"],
        stop_on_traffic_failure=run_time_args["stop_on_traffic_failure"],
        disable_checkout=run_time_args["disable_checkout"], pdb=run_time_args["pdb"])
        #pause_on=dict(action='pdb', patterns=[{'pattern': 'pytest.set_trace()'}, {'pattern': 'pdb.set_trace()'}]))
