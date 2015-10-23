import os
import sys

#always referrence this page : http://www.ahnlab.com/kr/site/securityinfo/secunews/secuNewsView.do?menu_dist=2&seq=22227
#http://nulltop.tistory.com/m/post/16

"""
input data
"""
dumpname = "memdump.mem"
profile = "Win7SP1x86"#"Win7SP1x64"
cmd = []

print "debug : "+sys.argv[0]

if dumpname == "":
    print "[!] somethings wrong, check input data."
    exit(1)

if profile == "" or len(sys.argv) == 1:
    print "[?] usage : python volascript.py <cmd>"
    print "[?] out directory : ./out"
    print "[+] Default : running imageinfo"

    script = "./old_volatility_2.4_x64 -f %s "%(dumpname)

    cmd.append("imageinfo")

elif sys.argv[1] != 'run':
    script = "./old_volatility_2.4_x64 -f %s --profile=%s "%(dumpname, profile)

    cmd.append(sys.argv[1])

else:
    script = "./old_volatility_2.4_x64 -f %s --profile=%s "%(dumpname, profile)

    #process
    cmd.append('pstree')
    cmd.append('psscan') # for finding process create time / end time
    #cmd.append('pslist')
    cmd.append('psxview') # for finding hide process
    cmd.append('cmdline')
    cmd.append('cmdscan')

    #dll and thread
    cmd.append('dlllist')
    #cmd.append('malfind')
    
    #network
    cmd.append('netscan')
    cmd.append('sockets')
    
    #timeline
    cmd.append('timeliner')
    #cmd.append('')

    #dump : procexedump 
    
for i in cmd:
    run = script + "--output-file=./out/%s.log %s"%(i, i)
    #debug
    print "[+] running script [%d/%d]"%(cmd.index(i)+1, len(cmd))
    print "%s"%run
    os.system(run)


