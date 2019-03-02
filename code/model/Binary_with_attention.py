# -*- coding:utf-8 -*-
import os
os.environ['KERAS_BACKEND']='tensorflow'
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers.core import Dense
from keras.layers.core import Dropout
from keras.layers.core import Activation
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM
from keras.models import load_model
from keras.layers import merge
from keras.layers.core import *
from keras.models import *
import numpy as np

# Attention模块
def nonlinear_attention_tanh(inputs,TIME_STEPS):
    # 换维层
    a = Permute((2, 1))(inputs)	

    # 三个全连接层，进行非线性映射
    a = Dense(TIME_STEPS, activation='softmax')(a)
    a = Dense(30, activation='tanh')(a)
    a = Dense(TIME_STEPS, activation='softmax')(a)

    # 换维层
    a_probs = Permute((2, 1), name='attention_vec')(a)

    # 融合层
    output_attention_mul = merge([inputs, a_probs], name='attention_mul', mode='mul')
    return output_attention_mul



def model_attention_applied_after_lstm(shape, max_features):
    inputs = Input(shape=(shape,))

    # Embedding层，生成词向量
    a = Embedding(max_features, 128, input_length=shape)(inputs)

    # LSTM层
    lstm_out = LSTM(128, return_sequences=True)(a)

    # Attention层，调用已经定义好的Attention模块
    attention_mul = nonlinear_attention_tanh(lstm_out, 75)

    # 平铺层，折叠成一维向
    attention_mul = Flatten()(attention_mul)    

    # Dropout层，防止过拟合
    a = Dropout(0.5)(attention_mul)

    # 全连接与激活层
    a = Dense(1)(a)
    outputs = Activation('sigmoid')(a)
    model = Model(input=[inputs], output=outputs)

    return model




def train(max_features, x_train, y_train, x_test, y_test, batch_size, epochs, modelPath):
    # 将数据统一成75维
    x_train = sequence.pad_sequences(x_train, maxlen=75)
    x_test = sequence.pad_sequences(x_test, maxlen=75)

    # 定义模型结构、损失函数、优化器
    model = model_attention_applied_after_lstm(75, max_features)
    model.summary()
    model.compile(loss='binary_crossentropy',optimizer='rmsprop')
    model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_data=(x_test, y_test))

    model.save(modelPath)



def predict(X_test, batch_size, modelPath, resultPath):
    X_test = sequence.pad_sequences(X_test, maxlen=75)
    # 加载模型，进行判别
    my_model = load_model(modelPath)
    y_test = my_model.predict(X_test, batch_size=batch_size).tolist()

    file = open(resultPath, 'w+')
    for index in y_test:
        y = float(str(index).strip('\n').strip('\r').strip(' ').strip('[').strip(']'))
        file.write(str(y) + '\n')





