

xmlFileString = "Wi-Fi-FiOS-EXAMPLE"
charset="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789-_"


f = open("pingResult.txt","r")
pingResultText=f.read()
#print pingResultText
f.close()

def isPingBroken():
	if pingResultText.find("could not find") > 0:
		#print "ping Failed"
		modifyXML()
		print "yes"
	else:
		print "no"

def findModificationIndex(inputString):
	retIndex = inputString.find(charset[len(charset)-1])
	if retIndex == -1:
		return len(inputString) - 1
	return retIndex-1

def modifyXML():
	e = open(xmlFileString,'r')
	xmlResult = e.read()
	beginningIndex=xmlResult.find('<keyMaterial>')
	endIndex = xmlResult.find('</keyMaterial>')
	passPhrase = xmlResult[beginningIndex+13:endIndex]
	#print passPhrase
	#normal case
	modificationIndex = findModificationIndex(passPhrase)
	if modificationIndex == -1:
		subPhrase = charset[0]
		phraseLength = len(passPhrase)
		index = 0
		while (index < phraseLength):
			subPhrase = subPhrase + charset[0]
			index += 1
		passPhrase = subPhrase
	else:
		#print passPhrase[modificationIndex]
		workingChar = passPhrase[modificationIndex]
		newWorkingChar = charset.find(workingChar)+1
		passPhrase = passPhrase[0:modificationIndex] + charset[newWorkingChar] + passPhrase[modificationIndex+1:len(passPhrase)]
	#print passPhrase
	#print workingChar + charset[newWorkingChar]
	newXMLResult=xmlResult[0:beginningIndex+13] + passPhrase + xmlResult[endIndex:len(xmlResult)]
	#print newXMLResult
	e.close()
	e = open(xmlFileString,'w')
	e.write(newXMLResult)
	e.close()
	
isPingBroken()