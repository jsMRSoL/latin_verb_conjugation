"""my xml-printing verb-conjugating program"""
from sys import argv

myVerbEndings = [
	["o", "as", "at", "amus", "atis", "ant"],
	["o", "s", "t", "mus", "tis", "nt"],
	["o", "is", "it", "imus", "itis", "unt"],
	["io", "is", "it", "imus", "itis", "iunt"],
	["o", "s", "t", "mus", "tis", "unt"],
	["or", "aris", "atur", "amur", "amini", "antur"],
	["or", "ris", "tur", "mur", "mini", "ntur"],
	["or", "eris", "itur", "imur", "imini", "untur"],
	["ior", "ieris", "itur", "imur", "imini", "iuntur"],
	["or", "eris", "tur", "mur", "mini", "untur"],
	["bam", "bas", "bat", "bamus", "batis", "bant"],
	["bar", "baris", "batur", "bamur", "bamini", "bantur"],
	["i", "isti", "it", "imus", "istis", "erunt"],
	["sum", "es", "est", "sumus", "estis", "sunt"],
	["eram", "eras", "erat", "eramus", "eratis", "erant"],
	["bo", "bis", "bit", "bimus", "bitis", "bunt"],
	["am", "es", "et", "emus", "etis", "ent"],
	["bor", "beris", "bitur", "bimur", "bimini", "buntur"],
	["ar", "eris", "etur", "emur", "emini", "entur"],
	["ero", "eris", "erit", "erimus", "eritis", "erint"],
	["ero", "eris", "erit", "erimus", "eritis", "erunt"],
	["em", "es", "et", "emus", "etis", "ent"],
	["am", "as", "at", "amus", "atis", "ant"],
	["er", "eris", "etur", "emur", "emini", "entur"],
	["ar", "aris", "atur", "amur", "amini", "antur"],
	["m", "s", "t", "mus", "tis", "nt"],
	["rer", "reris", "retur", "remur", "retis", "rentur"],
	["erim", "eris", "erit", "erimus", "eritis", "erint"],
	["sim", "sis", "sit", "simus", "sitis", "sint"]
]

