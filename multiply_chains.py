# Max range of unicode is 1114111
# skip first 48 - special chars

import glob


def gen_unicode():
   # generator fction to prodce a chain of unicodes
   for i in range(48,1114112):
      yield unichr(i)
      
def rewrite(oldpath,newpath,newletter):
   # rewrite pdb files with new chain letter
   with open(oldpath) as f:
      with open(newpath,'w') as g:
         for line in f:
            l=list(line)
            l[21]=newletter
            g.write(''.join(l))   

uni=gen_unicode()
oldletters=['a','b','c','d','e','A','B','C','D','E']
folder='domains/' #where are the single domain prototypes
outfolder='newdomains/'  # where to put new domains
ncopies=3 # how many proteins


for copy in xrange(ncopies):
   for letter in oldletters:
      newletter=uni.next()
      
      # Double lowercase to distinguish them from uppercase
      if letter.islower():
         strletter=letter+letter
      else:
         strletter=letter
      
      # load the prepared domain file
      domfile=glob.glob(folder+'EC*_'+strletter+'*.pdb')[0]
      
      # save with a meaningful name
      newname=domfile.replace(folder,outfolder)
      newname=newname.replace("_"+strletter,"_"+newletter+"_")
      
      rewrite(domfile,newname,newletter)

   