# Keras Flask WebApp

A simple web-app for Cat-Dog prediction using a pre-trained VGG16 model, the training was done using Keras API with Tensorflow
Backend.

`Here is the link to the VGG16 pretrained model` - https://drive.google.com/file/d/0Bz7KyqmuGsilT0J5dmRCM0ROVHc/view 

I built a a Cat-Dog classifier using Transfer Learning.
Downloaded the pretrained VGG16 model, and then froze all the layers except for the last layer, so that they dont 
get affected while retraining the last layer.

Saved the model as `VGG16_cats_and_dogs.h5` 

Note: You have to train the above model for it to work for you. Check the `CNN.ipynb` for a complete detail on how
      you can use your custom data to retrain the model. In case the amount of data you have is less, check out the
      `DataAugumentation.ipynb`.

Built a simple web-app using HTML, CSS and jQuery on the Front-End and Flask server on the Backend.

### Execution: -

If you are running a virtual environment for Tensorflow, activate it and `cd` into the directory of the project.

To run the code, type ``

```
$ export FLASK_APP=predict_app.py
$ python -m flask run
```

The web app should be running on you localhost!
