t_list = []
h_list = []
with open("predictions.txt", "r") as source:
    for line in source:
        line = line.split("\t")
        string = line[0]
        if string.startswith("T-"):
            t_list.append(line)
        elif string.startswith("H-"):
            h_list.append(line)
    line = 0
    false = 0
    while line < len(t_list):
        target = t_list[line][1]
        hypothesis = h_list[line][2]
        if target != hypothesis:
            false += 1
        line += 1
with open("WER_result.txt","w") as out_file:
    print("WER:", false, file=out_file)
