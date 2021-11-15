from flask import Flask, render_template, request, session, url_for, redirect, flash, Response
from datetime import date
from dateutil.relativedelta import relativedelta
import random
import preload_data
import cencus

#dictionary, key = state name, value = [[fip],[coynty list]]
#dictionary, key = county name, value = [[fip],[location]]
state_dic,county_dic = preload_data.preload_county_data()
#dictionary, key = var catagory, value = [[name],[code],[description]]
var_info,var_data = preload_data.preload_var()

app = Flask(__name__)

@app.route('/')
def welcome():
  return render_template('welcome.html')


@app.route('/searchCounty')
def search():
  return render_template('county_search.html', state_dic = state_dic)

@app.route('/searchCountyAuth', methods=['GET','POST'])
def searchCountyAuth():
  state = request.form.get('state')
  county = request.form.get('county')
  catagory = request.form.get('catagory')
  result_list = cencus.get_cencus(state,county,catagory)

  return render_template('county_result.html', result_list = result_list, state = state, county = county)

@app.route('/cataList',methods =['GET','POST'])
def cataList():
  return render_template('cataList.html', var_data = var_data)

@app.route('/external')
def external():
  return render_template('external_source.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/myData')
def myData():
  return render_template('my_data.html')

app.secret_key = 'some key that you will never guess'
if __name__ == "__main__":
	app.run('127.0.0.1', 8000, debug = True)