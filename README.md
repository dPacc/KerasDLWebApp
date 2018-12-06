# Cat-Dog Deep Learning WebApp

A simple web-app for Cat-Dog prediction using a pre-trained VGG16 model, the training was done using Keras API with Tensorflow
Backend.

### Link to download the VGG16 mode: -
 
https://drive.google.com/file/d/0Bz7KyqmuGsilT0J5dmRCM0ROVHc/view 

I built a a Cat-Dog classifier using Transfer Learning.
Downloaded the pretrained VGG16 model, and then froze all the layers except for the last layer, so that they dont 
get affected while retraining the last layer.

Saved the model as a .h5 file as follows `VGG16_cats_and_dogs.h5`. I haven't uploaded the model as its size is over 500MB.

### Note: - 

You have to train the above model for it to work for you. Check the `CNN.ipynb` for a complete detail on how
you can use your custom data to retrain the model. In case the amount of data you have is less, check out the `DataAugumentation.ipynb`.

#### Front-End:

`HTML, CSS & jQuery`

#### Backend:

`Flask`

### Execution: -

If you are running a virtual environment for Tensorflow, activate it and `cd` into the directory of the project.

To run the code, type ``

```
$ export FLASK_APP=predict_app.py

$ python -m flask run
```

The web app should be running on you localhost!
