import num_file_reader as nfr
fw = open('result.txt', 'w')
print('    Filename      |  Min  |  Max  |  Avr')
fw.write('    Filename      |  Min  |  Max  |  Avr\n')
for i in range(200):
    # print(f'./pt1_data/IT_ARU_{i}.txt')
    filename = f'./pt1_data/IT_ARU_{i}.txt'
    data = nfr.read_num_file(filename)
    filename = f'IT_ARU_{i}.txt'
    print(f'{filename:17} | {data[0]:7} | {data[1]:7} | {data[2]:7.2f}')
    fw.write(f'{filename:17} | {data[0]:7} | {data[1]:7} | {data[2]:7.2f}\n')
fw.close()
