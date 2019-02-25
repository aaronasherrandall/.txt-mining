def main ():
	# read file
	file = open ( "yesno.txt", "r" )
	lines = file.readlines()
	file.close()

	# look for patterns
	countYes = 0
	countNo  = 0
	for line in lines:
		line = line.strip().upper()
		#print ( line )
		#if YES appears somewhere
		if line.find( "YES" )!= -1 and len(line)==3:
			countYes = countYes + 1
		#if NO appears somewhere
		if line.find( "NO" ) != -1 and len(line)==2:
			countNo = countNo + 1

	#display result
	print( "Yes: ", countYes )
	print( "No:  ", countNo )
main()