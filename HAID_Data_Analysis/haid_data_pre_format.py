import os
import glob
import json
import xmltodict

DIRSEARCHPAT = "DataFrom"
SAVEDIR      = "./haid_experiment_data_files"


def iter_data_subdirs():
	for topdir in glob.iglob(f'./{DIRSEARCHPAT}*'):
		for filepath in glob.iglob(f'{topdir}/*.xml'):
			yield filepath

def main():
	for i, path in enumerate(iter_data_subdirs()):
		xml_dict = None
		with open(path, 'r') as fp:
			xml_dict = xmltodict.parse(fp.read())

		json_str = json.dumps(xml_dict)
		path_toks = os.path.splitext(path)
		save_dest = SAVEDIR + '/' + path_toks[0].split('/')[-1] + '.json'

		with open(save_dest, 'w') as wp:
			wp.write(json_str)

if __name__ == '__main__':
	main()