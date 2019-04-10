#-*- coding : utf-8 -*-

input_file1 = 'raw2id_260k.txt'
input_file2 = 'raw2id_200k_2nd.txt'
input_file3 = 'raw2id_200k_3rd.txt'
input_file4 = 'raw2id_200k_4th.txt'
input_file5 = 'raw2id_200k_5th.txt'
input_file6 = 'raw2id_200k_6th.txt'
input_file7 = 'raw2id_200k_7th.txt'

test_file ='raw_test2id.txt'
valid_file = 'raw_valid2id.txt'
dict = {}
NUM_ENTITY = 0
train_num = 0
valid_num = 0
test_num = 0
#save =open('entity2id.txt','a+')
save_train = open('train','a+')
save_test = open('test','a+')
save_valid = open('valid','a+')

def train_embed(input_file1,train_num):
    with open(input_file1,'r',encoding='utf-8') as sf:
        tt = sf.readlines()
        train_num += tt.__len__()
        for ele_tt in tt:
            print(str(dict[ele_tt.split()[0]])+'\t'+str(ele_tt.split()[2])+'\t'+str(dict[ele_tt.split()[1]]),file=save_train)
    return train_num

def valid_embed(valid_file,valid_num):
    with open(valid_file,'r',encoding='utf-8') as vf:
        vvf = vf.readlines()
        valid_num += vvf.__len__()
        for ele_tt in vvf:
            print(str(dict[ele_tt.split()[0]])+'\t'+str(ele_tt.split()[2])+'\t'+str(dict[ele_tt.split()[1]]),file=save_valid)
    return valid_num


def test_embed(test_file,test_num):
    with open(test_file,'r',encoding='utf-8') as tf:
        tff = tf.readlines()
        test_num += tff.__len__()
        for ele_tt in tff:
            print(str(dict[ele_tt.split()[0]])+'\t'+str(ele_tt.split()[2])+'\t'+str(dict[ele_tt.split()[1]]),file=save_test)
    return test_num


def entity_embed(input_file,NUM_ENTITY):
    print('dict',dict.__len__())
    with open(input_file,'r',encoding='utf-8') as f:
        sk = f.readlines()
        for s in sk:
            kk,k1 = s.split()[0],s.split()[1]
            if(kk not in dict.keys()):
                dict[kk] = NUM_ENTITY
                NUM_ENTITY +=1
            if(k1 not in dict.keys()):
                dict[k1] = NUM_ENTITY
                NUM_ENTITY +=1
    return NUM_ENTITY

NUM_ENTITY = entity_embed(input_file1,NUM_ENTITY)
NUM_ENTITY = entity_embed(input_file2,NUM_ENTITY)
NUM_ENTITY = entity_embed(input_file3,NUM_ENTITY)
NUM_ENTITY = entity_embed(input_file4,NUM_ENTITY)
NUM_ENTITY = entity_embed(input_file5,NUM_ENTITY)
NUM_ENTITY = entity_embed(input_file6,NUM_ENTITY)
NUM_ENTITY = entity_embed(input_file7,NUM_ENTITY)
#for ele in dict:
#    print(ele, dict[ele], file=save)
#save.close()

train_num = train_embed(input_file1,train_num)
train_num = train_embed(input_file2,train_num)
train_num = train_embed(input_file3,train_num)
train_num = train_embed(input_file7,train_num)
valid_num = valid_embed(valid_file,valid_num)
test_num = test_embed(test_file,test_num)

save_train.close()
save_test.close()
save_valid.close()
print('train_num',train_num)
print('valid_num',valid_num)
print('test_num',test_num)