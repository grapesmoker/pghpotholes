$(function () {
	
	var map = L.map('map').setView([40.4406, -79.9961], 13);
	
	L.tileLayer('http://{s}.tile.cloudmade.com/556944c7a8de4e198895cbeae74a0eea/997/256/{z}/{x}/{y}.png', {
    	key: 'API-key',
    	styleId: 997
	}).addTo(map);
	
});
