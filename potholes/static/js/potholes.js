$(function () {
	
	var map = L.map('map').setView([40.4406, -79.9961], 13);
	
	L.tileLayer('http://{s}.tile.cloudmade.com/{key}/997/256/{z}/{x}/{y}.png', {
    	key: '556944c7a8de4e198895cbeae74a0eea',
    	styleId: 997
	}).addTo(map);
	
});