class Verb(object):
	irreg = False
	dep = False
	semiDep = False
	PtPres = "none given"
	PtInf = "none given"
	PtPerf = "none given"
	PtPpp = "none given"
	
	def __init__(self, PrinPtsStringM):
		if "-" in PrinPtsStringM:
			Pts = PrinPtsStringM.split("-")
			self.Meanings = Pts[1].strip()
			PrinPtsString = Pts[0]
		elif ":" in PrinPtsStringM:
			Pts = PrinPtsStringM.split(":")
			self.Meanings = Pts[1].strip()
			PrinPtsString = Pts[0]
			
		PrinPts = PrinPtsString.split(", ")
		self.PtPres = PrinPts[0].strip()
		self.PtInf = PrinPts[1].strip()
		if len(PrinPts) > 2: 
			self.PtPerf = PrinPts[2].strip()
		if len(PrinPts) > 3:
			self.PtPpp = PrinPts[3].strip()
		
		self.PartsCount = len(PrinPts)
		
		if self.PtPres[len(self.PtPres) - 1] == "r":
			self.dep = True
			
		if "sum" in self.PtPres:
			self.irreg = True
			
		if (self.PtPres[len(self.PtPres) - 1] == "o") and (self.PtPerf[len(self.PtPerf) - 3:len(self.PtPerf)] == "sum"):
			self.semiDep = True
			
		#work out conjugation
		if self.PtInf[len(self.PtInf) - 3: len(self.PtInf)] == "are" \
			or self.PtInf[len(self.PtInf) - 3: len(self.PtInf)] == "ari":
			self.conj = "1"
		elif self.PtInf[len(self.PtInf) - 3: len(self.PtInf)] == "ire" \
			or self.PtInf[len(self.PtInf) - 3: len(self.PtInf)] == "iri":
			self.conj = "4"
		elif self.PtInf[len(self.PtInf) - 3: len(self.PtInf)] == "eri" \
			or (self.PtInf[len(self.PtInf) - 3: len(self.PtInf)] == "ere" \
			and self.PtPres[len(self.PtPres) - 2: len(self.PtPres)] == "eo"):
			self.conj = "2"
		elif self.PtInf[len(self.PtInf) - 3: len(self.PtInf)] == "ere" \
			and self.PtPres[len(self.PtPres) - 2: len(self.PtPres)] == "io":
			self.conj = "3.5"
		elif self.PtPres[len(self.PtPres) - 3: len(self.PtPres)] == "ior":
			self.conj = "3.5"		
		else:
			self.conj = "3"
		
		
			
	def printPrinPts(self):
		print "Total parts given: ", self.PartsCount
		print "Present tense: ", self.PtPres
		print "Infinitive: ", self.PtInf
		print "Perfect: ", self.PtPerf
		print "Meaning(s): ", self.Meanings
		print "Moodle meanings q: ", self.myMeaningQ
		#print "Final pres: ", self.PtPres[len(self.PtPres) - 1]
		#print "Final pf: ", self.PtPerf[len(self.PtPerf) - 3:len(self.PtPerf)] == "sum"
		#print "Final pf string: ", self.PtPerf[len(self.PtPerf) - 4:len(self.PtPerf)]
		#print "Final char: ", self.PtPerf[len(self.PtPerf)-1]
		#print "Hidden chars? ", repr(self.PtPerf)
		#print "Dep? ", self.dep
		#print "semiDep? ", self.semiDep
		if self.dep == True:
			print "Is deponent?: Yes"
		elif self.semiDep == True:
			print "PPP: ", self.PtPpp
			print "Is deponent?: Semi-deponent"
		else:
			print "PPP: ", self.PtPpp
			print "Is deponent?: No"
		print "Conjugation: ", self.conj
		print "Pres tense active: ", self.PresAct
		print "Pres tense passive: ", self.PresPass
		print "Impf tense active: ", self.ImpfAct
		print "Impf tense passive: ", self.ImpfPass
		print "Perf tense active: ", self.PerfAct
		print "Perf tense passive: ", self.PerfPass
		print "Plpf tense active: ", self.PlpfAct
		print "Plpf tense passive: ", self.PlpfPass
		print "Fut tense active: ", self.FutAct
		print "Fut tense passive: ", self.FutPass
		print "FutPf tense active: ", self.FutPfAct
		print "FutPf tense passive: ", self.FutPfPass
		print "Pres active subj: ", self.PresActSubj
		print "Pres passive subj: ", self.PresPassSubj
		print "Impf active subj: ", self.ImpfActSubj
		print "Impf passive subj: ", self.ImpfPassSubj
		print "Perf active subj: ", self.PerfActSubj
		print "Perf passive subj: ", self.PerfPassSubj
		print "Plpf active subj: ", self.PlpfActSubj
		print "Plpf passive subj: ", self.PlpfPassSubj
		print "Peri Fut subj: ", self.PeriFutSubj
		print "#######################################"
		print "+++++++++++++++++++++++++++++++++++++++"

	def getMeaningsQ(self):
		myMeaningsArr = self.Meanings.split(",")
		MeaningQ = '{1:SHORTANSWER:'
		for i in range(len(myMeaningsArr)):
			MeaningQ = MeaningQ + '~%100%' + myMeaningsArr[i].strip()
		MeaningQ = MeaningQ + '}'
		self.myMeaningQ = MeaningQ
	
	def conjPresAct(self):		
		if self.dep == False:
			if self.conj == "1":
				myIndex = 0
				myParingNo = 3
			if self.conj == "2":
				myIndex = 1
				myParingNo = 2
			if self.conj == "3":
				myIndex = 2
				myParingNo = 3
			if self.conj == "3.5":
				myIndex = 3
				myParingNo = 3
			if self.conj == "4":
				myIndex = 4
				myParingNo = 2
		else:
			if self.conj == "1":
				myIndex = 5
				myParingNo = 3
			if self.conj == "2":
				myIndex = 6
				myParingNo = 2
			if self.conj == "3":
				myIndex = 7
				myParingNo = 1
			if self.conj == "3.5":
				myIndex = 8
				myParingNo = 1
			if self.conj == "4":
				myIndex = 9
				myParingNo = 2
		
		
		self.PresAct = []
		for i in range(6):
			if i == 1 and (self.conj == "3" or self.conj == "4") and self.dep == True:
				myPart = self.PtInf[0:len(self.PtInf) - myParingNo] + myVerbEndings[myIndex][i] + "( not future!)"
			else:
				myPart = self.PtInf[0:len(self.PtInf) - myParingNo] + myVerbEndings[myIndex][i]
			self.PresAct.append(myPart)

	def conjPresPass(self):		
		if self.dep == False:
			if self.conj == "1":
				myIndex = 5
				myParingNo = 3
			if self.conj == "2":
				myIndex = 6
				myParingNo = 2
			if self.conj == "3":
				myIndex = 7
				myParingNo = 3
			if self.conj == "3.5":
				myIndex = 8
				myParingNo = 3
			if self.conj == "4":
				myIndex = 9
				myParingNo = 2
		
		
			self.PresPass = []
			for i in range(6):
				if i == 1 and (self.conj == "3" or self.conj == "4"):
					myPart = self.PtInf[0:len(self.PtInf) - myParingNo] + myVerbEndings[myIndex][i] + ' (not future!)'
				else:				
					myPart = self.PtInf[0:len(self.PtInf) - myParingNo] + myVerbEndings[myIndex][i]
				self.PresPass.append(myPart)
						
		else:
			self.PresPass = "None"
			
	def conjImpfAct(self):		
		if self.dep == False:
			myIndex = 10
			myParingNo = 3
			if self.conj == "1":
				myThemVowel = "a"
			if self.conj == "2":
				myThemVowel = "e"
			if self.conj == "3":
				myThemVowel = "e"
			if self.conj == "3.5":
				myThemVowel = "ie"
			if self.conj == "4":
				myThemVowel = "ie"
		else:
			myIndex = 11
			if self.conj == "1":
				myParingNo = 3
				myThemVowel = "a"			
			if self.conj == "2":
				myParingNo = 3
				myThemVowel = "e"
			if self.conj == "3":
				myParingNo = 1
				myThemVowel = "e"
			if self.conj == "3.5":
				myParingNo = 1
				myThemVowel = "ie"
			if self.conj == "4":
				myParingNo = 3
				myThemVowel = "ie"
				
		self.ImpfAct = []
		for i in range(6):
			myPart = self.PtInf[0:len(self.PtInf) - myParingNo] + myThemVowel + myVerbEndings[myIndex][i]
			self.ImpfAct.append(myPart)					

	def conjImpfPass(self):		
		if self.dep == False:
			myParingNo = 3
			myIndex = 11
			if self.conj == "1":
				myParingNo = 3
				myThemVowel = "a"			
			if self.conj == "2":
				myParingNo = 3
				myThemVowel = "e"
			if self.conj == "3":
				myParingNo = 3
				myThemVowel = "e"
			if self.conj == "3.5":
				myParingNo = 3
				myThemVowel = "ie"
			if self.conj == "4":
				myParingNo = 3
				myThemVowel = "ie"
				
			self.ImpfPass = []
			for i in range(6):
				myPart = self.PtInf[0:len(self.PtInf) - myParingNo] + myThemVowel + myVerbEndings[myIndex][i]
				self.ImpfPass.append(myPart)	

		else:
			self.ImpfPass = "None"
			
	def conjPerfAct(self):
		if self.PtPerf != "none given":	
			self.PerfAct = []
			if self.dep == False and self.semiDep == False:
				for i in range(6):
					myPart = self.PtPerf[0:len(self.PtPerf) - 1] + myVerbEndings[12][i]
					self.PerfAct.append(myPart)
			else:
				for i in range(3):
					myPart = self.PtPerf[0:len(self.PtPerf) - 4] + " " + myVerbEndings[13][i]
					self.PerfAct.append(myPart)
				for i in range(3,6):
					myPart = self.PtPerf[0:len(self.PtPerf) - 6] + "i " + myVerbEndings[13][i]
					self.PerfAct.append(myPart)
		else:
			self.PerfAct = "No perfect given"					

	def conjPerfPass(self):
		if self.dep == False and self.semiDep == False:
			if self.PtPpp != "none given":
				self.PerfPass = []
				for i in range(3):
					myPart = self.PtPpp + " " + myVerbEndings[13][i]
					self.PerfPass.append(myPart)
				for i in range(3,6):
					myPart = self.PtPpp[0:len(self.PtPpp) - 2] + "i " + myVerbEndings[13][i]
					self.PerfPass.append(myPart)
			else:
				self.PerfPass = "no PPP given"
		else:
			self.PerfPass = "None"		

	def conjPlpfAct(self):
		if self.PtPerf != "none given":	
			self.PlpfAct = []
			if self.dep == False and self.semiDep == False:
				for i in range(6):
					myPart = self.PtPerf[0:len(self.PtPerf) - 1] + myVerbEndings[14][i]
					self.PlpfAct.append(myPart)

			else:
				for i in range(3):
					myPart = self.PtPerf[0:len(self.PtPerf) - 4] + " " + myVerbEndings[14][i]
					self.PlpfAct.append(myPart)
				for i in range(3,6):
					myPart = self.PtPerf[0:len(self.PtPerf) - 6] + "i " + myVerbEndings[14][i]
					self.PlpfAct.append(myPart)
		else:
			self.PlpfAct = "No perfect given"					

	def conjPlpfPass(self):
		if self.dep == False and self.semiDep == False:
			if self.PtPpp != "none given":
				self.PlpfPass = []
				for i in range(3):
					myPart = self.PtPpp + " " + myVerbEndings[14][i]
					self.PlpfPass.append(myPart)
				for i in range(3,6):
					myPart = self.PtPpp[0:len(self.PtPpp) - 2] + "i " + myVerbEndings[14][i]
					self.PlpfPass.append(myPart)
			else:
				self.PlpfPass = "no PPP given"
		else:
			self.PlpfPass = "None"
				
	def conjFutAct(self):
		if self.dep == False:
			if self.conj == "1" or self.conj == "2":		
				myIndex = 15
				myParingNo = 3
				if self.conj == "1":
					myThemVowel = "a"
				if self.conj == "2":
					myThemVowel = "e"
			else:
				myIndex = 16
				myParingNo = 3
				if self.conj == "3":
					myThemVowel = ""
				if self.conj == "3.5":
					myThemVowel = "i"
				if self.conj == "4":
					myThemVowel = "i"	
			
			self.FutAct = []
			for i in range(6):
				if i == 0 and (self.conj == "3" or self.conj == "3.5" or self.conj == "4"):
					myPart = self.PtInf[0:len(self.PtInf) - myParingNo] + myThemVowel + myVerbEndings[myIndex][i] + ' (not subjunctive!)' 
				else: 
					myPart = self.PtInf[0:len(self.PtInf) - myParingNo] + myThemVowel + myVerbEndings[myIndex][i]
				self.FutAct.append(myPart)
				
		else:
			if self.conj == "1" or self.conj == "2":		
				myIndex = 17
				myParingNo = 3
				if self.conj == "1":
					myThemVowel = "a"
				if self.conj == "2":
					myThemVowel = "e"
			else:
				myIndex = 18
				if self.conj == "3":
					myParingNo = 1
					myThemVowel = ""
				if self.conj == "3.5":
					myParingNo = 1
					myThemVowel = "i"
				if self.conj == "4":
					myParingNo = 3
					myThemVowel = "i"	
			
			self.FutAct = []
			for i in range(6):
				if i == 0 and (self.conj == "3" or self.conj == "3.5" or self.conj == "4"):
					myPart = self.PtInf[0:len(self.PtInf) - myParingNo] + myThemVowel + myVerbEndings[myIndex][i] + ' (not subjunctive!)'
				elif i == 1 and (self.conj == "3" or self. conj == "3.5" or self.conj == "4"):
					myPart = self.PtInf[0:len(self.PtInf) - myParingNo] + myThemVowel + myVerbEndings[myIndex][i] + ' (not present!)'
				else:				
					myPart = self.PtInf[0:len(self.PtInf) - myParingNo] + myThemVowel + myVerbEndings[myIndex][i]
				self.FutAct.append(myPart)			

	def conjFutPass(self):
		if self.dep == False:
			if self.conj == "1" or self.conj == "2":		
				myIndex = 17
				myParingNo = 3
				if self.conj == "1":
					myThemVowel = "a"
				if self.conj == "2":
					myThemVowel = "e"
			else:
				myIndex = 18
				if self.conj == "3":
					myParingNo = 3
					myThemVowel = ""
				if self.conj == "3.5":
					myParingNo = 3
					myThemVowel = "i"
				if self.conj == "4":
					myParingNo = 3
					myThemVowel = "i"	
			
			self.FutPass = []
			for i in range(6):
				if i == 0 and (self.conj == "3" or self.conj == "3.5" or self.conj == "4"):
					myPart = self.PtInf[0:len(self.PtInf) - myParingNo] + myThemVowel + myVerbEndings[myIndex][i] + ' (not subjunctive!)'
				elif i == 1 and (self.conj == "3" or self. conj == "3.5" or self.conj == "4"):
					myPart = self.PtInf[0:len(self.PtInf) - myParingNo] + myThemVowel + myVerbEndings[myIndex][i] + ' (not present!)'
				else:				
					myPart = self.PtInf[0:len(self.PtInf) - myParingNo] + myThemVowel + myVerbEndings[myIndex][i]
				self.FutPass.append(myPart)
		else:
			self.FutPass = "None"
			
	def conjFutPfAct(self):
		if self.PtPerf != "none given":	
			self.FutPfAct = []
			if self.dep == False and self.semiDep == False:
				for i in range(6):
					myPart = self.PtPerf[0:len(self.PtPerf) - 1] + myVerbEndings[19][i]
					if i != 0:
						myPart = myPart + ' (not perfect subjunctive!)'
					self.FutPfAct.append(myPart)

			else:
				for i in range(3):
					myPart = self.PtPerf[0:len(self.PtPerf) - 4] + " " + myVerbEndings[20][i]
					self.FutPfAct.append(myPart)
				for i in range(3,6):
					myPart = self.PtPerf[0:len(self.PtPerf) - 6] + "i " + myVerbEndings[20][i]
					self.FutPfAct.append(myPart)
		else:
			self.FutPfAct = "No perfect given"					

	def conjFutPfPass(self):
		if self.dep == False and self.semiDep == False:
			if self.PtPpp != "none given":
				self.FutPfPass = []
				for i in range(3):
					myPart = self.PtPpp + " " + myVerbEndings[20][i]
					self.FutPfPass.append(myPart)
				for i in range(3,6):
					myPart = self.PtPpp[0:len(self.PtPpp) - 2] + "i " + myVerbEndings[20][i]
					self.FutPfPass.append(myPart)
			else:
				self.FutPfPass = "no PPP given"
		else:
			self.FutPfPass = "None"

	def conjPresActSubj(self):
		myThemVowel = ""
		if self.dep == False:
			if self.conj == "1":
				myIndex = 21
				myParingNo = 3
			if self.conj == "2":
				myIndex = 22
				myParingNo = 2
			if self.conj == "3":
				myIndex = 22
				myParingNo = 3
			if self.conj == "3.5":
				myIndex = 22
				myParingNo = 3
				myThemVowel = "i"
			if self.conj == "4":
				myIndex = 22
				myParingNo = 2
		else:
			if self.conj == "1":
				myIndex = 23
				myParingNo = 3
			if self.conj == "2":
				myIndex = 24
				myParingNo = 2
			if self.conj == "3":
				myIndex = 24
				myParingNo = 1
			if self.conj == "3.5":
				myIndex = 24
				myParingNo = 1
				myThemVowel = "i"
			if self.conj == "4":
				myIndex = 24
				myParingNo = 2
		
		
		self.PresActSubj = []
		for i in range(6):
			if i == 0 and (self.conj == "3" or self.conj == "3.5" or self.conj == "4"):
				myPart = self.PtInf[0:len(self.PtInf) - myParingNo] + myThemVowel + myVerbEndings[myIndex][i] + ' (not future!)'
			else:
				myPart = self.PtInf[0:len(self.PtInf) - myParingNo] + myThemVowel + myVerbEndings[myIndex][i]
			self.PresActSubj.append(myPart)
		
	def conjPresPassSubj(self):
		if self.dep == False:
			myThemVowel = ""
			if self.conj == "1":
				myIndex = 23
				myParingNo = 3
			if self.conj == "2":
				myIndex = 24
				myParingNo = 2
			if self.conj == "3":
				myIndex = 24
				myParingNo = 3
			if self.conj == "3.5":
				myIndex = 24
				myParingNo = 3
				myThemVowel = "i"
			if self.conj == "4":
				myIndex = 24
				myParingNo = 2
				
			self.PresPassSubj = []
			for i in range(6):
				if i == 0 and (self.conj == "3" or self.conj == "3.5" or self.conj == "4"):
					myPart = self.PtInf[0:len(self.PtInf) - myParingNo] + myThemVowel + myVerbEndings[myIndex][i] + ' (not future!)'
				else:
					myPart = self.PtInf[0:len(self.PtInf) - myParingNo] + myThemVowel + myVerbEndings[myIndex][i]
				self.PresPassSubj.append(myPart)
						
		else:
			self.PresPassSubj = "None"	

	def conjImpfActSubj(self):
		self.ImpfActSubj = []
		if self.dep == False:
			for i in range(6):
				myPart = self.PtInf + myVerbEndings[25][i]
				self.ImpfActSubj.append(myPart)
		else:
			myThemVowel = ""
			if self.conj == "1":
				myParingNo = 2
			if self.conj == "2":
				myParingNo = 2
			if self.conj == "3" or self.conj == "3.5":
				myParingNo = 1
				myThemVowel = "e"
			if self.conj == "4":
				myParingNo = 2
			
			for i in range(6):
				myPart = self.PtInf[0:len(self.PtInf) - myParingNo] + myThemVowel + myVerbEndings[26][i]
				self.ImpfActSubj.append(myPart)
				
	def conjImpfPassSubj(self):
		if self.dep == False:
			self.ImpfPassSubj = []
			for i in range(6):
				myPart = self.PtInf[0:len(self.PtInf) - 2] + myVerbEndings[26][i]
				self.ImpfPassSubj.append(myPart)		
		else:
			self.ImpfPassSubj = "None"
		
	def conjPerfActSubj(self):
		if self.PtPerf != "none given":	
			self.PerfActSubj = []
			if self.dep == False and self.semiDep == False:
				for i in range(6):
					myPart = self.PtPerf[0:len(self.PtPerf) - 1] + myVerbEndings[27][i]
					if i != 0:
						myPart = myPart + ' (not future perfect!)'
					self.PerfActSubj.append(myPart)
			else:
				for i in range(3):
					myPart = self.PtPerf[0:len(self.PtPerf) - 4] + " " + myVerbEndings[28][i]
					self.PerfActSubj.append(myPart)
				for i in range(3,6):
					myPart = self.PtPerf[0:len(self.PtPerf) - 6] + "i " + myVerbEndings[28][i]
					self.PerfActSubj.append(myPart)
		else:
			self.PerfActSubj = "No perfect given"
		
	def conjPerfPassSubj(self):
		if self.dep == False and self.semiDep == False:
			if self.PtPpp != "none given":
				self.PerfPassSubj = []
				for i in range(3):
					myPart = self.PtPpp + " " + myVerbEndings[28][i]
					self.PerfPassSubj.append(myPart)
				for i in range(3,6):
					myPart = self.PtPpp[0:len(self.PtPpp) - 2] + "i " + myVerbEndings[28][i]
					self.PerfPassSubj.append(myPart)
			else:
				self.PerfPassSubj = "no PPP given"
		else:
			self.PerfPassSubj = "None"		
	

	def conjPlpfActSubj(self):
		if self.PtPerf != "none given":	
			self.PlpfActSubj = []
			if self.dep == False and self.semiDep == False:
				for i in range(6):
					myPart = self.PtPerf[0:len(self.PtPerf)] + "sse" + myVerbEndings[25][i]
					self.PlpfActSubj.append(myPart)
			else:
				for i in range(3):
					myPart = self.PtPerf[0:len(self.PtPerf) - 4] + " esse" + myVerbEndings[25][i]
					self.PlpfActSubj.append(myPart)
				for i in range(3,6):
					myPart = self.PtPerf[0:len(self.PtPerf) - 6] + "i esse" + myVerbEndings[25][i]
					self.PlpfActSubj.append(myPart)
		else:
			self.PlpfActSubj = "No perfect given"
		
	def conjPlpfPassSubj(self):
		if self.dep == False and self.semiDep == False:
			if self.PtPpp != "none given":
				self.PlpfPassSubj = []
				for i in range(3):
					myPart = self.PtPpp + " esse" + myVerbEndings[25][i]
					self.PlpfPassSubj.append(myPart)
				for i in range(3,6):
					myPart = self.PtPpp[0:len(self.PtPpp) - 2] + "i esse" + myVerbEndings[25][i]
					self.PlpfPassSubj.append(myPart)
			else:
				self.PlpfPassSubj = "no PPP given"
		else:
			self.PlpfPassSubj = "None"

	def conjPeriFutSubj(self):
		self.PeriFutSubj = []
		if self.dep == False and self.semiDep == False:
			if self.PtPpp != "none given":
				for i in range(3):
					myPart = self.PtPpp[0:len(self.PtPpp) - 1] + "rus " + myVerbEndings[28][i]
					self.PeriFutSubj.append(myPart)
				for i in range(3,6):
					myPart = self.PtPpp[0:len(self.PtPpp) - 1] + "ri " + myVerbEndings[28][i]
					self.PeriFutSubj.append(myPart)
			else:
				self.PeriFutSubj = "no PPP given"
		else:
			for i in range(3):
				myPart = self.PtPerf[0:len(self.PtPerf) - 5] + "rus " + myVerbEndings[28][i]
				self.PeriFutSubj.append(myPart)
			for i in range(3,6):
				myPart = self.PtPerf[0:len(self.PtPerf) - 5] + "ri " + myVerbEndings[28][i]
				self.PeriFutSubj.append(myPart)		
		
