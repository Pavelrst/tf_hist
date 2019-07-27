import tensorflow as tf
from tensorflow.python.tools.inspect_checkpoint import print_tensors_in_checkpoint_file
import numpy
import os,sys
import re
import pickle

sys.stdout = open('networkWeights.txt', 'w')

numpy.set_printoptions(threshold=numpy.nan)
with tf.Session() as sess:
  new_saver = tf.train.import_meta_graph('/tmp/runs/cifar10_resnet32/model.ckpt-23002.meta')
  new_saver.restore(sess, tf.train.latest_checkpoint('/tmp/runs/cifar10_resnet32/'))
  print_tensors_in_checkpoint_file(file_name='/tmp/runs/cifar10_resnet32/model.ckpt-23002', tensor_name='', all_tensors=True)

with open("networkWeights.txt" , 'r') as handler:
 text = handler.read()
 listNumbers = re.findall(r'[-+]?(?:(?:\d*\.\d+)|(?:\d+\.?))(?:[Ee][+-]?\d+)' , text)
 listNumbers = [float(x)  for x in listNumbers]
 with open('weights.pkl' , 'wb') as f:
  pickle.dump(listNumbers , f)

