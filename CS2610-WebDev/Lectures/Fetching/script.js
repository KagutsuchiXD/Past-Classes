let apikey = 'x35gV-p5u8QtHdwgi-we';
let start = new Date();
let end = new Date();
start.setDate(end.getDate()-5);
end = (end.getFullYear + (('0' + (end.getMonth()+1)).slice(-2)) + (('0' + end.getDate()).slice(-2)));
start = (start.getFullYear + (('0' + (start.getMonth()+1)).slice(-2)) + (('0' + start.getDate()).slice(-2)));
var data;

var goldRUrl = `https://www.quandl.com/api/v3/datasets/LBMA/GOLD.json?api_key=${apikey}&column_index=2&
start_date=${start}&end_date=${end}`;

console.log(goldRUrl);

fetch(goldRUrl)
    .then( r => r.json() )
    .then( json => {
        data = json;
    });
let price = data[0][4][-1][-1];