def conjRegVerb(myVerb):
	myVerb.getMeaningsQ()
	myVerb.conjPresAct()
	myVerb.conjPresPass()
	myVerb.conjImpfAct()
	myVerb.conjImpfPass()
	myVerb.conjPerfAct()
	myVerb.conjPerfPass()
	myVerb.conjPlpfAct()
	myVerb.conjPlpfPass()
	myVerb.conjFutAct()
	myVerb.conjFutPass()
	myVerb.conjFutPfAct()
	myVerb.conjFutPfPass()
	myVerb.conjPresActSubj()
	myVerb.conjPresPassSubj()
	myVerb.conjImpfActSubj()
	myVerb.conjImpfPassSubj()
	myVerb.conjPerfActSubj()
	myVerb.conjPerfPassSubj()
	myVerb.conjPlpfActSubj()
	myVerb.conjPlpfPassSubj()
	myVerb.conjPeriFutSubj()

#Populate myPersonQsArr
myPersonsQsArr = [
"{1:MULTICHOICE_V:~%100%I~You (s)~He/She/It~We~You (pl)~They}",
"{1:MULTICHOICE_V:~I~%100%You (s)~He/She/It~We~You (pl)~They}",
"{1:MULTICHOICE_V:~I~You (s)~%100%He/She/It~We~You (pl)~They}",
"{1:MULTICHOICE_V:~I~You (s)~He/She/It~%100%We~You (pl)~They}",
"{1:MULTICHOICE_V:~%100%I~You (s)~He/She/It~We~%100%You (pl)~They}",
"{1:MULTICHOICE_V:~I~You (s)~He/She/It~We~You (pl)~%100%They}"
]

