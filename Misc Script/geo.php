<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>HTML5 Geolocation</title>
<script  type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=true"></script>
<script>
 
    if(navigator.geolocation) {
 
        function visitorLocation(position) {
            var latitude = position.coords.latitude;
            var longitude = position.coords.longitude;
            alert (latitude);
            alert(longitude);
            var point = new google.maps.LatLng(position.coords.latitude, position.coords.longitude),
            
            
            myOptions = {
                zoom: 15,
                center: point,
                mapTypeId: google.maps.MapTypeId.ROADMAP
            },
 
            mapDiv = document.getElementById("mapDiv"),
            map = new google.maps.Map(mapDiv, myOptions),
 
            marker = new google.maps.Marker({
                position: point,
                map: map,
                title: "You are here"
            });
        }
        navigator.geolocation.getCurrentPosition(visitorLocation);
    }
</script>
<style>
#mapDiv {
    width:500px;
    height:300px;
    border:1px solid #efefef;
    margin:auto;
    -moz-box-shadow:5px 5px 10px #000;
    -webkit-box-shadow:5px 5px 10px #000;
}
</style>
</head>
<body>
<div id="mapDiv"></div>
</body>
</html>