
document.addEventListener('DOMContentLoaded', () => {


let status = document.getElementById("status").innerHTML;
if(status = 'Хүсэлт илгээсэн'){

 document.getElementById("Хүсэлт илгээсэн").innerHTML= '&#10004;';

};
if(status == 'Хариу ирсэн'){

 document.getElementById("Хариу ирсэн").innerHTML = '&#10004;';

}
});
