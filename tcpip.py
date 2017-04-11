#!/usr/bin/python
# Let's parse tcpip.snap -- SEA and Virtual adapter.

import fileinput
import sys

def dotdotdot( parameter ):
    if parameter[5] == '\n':
        return
    else:
        return parameter[9:25]

def process_line( line ):
#    print(line.find('',0,len(line)))
    if line.find('-------------------- ',0,len(line)) != -1:
        print(line),

    # Basic info including title
    if line.find('ETHERNET ',0,len(line)) != -1:
        print(line),
    elif line.find('Transmit Stat',0,len(line)) != -1:
        print(line),
    elif line.find('^Packets',0,len(line)) != -1:
        print(line),
    elif line.find('Device Type',0,len(line)) != -1:
        print(line),
    elif line.find('Bytes:',0,len(line)) != -1:
        print(line),
    elif line.find('Transmit Errors:',0,len(line)) != -1:
        print(line),
    elif line.find('Packets Dropped:',0,len(line)) != -1:
        print(line),
    elif line.find('No Carrirer:',0,len(line)) != -1:
        print(line),
    elif line.find('DMA Under',0,len(line)) != -1:
        print(line),
    elif line.find('Lost CTS ',0,len(line)) != -1:
        print(line),
    elif line.find('Max Collision',0,len(line)) != -1:
        print(line),
        print('--------------------------------------------------------------')

# SEA statistics

    elif line.find('   State: ',0,len(line)) != -1:
        print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
        print(line),
    elif line.find('Bridge Mode: ',0,len(line)) != -1:
        print(line),
    elif line.find('High Availab',0,len(line)) != -1:
        print(line),
    elif line.find('Priority: ',3,len(line)) != -1:
        print(line),
        print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')


    else:
        return
#    else:
#        return
#    return


fd = open("tmp_netstat_v.txt", "w+")
header = False
# will be smarter later
#maxlen = {'CPU': 3, 'TID': 9}

try:
    tcpipsnap = fileinput.input(sys.argv[1:])

#    if header:
        # just print out lines above ^ID
#        for line in trcinput:
#            if len(line) < 2 or line[:2] != 'ID':
#                print(line),
#            else:
                # print re-aligned ID line and go to the next 'for' loop
#                print(line[:23] + ' ' + line[23:42] + ' ' + line[42:-1])
#                break

    # line_buf: string buffer for the line(s) being processed
    line_buf = ''

    netstat_v=0

    # use 'trcinput' as set above, cannot call input() again
    for line in tcpipsnap:

        if line[0] == '.' and line[5] == ' ':
            if netstat_v == 1:
                fd.close()
                break
            else:
                if line[9:19] == 'netstat -v':
                    print(line),
                    fd.write(line)
                    #line_buf = line_buf + line[9:19]
                    #rint(line_buf)
                    netstat_v = 1
                else:
                    # this is a new line
                    if netstat_v == 0:
                        continue
                    else:
                        print(line),
                        fd.write(line)
        else:
            if netstat_v == 1:
                #print(line),
                process_line( line )
                fd.write(line)
            else:
                continue
            # print out previous line in line_buf first
            #print(line_buf)


except IOError:
    try:
        sys.stdout.close()
    except IOError:
        pass
    try:
        sys.stderr.close()
    except IOError:
        pass
except KeyboardInterrupt:
    sys.stdout.flush()
    pass
