# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
import sys

# Load the Random Forest CLassifier model
filename = 'TrainedModels/first-innings-score-ridge-model.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()
    
    if request.method == 'POST':
        
        batting_team = request.form['batting-team']
        
        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array + [0]
        elif batting_team == 'Delhi Capitals':
            temp_array = temp_array + [1]
        elif batting_team == 'Kings XI Punjab':
            temp_array = temp_array + [2]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [3]
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [4]
        elif batting_team == 'Rajasthan Royals':
            temp_array = temp_array + [5]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [6]
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [7]
            
            
        bowling_team = request.form['bowling-team']
        
        if bowling_team == 'Chennai Super Kings':
            temp_array = temp_array + [0]
        elif bowling_team == 'Delhi Capitals':
            temp_array = temp_array + [1]
        elif bowling_team == 'Kings XI Punjab':
            temp_array = temp_array + [2]
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [3]
        elif bowling_team == 'Mumbai Indians':
            temp_array = temp_array + [4]
        elif bowling_team == 'Rajasthan Royals':
            temp_array = temp_array + [5]
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [6]
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [7]
            
            
        overs = int(request.form['overs'])
        balls = int(request.form['balls'])
        batsman_runs = int(request.form['batsman runs'])
        extra_runs = int(request.form['extra runs'])
        wickets = int(request.form['wickets'])
        
        temp_array = temp_array + [overs, balls,batsman_runs,extra_runs,wickets]
        
        venue = request.form['venue']
        grounds = ['Barabati Stadium', 'Brabourne Stadium', 'Buffalo Park',
       'De Beers Diamond Oval', 'Dr DY Patil Sports Academy',
       'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
       'Eden Gardens', 'Feroz Shah Kotla', 'Green Park',
       'Himachal Pradesh Cricket Association Stadium',
       'Holkar Cricket Stadium', 'Kingsmead', 'M Chinnaswamy Stadium',
       'MA Chidambaram Stadium, Chepauk',
       'Maharashtra Cricket Association Stadium', 'Nehru Stadium',
       'New Wanderers Stadium', 'Newlands', 'OUTsurance Oval',
       'Punjab Cricket Association IS Bindra Stadium, Mohali',
       'Punjab Cricket Association Stadium, Mohali',
       'Rajiv Gandhi International Stadium, Uppal',
       'Sardar Patel Stadium, Motera',
       'Saurashtra Cricket Association Stadium', 'Sawai Mansingh Stadium',
       "St George's Park", 'Subrata Roy Sahara Stadium',
       'SuperSport Park', 'Vidarbha Cricket Association Stadium, Jamtha',
       'Wankhede Stadium']

        index = grounds.index(venue)
        temp_array = temp_array + [index]

        data = np.array([temp_array])
        print(data,file=sys.stderr)
        my_prediction = int(regressor.predict(data))
        print(my_prediction,file=sys.stderr)
        return render_template('result.html', lower_limit = my_prediction-10, upper_limit = my_prediction+5)

if __name__ == '__main__':  
	app.run(debug=True)
    
