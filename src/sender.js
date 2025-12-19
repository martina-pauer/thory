function sendToServer()
{
    // Collect all the data from the form and send with some API to Python Back-End
    // JSON values for the getted from the inputs
    let data = {
        "product" : document.getElementById("thory-product").value,
        "units": document.getElementById("thory-units").value,
        "currency": document.getElementById("thory-currency").value

    };
    // Modify in the future WHEN KNOW HOW SEND TO PYTHON BACKEND
    console.log(data);
}