import sys
from collections import Counter

def list_files_in_common(files):
	outfiles = Counter()
	for f in files:
		includes_seen = False
		for line in open(f).readlines():
			if line.startswith("#include"):
				includes_seen = True
				# this assumes every include is "#include [filename]"
				included_file = line.split(" ")[1].strip().replace('"', '')
				if not included_file.startswith("<"):
					outfiles[included_file] += 1
			
			# this assumes all the includes are grouped together
			elif includes_seen:
				break
	return outfiles


# a utility that I'm using like so:
# git grep "struct_whose_definition_i_cannot_find_in_this_mess" | xargs python script/funcfinder.py
if __name__ == "__main__":
	files = sys.argv[1:]
	files = filter(lambda s:s.endswith(".c") or s.endswith(".h"), files)
	for k, v in list_files_in_common(files).most_common()[:10]:
		print k, v
