$(function () {
	
	var map = L.map('map').setView([40.4406, 79.9961], 13);
	
	L.tileLayer('http://{s}.tile.cloudmade.com/556944c7a8de4e198895cbeae74a0eea/997/256/{z}/{x}/{y}.png', {
    	attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
    	maxZoom: 18
	}).addTo(map);
	
});
