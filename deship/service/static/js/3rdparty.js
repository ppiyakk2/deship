var map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 37.245792, lng: 127.077192},
    zoom: 15
  });
  var myLatLng1 = {lat : 37.245792, lng : 127.077192};
  var marker1 = new google.maps.Marker({
    position: myLatLng1,
    map: map,
    title: '1'
  });
  var myLatLng2 = {lat : 37.245978, lng : 127.076650};
  var marker2 = new google.maps.Marker({
    position: myLatLng2,
    map: map,
    title: '2'
  });
  var myLatLng3 = {lat : 37.246155, lng : 127.077221}; 
  var marker3 = new google.maps.Marker({
    position: myLatLng3,
    map: map,
    title: '3'
  });
  var myLatLng4 = {lat : 37.241847, lng : 127.080021};  
  var marker4 = new google.maps.Marker({
    position: myLatLng4,
    map: map,
    title: '4'
  });
  var myLatLng5 = {lat : 37.239789, lng : 127.083448};   
  var marker5 = new google.maps.Marker({
    position: myLatLng5,
    map: map,
    title: '5'
  });
}