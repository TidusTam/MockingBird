def preprocess_transcript_aishell3(dict_info, dict_transcript):
    for v in dict_transcript:
        if not v:
            continue
        v = v.strip().replace("\n","").replace("\t"," ").split(" ")
        transList = []
        for i in range(2, len(v), 2):
            transList.append(v[i])
        dict_info[v[0]] = " ".join(transList)


def preprocess_transcript_magicdata(dict_info, dict_transcript):
    for v in dict_transcript:
        if not v:
            continue
        v = v.strip().replace("\n","").replace("\t"," ").split(" ")
        dict_info[v[0]] = " ".join(v[2:])
       
def preprocess_transcript_bznsyp(dict_info, dict_transcript):
    transList = []
    for t in dict_transcript:
        transList.append(t)
    for i in range(0, len(transList), 2):
        if not transList[i]:
            continue
        key = transList[i].split("\t")[0]
        transcript = transList[i+1].strip().replace("\n","").replace("\t"," ")
        dict_info[key] = transcript
