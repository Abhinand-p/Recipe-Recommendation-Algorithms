import os
import shutil
import unirest


from flask import Flask, render_template, request, redirect,url_for, send_from_directory
from werkzeug.utils import secure_filename
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
UPLOAD_FOLDER = '/Users/abhinandp/PycharmProjects/AIW-FoodRec/uploads/'
ALLOWED_EXTENSIONS =set(['jpeg','png','jpg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER


@app.route('/')
def division():
    return render_template('divisions.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
def upload():
    filelist0 = [f for f in os.listdir("/Users/abhinandp/PycharmProjects/AIW-FoodRec/uploads/")]
    for files0 in filelist0:
        os.remove('/Users/abhinandp/PycharmProjects/AIW-FoodRec/uploads/'+files0)

    if request.method == 'POST' and 'file' in request.files:
        for f in request.files.getlist('file'):
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))

    recive1= clarifai1()
    # clear_files_uploads()
    # recive2= clarifai2()
    # clear_files_uploads()
    # recive3= clarifai3()
    # clear_files_uploads()
    filelist1 = [f for f in os.listdir("/Users/abhinandp/PycharmProjects/AIW-FoodRec/uploads/")]
    filelist2=[]
    for fies in filelist1:
        x=""
        x= str(fies)
        y=[]
        y=x.split('.')
        filelist2.append(y[0])
    ans = search(filelist2)
    return render_template('divisions.html',log1=recive1,name=filelist2,final=ans)

def clarifai1():

    filelist1 = [f for f in os.listdir("/Users/abhinandp/PycharmProjects/AIW-FoodRec/uploads/")]

    app = ClarifaiApp()
    model = app.models.get('food-items-v1.0')
    # image = ClImage(url='https://samples.clarifai.com/food.jpg')
    string1=""
    for files1 in filelist1:
        image = ClImage(filename='/Users/abhinandp/PycharmProjects/AIW-FoodRec/uploads/'+files1)
        response = model.predict([image])
        concepts = response['outputs'][0]['data']['concepts']
        string1+=str(concepts[0])
    return string1
#
# def clarifai2():
#
#     filelist2 = [f for f in os.listdir("/Users/abhinandp/PycharmProjects/AIW-FoodRec/uploads/")]
#
#     app = ClarifaiApp()
#     model = app.models.get('food-items-v1.0')
#     # image = ClImage(url='https://samples.clarifai.com/food.jpg')
#     for files2 in filelist2:
#         image = ClImage(filename='/Users/abhinandp/PycharmProjects/AIW-FoodRec/uploads/'+files2)
#
#     response = model.predict([image])
#
#     concepts = response['outputs'][0]['data']['concepts']
#     # for concept in concepts:
#     #     print(concept['name'], concept['value'])
#     string2=""
#     string2+=str(concepts[0])
#
#     return string2
#
# def clarifai3():
#
#     filelist3 = [f for f in os.listdir("/Users/abhinandp/PycharmProjects/AIW-FoodRec/uploads/")]
#
#     app = ClarifaiApp()
#     model = app.models.get('food-items-v1.0')
#     # image = ClImage(url='https://samples.clarifai.com/food.jpg')
#     for files3 in filelist3:
#         image = ClImage(filename='/Users/abhinandp/PycharmProjects/AIW-FoodRec/uploads/'+files3)
#
#     response = model.predict([image])
#
#     concepts = response['outputs'][0]['data']['concepts']
#     # for concept in concepts:
#     #     print(concept['name'], concept['value'])
#     string3=""
#     string3+=str(concepts[0])
#
#     return string3
def search(x):
  response = unirest.get(
    "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients?fillIngredients=false&ingredients="+x[0]+"%2C"+x[1]+"%2C"+x[2]+"&limitLicense=false&number=5&ranking=1",
    headers={
      "X-Mashape-Key": "7JTdJTOMygmshkjAxSgkxUViVmlWp1ZqEOCjsnUiOIMyEsSe2G",
      "Accept": "application/json"})
  x = response.raw_body
  print x;
  lis = []
  arr = x.split("title")
  for i in arr:
      ans = i.split(",")[0];
      lis.append(ans[3:len(ans) - 1]);
  return lis

def clear_files_uploads():
	shutil.rmtree('/Users/abhinandp/PycharmProjects/AIW-FoodRec/uploads/')
	os.system("mkdir uploads")

if __name__ == '__main__':
    app.run(debug=True)
