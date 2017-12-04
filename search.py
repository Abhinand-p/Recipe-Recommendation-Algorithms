import unirest
# These code snippets use an open-source library. http://unirest.io/python
response = unirest.get("https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients?fillIngredients=false&ingredients=apples%2Cflour%2Csugar&limitLicense=false&number=5&ranking=1",
  headers={
    "X-Mashape-Key": "7JTdJTOMygmshkjAxSgkxUViVmlWp1ZqEOCjsnUiOIMyEsSe2G",
    "Accept": "application/json"
  }
)

print response.raw_body