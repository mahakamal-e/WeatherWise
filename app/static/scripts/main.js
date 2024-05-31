$(document).ready(function() {
    const $locationButton = $('#locationButton');
    const $searchForm = $('#search-form');
    const $cityInput = $('#cityInput');

    $('<input>').attr({ type: 'hidden', id: 'useLocation', name: 'use_location', value: 'false' }).appendTo($searchForm);

    $locationButton.on('click', function() {
        $('#useLocation').val('true');
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition, showError);
        } else {
            alert("Geolocation is not supported by this browser.");
        }
    });

    function showPosition(position) {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;
        console.log("Latitude:", lat);
        console.log("Longitude:", lon);
        $('<input>').attr({ type: 'hidden', name: 'latitude', value: lat }).appendTo($searchForm);
        $('<input>').attr({ type: 'hidden', name: 'longitude', value: lon }).appendTo($searchForm);
        // Submit the form after obtaining the location
        $searchForm.submit();
    }

    function showError(error) {
        switch (error.code) {
            case error.PERMISSION_DENIED:
                alert("User denied the request for Geolocation.");
                break;
            case error.POSITION_UNAVAILABLE:
                alert("Location information is unavailable.");
                break;
            case error.TIMEOUT:
                alert("The request to get user location timed out.");
                break;
            case error.UNKNOWN_ERROR:
                alert("An unknown error occurred.");
                break;
        }
    }
    // Check if the map container exists and if Leaflet is available
    if ($('#map').length && typeof L !== 'undefined') {
        // Initialize map only if it hasn't been initialized before
        if (!window.mapInitialized) {
            var map = L.map('map').setView([currentWeather.lat, currentWeather.lon], 13);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(map);
            L.marker([currentWeather.lat, currentWeather.lon]).addTo(map)
                .bindPopup(`<b>${currentWeather.city}</b>`).openPopup();

            // Set a flag to indicate map initialization
            window.mapInitialized = true;
        }
    }
});