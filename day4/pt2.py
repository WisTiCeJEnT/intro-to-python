import num_file_reader
for i in range(200):
    fn = f'./pt1_data/IT_ARU_{i}.txt'
    data = num_file_reader.read_num_file_list(fn)
    data = sorted(data)
    # print(data)
    fnw = f'./pt1_data_sorted/IT_ARU_{i}.txt'
    fw = open(fnw, 'w')
    for j in data:
        fw.write(str(j) + '\n')
    fw.close()
