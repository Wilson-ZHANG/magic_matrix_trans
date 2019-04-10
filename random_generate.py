import os
import random
#input_file = 'raw2id_260k.txt'
input_file1 = 'raw2id_260k.txt'
input_file2 = 'raw2id_200k_2nd.txt'
input_file3 = 'raw2id_200k_3rd.txt'
input_file4 = 'raw2id_200k_4th.txt'
input_file5 = 'raw2id_200k_5th.txt'
input_file6 = 'raw2id_200k_6th.txt'
with open(input_file4,'r',encoding='utf-8') as f:
    all_lines=f.readlines()
    test=random.sample(all_lines,3000)
    all_lines=set(all_lines)
    test=set(test)
    train=all_lines-test
    with open( 'raw_test2id.txt' ,'a') as valid_txt:
        for valid_name in test:
            valid_txt.write(valid_name)
    with open('raw_valid2id.txt', 'a') as train_txt:
        for train_name in train:
            train_txt.write(train_name)