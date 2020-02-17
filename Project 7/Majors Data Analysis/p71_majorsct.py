'''
p71- Major Analysis
Analyze text docs of majors within CIS 210
Author: Lillie Rose

Help: N/A
'''
import doctest
def majors_readf(fname):
    ''' (.txt) -> list
    Return all majors in a text tile in CIS 210
                #Examples of use:
    >>> majors_readf('fname.txt')
    ['CIS', 'BADM', 'MATH', 'CIS', 'SDSC', 'CIS', 'EC']

    '''
    ffile= open(fname, 'r')
    ffile
    majorsli =(ffile.readlines())
    ffile.close()

    majorsli= majorsli[2:]
    for item in range(len(majorsli)):
        majorsli[item]= majorsli[item].replace('\n', '')
    return majorsli
    
def majors_analysis(majorsli):
    ''' (list) -> tuple
    Return the mode of the major list and count of the list
                #Examples of use:
    >>> majors_analysis(['CIS', 'BADM', 'MATH', 'CIS', 'SDSC', 'CIS', 'EC'])
    ('CIS', {'BADM': 1, 'CIS': 3, 'EC': 1, 'MATH': 1, 'SDSC': 1})
    '''
    #making the lists 'major:#'
    countdict= {}
    for item in majorsli:
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
 
    return majors_mode, majors_ct


def majors_report(majors_mode, majors_ct, majorsli):
    ''' (list, list, list) -> None
    >>>majors_report('CIS', {'BADM': 1, 'CIS': 3, 'EC': 1, 'MATH': 1, 'SDSC': 1}, ['CIS', 'BADM', 'MATH', 'CIS', 'SDSC', 'CIS', 'EC'])
    5 major's are represented in the CIS 210 this term.
    The most represented major(s): CIS
    ITEM FREQUENCY
    BADM 	 1
    CIS 	 3
    EC 	         1
    MATH 	 1
    SDSC 	 1
    '''
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
    7 major's are represented in the CIS 210 this term.
    The most represented major(s): CIS
    ITEM FREQUENCY
    ARCH 	 1
    ATCH 	 1
    BADM 	 4
    BI 	         1
    CEP 	 2
    CINE 	 1
    CIS 	 92
    EC   	 6
    EXPL 	 13
    GB 	         1
    GS 	         6
    HPHY 	 1
    JPN 	 1
    LING 	 2
    MACS 	 3
    MATH 	 7
    MDST 	 1
    PBA 	 5
    PDS 	 1
    PDSG 	 1
    PEN 	 1
    PHIL 	 1
    PHYS 	 7
    PJ   	 1
    PS  	 1
    PSY 	 1
    SDSC 	 1
    '''
    #fname = 'majors_short.txt'
    fname = 'p71_majors_cis210f18.txt'
    majorsli = majors_readf(fname) #read
    majors_mode, majors_ct = majors_analysis(majorsli) #analyze
    majors_report(majors_mode, majors_ct, majorsli) #report
    return None

main()

#doctest.testmod()
