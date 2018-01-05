""" 
Parse command line arguments using arg-parse
> mandatory arguments

This will throw an error if any of the parameter is not passed and will also show a help text
"""
import argparse
mandatory_args = OrderedDict()
mandatory_args['param1'] = "Parameter one"
mandatory_args['param2'] = "Parameter two"
parser = argparse.ArgumentParser()
if mandatory_args:
	mand = parser.add_argument_group("Mandatory arguments")
	for key, value in mandatory_args.items():
		mand.add_argument(key, help = value)
args = parser.parse_args()
print(args.param1)
print(args.param2)
