#!/usr/bin/env python

import unittest

class TestTF(unittest.TestCase):
    
    def n_testTF1(self):
        # first time to run tensorflow
        import tensorflow as tf
        import numpy as np

        # create data
        x_data = np.random.rand(100).astype(np.float32)
        y_data = x_data*x_data*0.1 + 0.3

        ### create tensorflow structure start
        Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
        biases = tf.Variable(tf.zeros([1]))

        y = Weights*x_data*x_data + biases

        loss = tf.reduce_mean(tf.square(y-y_data))
        optimizer = tf.train.GradientDescentOptimizer(0.5)
        train = optimizer.minimize(loss)

        init = tf.initialize_all_variables()
        ### create tensorflow structure end

        sess = tf.Session()
        sess.run(init)

        for step in range(201):
            sess.run(train)
            if step % 20 == 0:
                print(step, sess.run(Weights), sess.run(biases))
    
    def n_testTF2(self):
        import tensorflow as tf
        import numpy as np

        matrix1 = tf.constant([[3,3]])
        matrix2 = tf.constant([
            [2],
            [2]
        ])

        product = tf.matmul(matrix1, matrix2)

        # method 1
        sess = tf.Session()
        result = sess.run(product)
        print("result1:{}".format(result))

        # method 2
        with tf.Session() as sess2:
            result2 = sess2.run(product)
            print("result2:{}".format(result2))
    
    def testTF3(self):
        import tensorflow as tf

        state = tf.Variable(0, name='counter')


if __name__ == '__main__':
    unittest.main()