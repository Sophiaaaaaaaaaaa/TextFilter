with open('p.project','r') as reader, open('p.txt', 'w') as writer:
    for index, line in enumerate(reader):
        if index % 12 == 9:
            line=line.strip('\n')
            writer.write(line)
            writer.write('\t')
        if index % 12 == 10:
            line=line.strip('\n')
            writer.write(line)
            writer.write('\t')
        if index % 12 == 11:
            writer.write(line)


