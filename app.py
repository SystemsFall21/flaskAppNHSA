from flask import Flask, render_template, request, send_file
from datetime import date
from dateutil.relativedelta import relativedelta
import random
import preload_data
import cencus

#dictionary, key = state name, value = [[fip],[coynty list]]
#dictionary, key = county name, value = [[fip],[location]]
state_dic,county_dic = preload_data.preload_county_data()
#dictionary, key = var catagory, value = [[name],[code],[description],[new code]]
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
  category = request.form.get('category')
  result_list = cencus.get_cencus(state,county,category)
  if category == "Educational Attainment":
    return render_template('education.html', result_list = result_list, state = state, county = county)
  if category == 'Children Under 6 Population Living With Family':
     return render_template('family.html', result_list = result_list, state = state, county = county)
  if category == "Children in Foster Care":
    return render_template('foster.html', result_list = result_list, state = state, county = county)
  if category == "Health Insurance Coverage":
    return render_template('health.html', result_list = result_list, state = state, county = county)
  if category == 'Population Living With Disabilities':
    return render_template('disability.html', result_list = result_list, state = state, county = county)
  if category == 'Population in Poverty by Age':
    return render_template('poverty.html', result_list = result_list, state = state, county = county)
  if category == 'Race and Ethnicity':
    return render_template('simple.html', result_list = result_list, state = state, county = county)
  if category == 'SSI, Cash Public Assistance, Food Stamps':
    return render_template('ssi.html', result_list = result_list, state = state, county = county)
  if category == 'School Enrollment':
    return render_template('school.html', result_list = result_list, state = state, county = county)
  if category == 'Teen mothers':
    return render_template('teen.html', result_list = result_list, state = state, county = county)
  if category == 'Total population':
    return render_template('population.html', result_list = result_list, state = state, county = county)
  if category == 'Unemployment Rate':
    return render_template('unemployment.html', result_list = result_list, state = state, county = county)

@app.route('/categaryList',methods =['GET','POST'])
def categaryList():
  return render_template('cateList.html', var_data = var_data)

@app.route('/resources')
def resources():
  return render_template('resources.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/myData')
def myData():
  return render_template('my_data.html')

@app.route('/download_pie')
def download_pie():
  return send_file("pie_template.xlsx", attachment_filename="pie_template.xlsx", as_attachment=True)

@app.route('/download_one_var')
def download_one_var():
  return send_file("one_variable_template.xlsx", attachment_filename="one_variable_template.xlsx", as_attachment=True)

@app.route('/download_two_var')
def download_two_var():
  return send_file("two_variable_template.xlsx", attachment_filename="two_variable_template.xlsx", as_attachment=True)

app.secret_key = 'some key that you will never guess'
if __name__ == "__main__":
	app.run('127.0.0.1', 8000, debug = False)