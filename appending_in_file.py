appendMe='Sample text to append\nExample'

saveFile=open('exampleAppendFile.txt','a')

saveFile.write(appendMe)

saveFile.close()