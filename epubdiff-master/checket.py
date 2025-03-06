import epubdiff

#init
checker = epubdiff.EpubDiff("/storage/emulated/0/Download/1.epub"," /storage/emulated/0/Download/2.epub ")

#check files
checker.check()

#show differences
print(checker.difflog)