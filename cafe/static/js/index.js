const axios = require('axios')



console.log("hello")
var data =  axios({
    url: 'http://127.0.0.1:8000/api/get',
    method: 'get',
    param:'@',
    timeout: 3000,
    headers: { 'X-Requested-With': 'XMLHttpRequest' },



})
.then((response)=>{
    console.log( response.data[1].menu)
});



