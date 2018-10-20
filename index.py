from flask import Flask,render_template,redirect,request,jsonify
from scrap import GamePriceComparator
import datetime,json
app = Flask(__name__)

#https://hackersandslackers.com/starting-a-flask-project-with-heroku/

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/ajax/search', methods = ['GET'])
def search_games():
	search=request.args["q"]
	tienda=request.args["tienda"]
	try:
		if tienda=="amazon":
			file=open("data/search_data.json","a")
			data={	"query":search,
					"date":str(datetime.datetime.now())}
			json.dump(data,file)
			file.write("\n")
			file.close()
	except Exception as e:
		print(e)
	try:
		comparator=GamePriceComparator()
		
		if tienda=="fnac":
			return search_fnac(search)
		elif tienda=="instant_gaming":
			return search_instant_gaming(search)
		elif tienda=="corte_ingles":
			return search_corte_ingles(search)
		elif tienda=="amazon":
			return search_amazon(search)
		elif tienda=="game":
			return search_game(search)
	except Exception as e:
		print("Error",e)
		return jsonify(error="error")

@app.errorhandler(404)
def page_not_found(e):
	return redirect("/")

def search_fnac(search):
	comparator=GamePriceComparator()
	fnac=comparator.get_price_fnac(search)
	return jsonify(price_fnac=fnac[0],
						url_fnac=fnac[1],
						name_fnac=fnac[2],)

def search_instant_gaming(search):
	comparator=GamePriceComparator()
	instant_gaming=comparator.get_price_instant_gaming(search)
	return jsonify(	price_instant_gaming=instant_gaming[0],
					url_instant_gaming=instant_gaming[1],
					name_instant_gaming=instant_gaming[2],)

def search_corte_ingles(search):
	comparator=GamePriceComparator()
	corte_ingles=comparator.get_price_corte_ingles(search)
	return jsonify(	price_corte_ingles=corte_ingles[0],
					url_corte_ingles=corte_ingles[1],
					name_corte_ingles=corte_ingles[2],)

def search_amazon (search):
	comparator=GamePriceComparator()
	amazon=comparator.get_price_amazon(search)
	return jsonify(	price_amazon=amazon[0],
					url_amazon=amazon[1],
					name_amazon=amazon[2],)

def search_game (search):
	comparator=GamePriceComparator()
	game=comparator.get_price_game(search)
	return jsonify(	price_game=game[0],
					url_game=game[1],
					name_game=game[2],)