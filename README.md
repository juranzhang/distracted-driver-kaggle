# distracted-driver-kaggle

## AlexNet
#### Print model architecture
`python /home/juran/caffe/python/draw_net.py /home/juran/distracteddriver/caffe_models/caffe_model_1/caffenet_train_val_1.prototxt /home/juran/distracteddriver/caffe_models/caffe_model_1/caffe_model_1.png`

#### Train
`/home/juran/caffe/build/tools/caffe train --solver /home/juran/distracteddriver/caffe_models/caffe_model_1/solver_1.prototxt 2>&1 | tee /home/juran/distracteddriver/caffe_models/caffe_model_1/model_1_train.log`

#### Plot learning curve
`python /home/juran/distracteddriver/code/plot_learning_curve.py /home/juran/distracteddriver/caffe_models/caffe_model_1/model_1_train.log  /home/juran/distracteddriver/caffe_models/caffe_model_1/caffe_model_1_learning_curve.png`


## GoogLeNet
`python /home/juran/caffe/python/draw_net.py /home/juran/distracteddriver/caffe_models/caffe_model_2/caffenet_train_val_2.prototxt /home/juran/distracteddriver/caffe_models/caffe_model_2/caffe_model_2.png`

`/home/juran/caffe/build/tools/caffe train --solver /home/juran/distracteddriver/caffe_models/caffe_model_2/solver_2.prototxt 2>&1 | tee /home/juran/distracteddriver/caffe_models/caffe_model_2/model_2_train.log`


## VGG-16
`python /home/juran/caffe/python/draw_net.py /home/juran/distracteddriver/caffe_models/caffe_model_3/caffenet_train_val_3.prototxt /home/juran/distracteddriver/caffe_models/caffe_model_3/caffe_model_3.png`

`/home/juran/caffe/build/tools/caffe train --solver /home/juran/distracteddriver/caffe_models/caffe_model_3/solver_3.prototxt 2>&1 | tee /home/juran/distracteddriver/caffe_models/caffe_model_3/model_3_train.log`
