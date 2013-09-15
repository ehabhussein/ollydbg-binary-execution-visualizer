x = open("crack_vis.txt","r")
y = open("crack_vis_parsed.txt","w")
for i in x.xreadlines():
	if "eip" not in i:
             pass
     	else:
             print>>y, i.strip().replace("eip: ","").split()[0]
y.close()
