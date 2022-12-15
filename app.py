import json
from flask import Flask, request
from serve import anime_recommend_api

# I've commented out the last import because it won't work in kernels,
# but you should uncomment it when we build our app tomorrow

# create an instance of Flask
app = Flask(__name__)

# load our pre-trained model & function
# recommender = anime_recommend_api()

# Define a post method for our API.


@app.route('/anime', methods=['POST'])
def extractpackages():
    """ 
    Takes in a json file, extracts the keywords &
    their indices and then returns them as a json file.
    """
    # the data the user input, in json format
    input_data = request.json
    print(request)

    # use our API function to get the keywords
    print(input_data)
    print(type(input_data))
    print(input_data['name'], input_data['type'])
    print(type(input_data['name']), type(input_data['type']))
    output_data = anime_recommend_api(input_data['name'], input_data['type'])

    # convert our dictionary into a .json file
    # (returning a dictionary wouldn't be very
    # helpful for someone querying our API from
    # java; JSON is more flexible/portable)
    response = json.dumps(output_data)

    # return our json file
    return response
