function onClickedEstimatePrice() {
    var area = document.getElementById("uiSqft").value;
    var bhk = document.querySelector('input[name="uiBHK"]:checked').value;
    var bathrooms = document.querySelector('input[name="uiBathrooms"]:checked').value;
    var location = document.getElementById("uiLocations").value;

    var data = {
        area: area,
        bhk: bhk,
        bathrooms: bathrooms,
        location: location
    };

    fetch("http://localhost:5000/predict_price", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        var price = result.price;
        document.getElementById("uiEstimatedPrice").innerHTML = "<h2>Estimated Price: " + price + "</h2>";
    })
    .catch(error => {
        console.log("Error:", error);
    });
}
