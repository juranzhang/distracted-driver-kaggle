# distracted-driver-kaggle

## AlexNet
`python /home/juran/caffe/python/draw_net.py /home/juran/distracteddriver/caffe_models/caffe_model_1/caffenet_train_val_1.prototxt /home/juran/distracteddriver/caffe_models/caffe_model_1/caffe_model_1.png`

`/home/juran/caffe/build/tools/caffe train --solver /home/juran/distracteddriver/caffe_models/caffe_model_1/solver_1.prototxt 2>&1 | tee /home/juran/distracteddriver/caffe_models/caffe_model_1/model_1_train.log`


## GoogLeNet
`python /home/juran/caffe/python/draw_net.py /home/juran/distracteddriver/caffe_models/caffe_model_2/caffenet_train_val_2.prototxt /home/juran/distracteddriver/caffe_models/caffe_model_2/caffe_model_2.png`

`/home/juran/caffe/build/tools/caffe train --solver /home/juran/distracteddriver/caffe_models/caffe_model_2/solver_2.prototxt 2>&1 | tee /home/juran/distracteddriver/caffe_models/caffe_model_2/model_2_train.log`
