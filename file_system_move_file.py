import os

folder=r"C:/Users/a/Downloads/test"
newName="afsheen"
oldname="ameena"


	# Checking if the file is present in the list
if oldname in folder:

		# Rename the file
		os.rename(oldname, newName)

list = os.listdir(folder)
print(list)
