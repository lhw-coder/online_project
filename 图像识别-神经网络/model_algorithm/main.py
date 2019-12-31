import numpy
import pandas
import tensorflow as tf
import os
from tensorflow.examples.tutorials.mnist import input_data
import scipy.misc
from PIL import Image


minist = input_data.read_data_sets('datasets/', one_hot=True)
# print(minist.train.images.shape)  # (55000, 784) 55000张图片，784维的向量
# print(minist.train.labels.shape)  # (55000, 10)
# print(minist.train.images[0,:])     # 查看第一张图片
# print(minist.train.labels[0,:])     # 查看第一张图片的标签

# dir_data_pic = 'picture/'
# if os.path.exists(dir_data_pic) is False:
#     os.makedirs(dir_data_pic)

# for i in range(5):
#     image_array = minist.train.images[i,:]
#     image_array = image_array.reshape(28,28)
#     image_file = dir_data_pic + 'mnist_train_%d.jpg' % i
#     im = Image.fromarray(image_array)
#     im.save(image_file)
#     scipy.misc(image_array, cmin=0.0, cmax=1.0).save(image_file)
x = tf.placeholder(tf.float32, [None,784])
w = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
y_ = tf.placeholder(tf.float32,[None,10])

# y = softmax(x*w+b)
y = tf.nn.softmax(tf.matmul(x, w)+b)

cross_func = tf.reduce_sum(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y_,logits=y))

train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_func)

with tf.Session() as sess:
    tf.global_variables_initializer().run()
    for _ in range(1000):
        batch_xs,batch_ys = minist.train.next_batch(100)
        sess.run(train_step, feed_dict = {x:batch_xs,y_:batch_ys})

    curr_pre = tf.equal(tf.arg_max(y,1),tf.arg_max(y_,1))
    acc = tf.reduce_mean(tf.cast(curr_pre, tf.float32))
    print(sess.run(acc,feed_dict={x:minist.test.images,y_:minist.test.labels}))







