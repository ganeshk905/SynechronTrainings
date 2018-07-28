F1=open(r'C:\training\log\out4.txt')
F2=open(r'C:\training\log\out5.txt','w')
F3=open(r'C:\training\log\out6.csv','w')
print('IP','Date','PICS', 'Website', sep='\t\t', file=F2)
print('IP','Date','PICS', 'Website', sep='\t\t', file=F3)
for line in F1:
    if len(line)>0 and line[0].isdigit() and len(line.split()[0])>4:
        sp=line.split()
        ip=sp[0]
        print(ip)
        dt=sp[3]
        dt=dt.split(':')
        dt=dt[0]
        dt=dt.lstrip('[')
        print(dt)
        pc=sp[6]
        if '/pics' in pc:
            pc=pc.lstrip('/pics/')
        else:
            pc='No Image'
        print(pc)
        wb=sp[10]
        wb=wb.split('/')
        wb=wb[2]
        print(ip, dt, pc, wb, sep='\t', file=F2)
        print(ip, dt, pc, wb, sep='\t', file=F3)
F2.close()
F3.close()