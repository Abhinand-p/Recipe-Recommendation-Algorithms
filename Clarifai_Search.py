from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage


app = ClarifaiApp()
model = app.models.get('food-items-v1.0')
# image = ClImage(url='https://samples.clarifai.com/food.jpg')
image = ClImage(filename='uploads/radish.jpg')

response = model.predict([image])

concepts = response['outputs'][0]['data']['concepts']
# for concept in concepts:
#     print(concept['name'], concept['value'])
print concepts[0]