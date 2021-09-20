word = "good is boy The"
word2 = "put some and a jar into Take glass soil it "
word3 = 'shake water settle up. Add Then it let and '

the = word[11:15]
boy = word[7:11]
nw = word[4:8]
good = word[0:5]
nw2 = (word2[24:29] + word2[4:9] + word2[35:40] + word2[9:13] + word2[0:4] + word2[40:43] + word2[19:24] + word2[13:15] + word2[29:35] + word2[15:18])
nw3 = (word3[23:27] +word3[6:12] + word3[39:43] + word3[0:6] + word3[32:35] + word3[19:23] + word3[27:32] + word3[35:39] + word3[32:35] + word3[12:19])

print(the + boy + nw + good)
print(nw2)
print(nw3)
