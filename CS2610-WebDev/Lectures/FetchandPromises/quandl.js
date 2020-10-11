// Erik's API key. Get your own :P
let apiKey = 'api_key=x35gV-p5u8QtHdwgi-we';
let start = "start_date=2018-11-01",
    end   = "end_date=2018-11-07";

// Return a parameter string for a GET request from its arguments
var formParamsString = function() {
    let argsArray = Array.from(arguments);
    let url = argsArray.shift();
    return `${url}?${argsArray.join('&')}`;
}



// global variable to contain the result of our asynchronous request
var theData;

var go_fetch = function() {

    let url = '';
    switch ( document.querySelector('#dataset').value ) {
        case "visa":
            url = formParamsString('https://www.quandl.com/api/v3/datasets/EOD/V.json', apiKey, start, end);
            break;

        case "ge":
            url = formParamsString('https://www.quandl.com/api/v3/datasets/EOD/GE.json', apiKey, start, end);
            break;

        case "treasury":
            url = formParamsString('https://www.quandl.com/api/v3/datasets/FED/SVENPY.json', apiKey, start, end);
            break;

        case "poptot":
            url = formParamsString('https://www.quandl.com/api/v3/datasets/UGID/POPTOT_.json', apiKey);
            break;

        case "slcpop":
            url = formParamsString('https://www.quandl.com/api/v3/datasets/CITYPOP/CITY_SALTLAKECITYUTUSA.json', apiKey);
            break;

        case "nycpop":
            url = formParamsString('https://www.quandl.com/api/v3/datasets/CITYPOP/CITY_NEWYORKNYUSA.json', apiKey);
            break;
    }

    console.log(url);

    fetch(url)
        .then( r => r.json() )
        .then( json => {
            theData = json;
            document.querySelector('#quandl').textContent = "Your data is available in the variable 'theData'";
            document.title = theData.dataset.name;
        });

}
