#from tensorflow.keras.datasets.fashion_mnist import load_data
#from tensorflow.python import tf2
from keras.datasets.fashion_mnist import load_data

(x_train,y_train),(x_test,y_test)=load_data()
print(x_train.shape,y_train.shape)
print(x_test.shape,y_test.shape)

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(777)
class_names=['T-shirt/top','Ttouser','Pullover','Dress','Coat','Sendal',
             'Shirt','Sneaker','Bag','Ankle boot']
sample_size=9
random_idx=np.random.randint(60000,size=sample_size)
print(random_idx)
plt.figure(figsize=(5,5))
for i,idx in enumerate(random_idx):
    plt.subplot(3,3,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(x_train[i],cmap='gray')
    plt.xlabel(class_names[y_train[i]])
plt.show()
x_train=x_train/255
t_test=x_test/255
#from tensorflow.keras.utils import to_categorical
from keras.utils import to_categorical
y_train=to_categorical(y_train)
y_test=to_categorical(y_test)
#from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
x_train,x_val,y_train,y_val=train_test_split(x_train,y_train,test_size=0.3,
                                             random_state=777)
from keras.models import Sequential
from keras.layers import Dense,Flatten
fist_model=Sequential()
fist_model.add(Flatten(input_shape=(28,28)))
fist_model.add(Dense(64,activation='relu'))
fist_model.add(Dense(32,activation='relu'))
fist_model.add(Dense(10,activation='softmax'))

fist_model.compile(optimizer='adam',
                   loss='categorical_crossentropy',
                   metrics=['acc'])
fist_history=fist_model.fit(x_train,y_train,epochs=30,
                            batch_size=128,validation_data=(x_val,y_val))
print(y_test[0])
result=fist_model.predict(x_test)
print(result[0])


