from flask import Flask,jsonify,request

app = Flask(__name__)

import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib


@app.route('/train')
def train():
	df_train = pd.read_excel('False Alarm Cases.xlsx')
	df_train = df_train.iloc[:, 1:8]
	X = df_train.iloc[:,0:6]
	y = df_train['Spuriosity Index(0/1)']
	
	classifier = GaussianNB()
	classifier.fit(X, y)
	joblib.dump(classifier, 'filename.pkl')
    
	
	return 'Model has been Trained'
	
@app.route('/test', methods=['POST'])
def test():
	clf = joblib.load('filename.pkl')
	
	request_data = request.get_json()
	
	a = request_data['Ambient Temperature']
	b = request_data['Calibration']
	c = request_data['Unwanted substance deposition']
	d = request_data['Humidity']
	e = request_data['H2S Content']
	f = request_data['detected by']
	l = [a,b,c,d,e,f]
	narr = np.array(l)
	narr = narr.reshape(1,6)
	df_test = pd.DataFrame(narr, columns = ['Ambient Temperature', 'Calibration', 'Unwanted substance deposition',
	'Humidity', 'H2S Content', 'detected by'])
	
	ypred = clf.predict(df_test)
	
	if ypred ==1:
		result = 'Danger'
	
	else:
		result='No Danger'
	
	return jsonify({'Recommendation':result})
	
	
app.run(port=5000)