#Populate myTenseQsArr
myTensesQsArr = [
"{1:MULTICHOICE_V:~%100%Present~Imperfect~Perfect~Pluperfect~Future~Future Perfect}",
"{1:MULTICHOICE_V:~Present~%100%Imperfect~Perfect~Pluperfect~Future~Future Perfect}",
"{1:MULTICHOICE_V:~Present~Imperfect~%100%Perfect~Pluperfect~Future~Future Perfect}",
"{1:MULTICHOICE_V:~Present~Imperfect~Perfect~%100%Pluperfect~Future~Future Perfect}",
"{1:MULTICHOICE_V:~Present~Imperfect~Perfect~Pluperfect~%100%Future~Future Perfect}",
"{1:MULTICHOICE_V:~Present~Imperfect~Perfect~Pluperfect~Future~%100%Future Perfect}"
]

#Populate myVoiceQsArr
myVoiceQsArr = [
"{1:MULTICHOICE_V:~%100%Active~Passive~Deponent}",
"{1:MULTICHOICE_V:~Active~%100%Passive~Deponent}",
"{1:MULTICHOICE_V:~Active~Passive~%100%Deponent}"
]
#Populate myMoodQsArr
myMoodQsArr = [
"{1:MULTICHOICE_V:~%100%Indicative~Subjunctive}",
"{1:MULTICHOICE_V:~Indicative~%100%Subjunctive}"
]


	
def questionCreate(qNo, verbPart, meaningQ, tenseQ, personQ, voiceQ, moodQ):
	xmlQuestion = """<!-- question: %s  -->
<question type="cloze">
<name>
	<text>Parse_%s</text>
</name>
<questiontext format="html">
	<text><![CDATA[<p>%s</p>
					<p>Basic Meaning: %s</p>
					<table border="1" cellspacing="0" cellpadding="0">
					<tbody>
						<tr><td valign="top" width="310"><p>Tense</p></td><td valign="top" width="307"><p>Person</p></td></tr>
						<tr><td valign="top" width="310"><p>%s</p></td><td valign="top" width="307"><p>%s</p></td></tr>
						<tr><td valign="top" width="310"><p>Voice</p></td><td valign="top" width="307"><p>Mood</p></td></tr>
						<tr><td valign="top" width="310"><p>%s</p></td><td valign="top" width="307"><p>%s</p></td></tr>
					</tbody>
					</table>]]>
	</text>
</questiontext>
<generalfeedback format="html">
	<text></text>
</generalfeedback>
<penalty>0.3333333</penalty>
<hidden>0</hidden>
</question>\n""" % (qNo, verbPart, verbPart, meaningQ, tenseQ, personQ, voiceQ, moodQ)
	return xmlQuestion

