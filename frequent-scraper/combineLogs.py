# debiele code
output = open('out.txt', 'w')
index = 0;
while 1:
    try:
        f = open(f'log{index}.txt', 'r')
        output.write(f.read())
        f.close()
        index += 1
        print(index)
    except Exception:
        pass

output.close()