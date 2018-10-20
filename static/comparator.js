var show = function (elem) {
	elem.classList.add('is-visible');
};

var hide = function (elem) {
	elem.classList.remove('is-visible');
};

var toggle = function (elem) {
	elem.classList.toggle('is-visible');
};

function searchGames(){
	if(document.getElementById('js-search-query').value == ""){
		show(document.getElementById("js-empty-search"));
		return;
	}
	hide(document.getElementById("js-empty-search"));
	document.getElementById("js-search-title").innerHTML=document.getElementById('js-search-query').value;
	searchGame();
	searchFnac();
	searchAmazon();
	searchInstantGaming();
	searchCorteIngles();
	show(document.getElementById("js-search-results"));
	
}

function searchFnac(){
	show(document.getElementById('js-loading-fnac'))
	hide(document.getElementById('js-results-fnac'))
	var req = new XMLHttpRequest()
	req.onreadystatechange = function()
	{
		if (req.readyState == 4)
		{
			if (req.status != 200)
			{
				//var response = JSON.parse(req.responseText)
				document.getElementById('js-search-results').innerHTML = "ERROR"

			}
			else
			{
				var response = JSON.parse(req.responseText)
				hide(document.getElementById('js-loading-fnac'))
				show(document.getElementById('js-results-fnac'))
				document.getElementById('js-price-fnac').innerHTML=response.price_fnac;
				document.getElementById('js-url-fnac').href=response.url_fnac;
				document.getElementById('js-name-fnac').innerHTML=response.name_fnac;

			}
		}
	}
	var q = document.getElementById('js-search-query').value
	req.open('Get', '/ajax/search?q='+q+"&tienda=fnac")
	console.log('/ajax/search?q='+q+"&tienda=fnac")
	req.send()
	
	return false
}

function searchAmazon(){
	show(document.getElementById('js-loading-amazon'))
	hide(document.getElementById('js-results-amazon'))
	var req = new XMLHttpRequest()
		req.onreadystatechange = function()
		{
			if (req.readyState == 4)
			{
				if (req.status != 200)
				{
					//var response = JSON.parse(req.responseText)
					document.getElementById('js-search-results').innerHTML = "ERROR"
					show(document.getElementById('js-search-results'))

				}
				else
				{
					hide(document.getElementById('js-loading-amazon'))
					show(document.getElementById('js-results-amazon'))
					var response = JSON.parse(req.responseText)
					document.getElementById('js-price-amazon').innerHTML=response.price_amazon;
					document.getElementById('js-url-amazon').href=response.url_amazon;
					document.getElementById('js-name-amazon').innerHTML=response.name_amazon;

				}
			}
		}
		var q = document.getElementById('js-search-query').value
		req.open('Get', '/ajax/search?q='+q+"&tienda=amazon")
		req.send()
		
		return false
}

function searchInstantGaming(){
	show(document.getElementById('js-loading-instant-gaming'))
	hide(document.getElementById('js-results-instant-gaming'))
	var req = new XMLHttpRequest()
		req.onreadystatechange = function()
		{
			if (req.readyState == 4)
			{
				if (req.status != 200)
				{
					//var response = JSON.parse(req.responseText)
					document.getElementById('js-search-results').innerHTML = "ERROR"
					show(document.getElementById('js-search-results'))

				}
				else
				{
					var response = JSON.parse(req.responseText)
					hide(document.getElementById('js-loading-instant-gaming'))
					show(document.getElementById('js-results-instant-gaming'))
					document.getElementById('js-price-instant-gaming').innerHTML=response.price_instant_gaming;
					document.getElementById('js-url-instant-gaming').href=response.url_instant_gaming;
					document.getElementById('js-name-instant-gaming').innerHTML=response.name_instant_gaming;

				}
			}
		}
		var q = document.getElementById('js-search-query').value
		req.open('Get', '/ajax/search?q='+q+"&tienda=instant_gaming")
		req.send()
		
		return false
}

function searchCorteIngles(){
	show(document.getElementById('js-loading-corte-ingles'))
	hide(document.getElementById('js-results-corte-ingles'))
	var req = new XMLHttpRequest()
		req.onreadystatechange = function()
		{
			if (req.readyState == 4)
			{
				if (req.status != 200)
				{
					//var response = JSON.parse(req.responseText)
					document.getElementById('js-search-results').innerHTML = "ERROR"
					show(document.getElementById('js-search-results'))

				}
				else
				{
					var response = JSON.parse(req.responseText)
					hide(document.getElementById('js-loading-corte-ingles'))
					show(document.getElementById('js-results-corte-ingles'))
					document.getElementById('js-price-corte-ingles').innerHTML=response.price_corte_ingles;
					document.getElementById('js-url-corte-ingles').href=response.url_corte_ingles;
					document.getElementById('js-name-corte-ingles').innerHTML=response.name_corte_ingles;

				}
			}
		}
		var q = document.getElementById('js-search-query').value
		req.open('Get', '/ajax/search?q='+q+"&tienda=corte_ingles")
		req.send()
		
		return false
}

function searchGame(){
	show(document.getElementById('js-loading-game'))
	hide(document.getElementById('js-results-game'))
	var req = new XMLHttpRequest()
	req.onreadystatechange = function()
	{
		if (req.readyState == 4)
		{
			if (req.status != 200)
			{
				//var response = JSON.parse(req.responseText)
				document.getElementById('js-search-results').innerHTML = "ERROR"
				show(document.getElementById('js-search-results'))

			}
			else
			{
				var response = JSON.parse(req.responseText)
				hide(document.getElementById('js-loading-game'))
				show(document.getElementById('js-results-game'))
				document.getElementById('js-price-game').innerHTML=response.price_game;
				document.getElementById('js-url-game').href=response.url_game;
				document.getElementById('js-name-game').innerHTML=response.name_game;

			}
		}
	}
	var q = document.getElementById('js-search-query').value
	req.open('Get', '/ajax/search?q='+q+"&tienda=game")
	req.send()
	
	return false
}



