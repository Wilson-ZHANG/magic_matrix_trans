import os
import random
input_file = 'raw_cmekg.txt'
with open(input_file,'r',encoding='utf-8') as f:
    all_lines=f.readlines()
    test=random.sample(all_lines,6666)
    all_lines=set(all_lines)
    test=set(test)
    train=all_lines-test
    valid = random.sample(train,6666)
    train = set(train)
    valid = set(valid)
    train = train-valid
    with open( 'cmekg_raw_test.txt' ,'a') as test_txt:
        for test_name in test:
            test_txt.write(test_name)
    with open('cmekg_raw_valid.txt', 'a') as valid_txt:
        for valid_name in valid:
            valid_txt.write(valid_name)
    with open('cmekg_raw_train.txt', 'a') as train_txt:
        for train_name in train:
            train_txt.write(train_name)