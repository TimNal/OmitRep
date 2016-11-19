'''
Created on 8.11.2016

@author: Timo
'''
'''
from fi.genealogia.taapeli.jsonutils.CreateGrampsObject import buildTag, \
    buildRepository, buildSource
'''

import sys

from fi.genealogia.taapeli.json.CreateGrampsObject import CreateGrampsObject



def give_idno(pfx, idno):
        idno =idno + 1
        return(pfx + str(idno))
    
def main(argv = ["aaa", "C:/Temp/"]):
    if argv is None:
        argv = sys.argv   
        
    if len(argv) != 2:
        print("Wrong number of arguments")
        return 8

    tag = None
    repository = None
    source = None
    
    repository_idno = 500000
    source_idno     = 500000

    fdir = argv[1] 
    print("File directory for program " + argv[0] + " is " + fdir)
    
    cgo = CreateGrampsObject()
      
    try:
        with open(fdir + "JsonIn.json", "w") as j_out:

            with open(fdir + "Tags.txt", "r") as t_in:
                for line in t_in:
                    ttext =  line.strip('\n ')
#                    print(ttext)
                    tag = cgo.buildTag(ttext)
                    print(tag.to_struct(), file=j_out)
                    break

            with open(fdir + "Repositories.txt", "r") as r_in:
                for line in r_in:
                    rtext =  line.strip('\n ')
#                    print(rtext)
                    repository_idno = repository_idno + 1
                    ridno = 'R' +  str(repository_idno)
                    repository = cgo.buildRepository(ridno, rtext, tag, 4)
                    print(repository.to_struct(), file=j_out)
                    break

            with open(fdir + "Sources.txt", "r") as s_in:
                for line in s_in:
                    stext =  line.strip('\n ')
#                    print(stext)
                    source_idno = source_idno + 1
                    sidno = 'S' + str(source_idno)
                    source = cgo.buildSource(sidno, stext, tag, repository)
                    print(source.to_struct(), file=j_out)
#                   break

    except  IOError:
        print(IOError.winerror)
        print("IOError in j_out handling")
        return 8    
    
if __name__ == '__main__':
    sys.exit(main())
             