def questionCategoryCreate(folderName, PtPres):
	xmlCategory = """<!-- question: 0  -->
	<question type="category">
		<category>
			<text>$course$/%s/%s</text>
		</category>
	</question>\n""" % (folderName, PtPres)
	return xmlCategory

def printToXml():
	"""	printPresAct = raw_input('Print present active? [y/n]: ').lower
		printPresPass = raw_input('Print present passive? [y/n]: ').lower
		printImpfAct = raw_input('Print imperfect active? [y/n]: ').lower
		printImpfPass = raw_input('Print imperfect passive? [y/n]: ').lower
		printPerfAct = raw_input('Print perfect active? [y/n]: ').lower
		printPerfPass = raw_input('Print perfect passive? [y/n]: ').lower
		printPlpfAct = raw_input('Print present active? [y/n]: ').lower
		printPlpfPass = raw_input('Print present passive? [y/n]: ').lower
		printFutAct = raw_input('Print future active? [y/n]: ').lower
		printFutPass = raw_input('Print future passive? [y/n]: ').lower
		printFutPerfAct = raw_input('Print present active? [y/n]: ').lower
		printFutPerfPass = raw_input('Print present passive? [y/n]: ').lower
		printPresActSubj = raw_input('Print present active? [y/n]: ').lower
		printPresPassSubj = raw_input('Print present passive? [y/n]: ').lower
		printImpfActSubj = raw_input('Print imperfect active? [y/n]: ').lower
		printImpfPassSubj = raw_input('Print imperfect passive? [y/n]: ').lower
		printPerfActSubj = raw_input('Print perfect active? [y/n]: ').lower
		printPerfPassSubj = raw_input('Print perfect passive? [y/n]: ').lower
		printPlpfActSubj = raw_input('Print present active? [y/n]: ').lower
		printPlpfPassSubj = raw_input('Print present passive? [y/n]: ').lower	
		printPeriFutSubj = raw_input('Print present active? [y/n]: '). """
	
	
	folderName = raw_input("Please input 'destination folder' in moodle: ")
    #myIntro = '<?xml version="1.0" encoding="utf-8"?><quiz><!-- question: 0  -->' + '<question type="category"><category><text>$course$/' + folderName + '</text></category></question>'
	#myOutro = '</quiz>'
	myIntro = '<?xml version="1.0" encoding="utf-8"?>\n<quiz>\n'
	myOutro = '</quiz>'				

	
	with open("outputToXml.xml", "w") as myOutputFile:
		myOutputFile.write(myIntro)
		counter = 0
		for myVerb in myVerbArray:
			# write category to file
			myOutputFile.write(questionCategoryCreate(folderName, myVerb.PtPres))
			#get pres act and dep and semi-dep questions.
			if myVerb.dep == False:
				for i in range(6):
					myOutputFile.write(questionCreate(str(1000 + counter), myVerb.PresAct[i], myVerb.myMeaningQ, myTensesQsArr[0], myPersonsQsArr[i], myVoiceQsArr[0], myMoodQsArr[0]))
					counter += 1
			elif myVerb.dep == True:
				for i in range(6):
					myOutputFile.write(questionCreate(str(1000 + counter), myVerb.PresAct[i], myVerb.myMeaningQ, myTensesQsArr[0], myPersonsQsArr[i], myVoiceQsArr[2], myMoodQsArr[0]))
					counter += 1							
			#get pres pass moodle questions
			if myVerb.dep == False and myVerb.semiDep == False:
				for i in range(6):
					myOutputFile.write(questionCreate(str(1000 + counter), myVerb.PresPass[i], myVerb.myMeaningQ, myTensesQsArr[0], myPersonsQsArr[i], myVoiceQsArr[1], myMoodQsArr[0]))
					counter += 1
			#get imperf act and dep and semi-dep questions
			if myVerb.dep == False:
				for i in range(6):
					myOutputFile.write(questionCreate(str(1000 + counter), myVerb.ImpfAct[i], myVerb.myMeaningQ, myTensesQsArr[1], myPersonsQsArr[i], myVoiceQsArr[0], myMoodQsArr[0]))
					counter += 1
			elif myVerb.dep == True:
				for i in range(6):
					myOutputFile.write(questionCreate(str(1000 + counter), myVerb.ImpfAct[i], myVerb.myMeaningQ, myTensesQsArr[1], myPersonsQsArr[i], myVoiceQsArr[2], myMoodQsArr[0]))
					counter += 1				
			#get impf pass moodle questions
			if myVerb.dep == False and myVerb.semiDep == False:
				for i in range(6):
					myOutputFile.write(questionCreate(str(1000 + counter), myVerb.ImpfPass[i], myVerb.myMeaningQ, myTensesQsArr[1], myPersonsQsArr[i], myVoiceQsArr[1], myMoodQsArr[0]))
					counter += 1
			#get pf act dep and semidep questions
			if myVerb.PtPerf != "none given":
				if myVerb.dep == False and myVerb.semiDep == False:
					for i in range(6):
						myOutputFile.write(questionCreate(str(1000 + counter), myVerb.PerfAct[i], myVerb.myMeaningQ, myTensesQsArr[2], myPersonsQsArr[i], myVoiceQsArr[0], myMoodQsArr[0]))
						counter += 1
				else:
					for i in range(6):
						myOutputFile.write(questionCreate(str(1000 + counter), myVerb.PerfAct[i], myVerb.myMeaningQ, myTensesQsArr[2], myPersonsQsArr[i], myVoiceQsArr[2], myMoodQsArr[0]))
						counter += 1				
			#get pf pass moodle questions
			if myVerb.PtPpp != "none given":
				if myVerb.dep == False and myVerb.semiDep == False:
					for i in range(6):
						myOutputFile.write(questionCreate(str(1000 + counter), myVerb.PerfPass[i], myVerb.myMeaningQ, myTensesQsArr[2], myPersonsQsArr[i], myVoiceQsArr[1], myMoodQsArr[0]))
						counter += 1
			#get plpf act moodle questions and dep and semi dep
			if myVerb.PtPerf != "none given":
				if myVerb.dep == False and myVerb.semiDep == False:
					for i in range(6):
						myOutputFile.write(questionCreate(str(1000 + counter), myVerb.PlpfAct[i], myVerb.myMeaningQ, myTensesQsArr[3], myPersonsQsArr[i], myVoiceQsArr[0], myMoodQsArr[0]))
						counter += 1
				else:
					for i in range(6):
						myOutputFile.write(questionCreate(str(1000 + counter), myVerb.PlpfAct[i], myVerb.myMeaningQ, myTensesQsArr[3], myPersonsQsArr[i], myVoiceQsArr[2], myMoodQsArr[0]))
						counter += 1				
			#get Plpf pass moodle questions
			if myVerb.PtPpp != "none given":
				if myVerb.dep == False and myVerb.semiDep == False:
					for i in range(6):
						myOutputFile.write(questionCreate(str(1000 + counter), myVerb.PlpfPass[i], myVerb.myMeaningQ, myTensesQsArr[3], myPersonsQsArr[i], myVoiceQsArr[1], myMoodQsArr[0]))
						counter += 1
			#get Fut act and dep and semi-dep questions.
			if myVerb.dep == False and myVerb.semiDep == False:
				for i in range(6):
					myOutputFile.write(questionCreate(str(1000 + counter), myVerb.FutAct[i], myVerb.myMeaningQ, myTensesQsArr[4], myPersonsQsArr[i], myVoiceQsArr[0], myMoodQsArr[0]))
					counter += 1
			else:
				for i in range(6):
					myOutputFile.write(questionCreate(str(1000 + counter), myVerb.FutAct[i], myVerb.myMeaningQ, myTensesQsArr[4], myPersonsQsArr[i], myVoiceQsArr[2], myMoodQsArr[0]))
					counter += 1							
			#get Fut pass moodle questions
			if myVerb.dep == False and myVerb.semiDep == False:
				for i in range(6):
					myOutputFile.write(questionCreate(str(1000 + counter), myVerb.FutPass[i], myVerb.myMeaningQ, myTensesQsArr[4], myPersonsQsArr[i], myVoiceQsArr[1], myMoodQsArr[0]))
					counter += 1
			#get Futpf act dep and semidep questions
			if myVerb.PtPerf != "none given":
				if myVerb.dep == False and myVerb.semiDep == False:
					for i in range(6):
						myOutputFile.write(questionCreate(str(1000 + counter), myVerb.FutPfAct[i], myVerb.myMeaningQ, myTensesQsArr[5], myPersonsQsArr[i], myVoiceQsArr[0], myMoodQsArr[0]))
						counter += 1
				else:
					for i in range(6):
						myOutputFile.write(questionCreate(str(1000 + counter), myVerb.FutPfAct[i], myVerb.myMeaningQ, myTensesQsArr[5], myPersonsQsArr[i], myVoiceQsArr[2], myMoodQsArr[0]))
						counter += 1				
			#get Futpf pass moodle questions
			if myVerb.PtPpp != "none given":
				if myVerb.dep == False and myVerb.semiDep == False:
					for i in range(6):
						myOutputFile.write(questionCreate(str(1000 + counter), myVerb.FutPfPass[i], myVerb.myMeaningQ, myTensesQsArr[5], myPersonsQsArr[i], myVoiceQsArr[1], myMoodQsArr[0]))
						counter += 1
			#get SUBJUNCTIVE pres act and dep and semi-dep questions.
			if myVerb.dep == False:
				for i in range(6):
					myOutputFile.write(questionCreate(str(1000 + counter), myVerb.PresActSubj[i], myVerb.myMeaningQ, myTensesQsArr[0], myPersonsQsArr[i], myVoiceQsArr[0], myMoodQsArr[1]))
					counter += 1
			else:
				for i in range(6):
					myOutputFile.write(questionCreate(str(1000 + counter), myVerb.PresActSubj[i], myVerb.myMeaningQ, myTensesQsArr[0], myPersonsQsArr[i], myVoiceQsArr[2], myMoodQsArr[1]))
					counter += 1							
			#get SUBJUNCTIVE pres pass moodle questions
			if myVerb.dep == False and myVerb.semiDep == False:
				for i in range(6):
					myOutputFile.write(questionCreate(str(1000 + counter), myVerb.PresPassSubj[i], myVerb.myMeaningQ, myTensesQsArr[0], myPersonsQsArr[i], myVoiceQsArr[1], myMoodQsArr[1]))
					counter += 1
			#get SUBJUNCTIVE IMPF act and dep and semi-dep questions.
			if myVerb.dep == False:
				for i in range(6):
					myOutputFile.write(questionCreate(str(1000 + counter), myVerb.ImpfActSubj[i], myVerb.myMeaningQ, myTensesQsArr[1], myPersonsQsArr[i], myVoiceQsArr[0], myMoodQsArr[1]))
					counter += 1
			else:
				for i in range(6):
					myOutputFile.write(questionCreate(str(1000 + counter), myVerb.ImpfActSubj[i], myVerb.myMeaningQ, myTensesQsArr[1], myPersonsQsArr[i], myVoiceQsArr[2], myMoodQsArr[1]))
					counter += 1				
			
			#get SUBJUNCTIVE IMPF pass moodle questions
			if myVerb.dep == False and myVerb.semiDep == False:
				for i in range(6):
					myOutputFile.write(questionCreate(str(1000 + counter), myVerb.ImpfPassSubj[i], myVerb.myMeaningQ, myTensesQsArr[1], myPersonsQsArr[i], myVoiceQsArr[1], myMoodQsArr[1]))
					counter += 1
			#get SUBJUNCTIVE pf act dep and semidep questions
			if myVerb.PtPerf != "none given":
				if myVerb.dep == False and myVerb.semiDep == False:
					for i in range(6):
						myOutputFile.write(questionCreate(str(1000 + counter), myVerb.PerfActSubj[i], myVerb.myMeaningQ, myTensesQsArr[2], myPersonsQsArr[i], myVoiceQsArr[0], myMoodQsArr[1]))
						counter += 1
				else:
					for i in range(6):
						myOutputFile.write(questionCreate(str(1000 + counter), myVerb.PerfActSubj[i], myVerb.myMeaningQ, myTensesQsArr[2], myPersonsQsArr[i], myVoiceQsArr[2], myMoodQsArr[1]))
						counter += 1				
			#get SUBJUNCTIVE pf pass moodle questions
			if myVerb.PtPpp != "none given":
				if myVerb.dep == False and myVerb.semiDep == False:
					for i in range(6):
						myOutputFile.write(questionCreate(str(1000 + counter), myVerb.PerfPassSubj[i], myVerb.myMeaningQ, myTensesQsArr[2], myPersonsQsArr[i], myVoiceQsArr[1], myMoodQsArr[1]))
						counter += 1
			#get SUBJUNCTIVE Plpf act dep and semidep questions
			if myVerb.PtPerf != "none given":
				if myVerb.dep == False and myVerb.semiDep == False:
					for i in range(6):
						myOutputFile.write(questionCreate(str(1000 + counter), myVerb.PlpfActSubj[i], myVerb.myMeaningQ, myTensesQsArr[3], myPersonsQsArr[i], myVoiceQsArr[0], myMoodQsArr[1]))
						counter += 1
				else:
					for i in range(6):
						myOutputFile.write(questionCreate(str(1000 + counter), myVerb.PlpfActSubj[i], myVerb.myMeaningQ, myTensesQsArr[3], myPersonsQsArr[i], myVoiceQsArr[2], myMoodQsArr[1]))
						counter += 1				
			#get SUBJUNCTIVE Plpf pass moodle questions
			if myVerb.PtPpp != "none given":
				if myVerb.dep == False and myVerb.semiDep == False:
					for i in range(6):
						myOutputFile.write(questionCreate(str(1000 + counter), myVerb.PlpfPassSubj[i], myVerb.myMeaningQ, myTensesQsArr[3], myPersonsQsArr[i], myVoiceQsArr[1], myMoodQsArr[1]))
						counter += 1	
			#get SUBJUNCTIVE Periphrastic Fut act dep and semidep questions
			if myVerb.PtPpp != "none given":
				if myVerb.dep == False and myVerb.semiDep == False:
					for i in range(6):
						myOutputFile.write(questionCreate(str(1000 + counter), myVerb.PeriFutSubj[i], myVerb.myMeaningQ, myTensesQsArr[4], myPersonsQsArr[i], myVoiceQsArr[0], myMoodQsArr[1]))
						counter += 1
				else:
					for i in range(6):
						myOutputFile.write(questionCreate(str(1000 + counter), myVerb.PeriFutSubj[i], myVerb.myMeaningQ, myTensesQsArr[4], myPersonsQsArr[i], myVoiceQsArr[2], myMoodQsArr[1]))
						counter += 1									
		myOutputFile.write(myOutro)	
		
		
script, myFileName = argv
myVerbArray = []
with open(myFileName, "r") as myFile:
	for myLine in myFile:
		if myLine.strip() != "":
			myNewVerb = Verb(myLine)
			myVerbArray.append(myNewVerb)
		
for myVerb in myVerbArray:
	conjRegVerb(myVerb)
#	print myVerb.printPrinPts()

printToXml()
	
