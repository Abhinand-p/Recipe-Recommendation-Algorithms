import os
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

# Creating our app model
app = ClarifaiApp()

# Adding our image for training
filelist = [f for f in os.listdir("AIW_Training_Images")]

for files in filelist:
    app.inputs.create_image_from_filename("AIW_Training_Images/"+files, concepts=['food'])