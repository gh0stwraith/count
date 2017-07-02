'''
Calculate number of beds needed  

'''
global nbr  # number beds run
global pt  # production time
global dt  # down time hours /60 for mintues
global spb # strands per bed
global spm # strands per min
global bps # beds per shift
global pts # production time per shift default 480 minutes
global pta  # production time for assembler
global aps # average production per shift
global prod # Production Percent starts at 65% goes to 100%

pts = 480
nbr = eval(input("How many beds have you run? >> "))
dt = eval(input("downtime (hours) ? >> "))
pta = (pts - (dt*60))/60
spb = 33
spm = 17
bps = (spm*pts)/spb
aps	= "{0:.0f}%".format(nbr/bps * 100)
	
prod = (65,70,75,80,85,90,95,100)
print ("beds per shift ",str(round(bps, 2))," average was ",aps," downtime is ",dt," with ",pta," production time")
for x in prod:
	bnt = (x/100)*bps
	x = "{0:.0f}%".format(x)
	print (x," = ",str(round(bnt, 2)))

wait = input("PRESS ENTER TO CONTINUE.")

