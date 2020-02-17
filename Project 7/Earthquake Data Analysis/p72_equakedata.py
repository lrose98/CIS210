'''
'''

def majors_readf(fname):
    ''' (.txt) -> list
    Return all majors in a text tile in CIS 210
                #Examples of use:
    >> majors_readf('fname.txt)
    '''
    ffile= open(fname, 'r')
    ffile
    listmajors =(ffile.readlines())
    ffile.close()
    run= ''
    uh= ''
    equake= []
    for index in range(len(listmajors)):
        run= listmajors[index]
        run= run.split(',')
        mag= run[4:5]
        x= str(mag)
        print(type(x))
        print(x)
        uh += x

    uh=uh.replace('\']', ',')
    uh= uh.replace('[\'', '')

    magnitude= uh.split(',')
    magnitude= magnitude[1:]
    magnitude= magnitude[:-1]
    return magnitude

        
#['5.2', '5.1', '6', '5.9', '5.6', '5.7', '5', '5', '5.2', '5.1', '5.4', '5.2', '5.6']   

def majors_analysis(magnitude):
    #making the lists 'major:#'
    countdict= {}
    for item in magnitude:
        if item in countdict:
            countdict[item]= countdict[item]+1
        else:
            countdict[item]= 1
   
    itemlist= list(countdict.keys())
    itemlist.sort()

    #list of majors, majors_ct
    majors_ct= {}
    for item in itemlist:
        majors_ct[item]= countdict[item]
    
    #mode, majors_mode
    countmode= countdict.values()
    maxcount= max(countmode)
    modelist=[]
    for item in countdict:
        if countdict[item] == maxcount:
            modelist.append(item)
    majors_mode= ""
    for item in range(len(modelist)):
        majors_mode= majors_mode + modelist[item]
    print(type(majors_ct))
    return majors_mode, majors_ct

def majors_report(majors_mode, majors_ct, majorsli):
    num_major= len(majors_ct)
    print("{} {} are represented in the {} this term.".format(num_major, 'major\'s', 'CIS 210'))
    print("The most represented major(s): {}".format(majors_mode))
    print("ITEM", "FREQUENCY")

    majors_li= list(majors_ct.keys())
    
    for item in majors_li:
        print(item, "\t", majors_ct[item])

    return None

def main():
 '''()-> None
 Calls: majors_readf, majors_analysis, majors_report
 Top level function for analysis of CIS 210 majors data.
 Returns None.
 > majors_main()
 '''
 #fname = 'majors_short.txt'
 fname = 'p71_majors_cis210f18.txt'

 majorsli = majors_readf(fname) #read
 majors_mode, majors_ct = majors_analysis(majorsli) #analyze
 majors_report(majors_mode, majors_ct, majorsli) #report
 return None

def dictton(X):
    
