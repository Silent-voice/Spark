# -*- coding: utf-8 -*-

def create_new_file_name(prefix):
    import random
    import os
    while True:
        num = random.randint(0,10000)
        file_path = prefix + str(num) + '.txt'
        if os.path.exists(file_path):
            continue
        else:
            break

    return file_path

def predict(domain_list, X_test, batch_size, modelPath):
    import os
    os.environ['KERAS_BACKEND']='tensorflow'
    import keras

    X_test = keras.preprocessing.sequence.pad_sequences(X_test, maxlen=75)
    # 加载模型，进行判别

    my_model = keras.models.load_model(modelPath)
    y_test = my_model.predict(X_test, batch_size=batch_size).tolist()

    res = []
    for i in range(len(y_test)):
        y = float(str(y_test[i]).strip('\n').strip('\r').strip(' ').strip('[').strip(']'))
        res.append((domain_list[i], y))
    return res

def domain_predict(x_list):
    import numpy as np
    domain_list = []
    vec_list = []
    for x in x_list:
        domain_list.append(x[0])
        vec_list.append(x[1])


    x_data_sum = np.array(vec_list)
    res_list = predict(domain_list, x_data_sum, 128, '/data/spark/modelFiles/dns/dga_model.h5')

    f = open(create_new_file_name('/data/spark/tempFiles/dns/time/dga_res'), 'w+')
    for i in res_list:
        f.write(str(i) + '\n')
    f.close()

    return res_list

