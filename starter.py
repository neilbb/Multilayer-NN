import tensorflow as tf

#first thing is you construct graph

x1 = tf.constant(5)
x2 = tf.constant(6)


#

#result = x1 * x2

#these are just values but usually its matrices
result = tf.multiply(x1,x2) # define model

print (result)
'''
=>Tensor("Mul:0", shape=(), dtype=int32)
which is an abstract tensor 
- to actually see result you run it in a session

'''
'''
sess = tf.Session()
# gives you sess variable

print (sess.run(result))

sess.close()
'''
#Another way to write it
# which will automatically close
with tf.Session() as sess:
	print(sess.run(result))

