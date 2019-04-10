save = open('test2id_simple.txt','a+')
with open('raw_test2id.txt','a+',encoding='utf-8') as f:
    s = f.readlines()
    num = 0
    for ele in s:
        print(ele)
        num+=1
        if(num==7777):
            break;
save.close()