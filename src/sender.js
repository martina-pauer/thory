function sendToServer()
{
    // Collect all the data from the form and send with some API to Python Back-End
    // JSON values for the getted from the inputs
    let data = {
        "product" : document.getElementById("thory-product").value,
        "units": document.getElementById("thory-units").value,
        "currency": document.getElementById("thory-currency").value,
        "price": document.getElementById("thory-price").value

    };
    // Storage as Cookies for get later with Flask and split(',') mwthod
    output = data.product + ',' + data.units + ',' + data.currency + ',' + data.price;
    document.cookie = "thory=" + output + ";expires=; path=/ samesite";
}