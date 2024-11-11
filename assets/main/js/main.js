// AJAX = Asynchronous Javascript And Xml
// function showCountries() {
//     let xhr = new XMLHttpRequest();
//
//     // xhr.open('GET', 'https://restcountries.com/v3.1/all', true);
//
//     xhr.open('GET', 'http://127.0.0.1:8000/api/color/', true)
//
//     xhr.onload = function() {
//         if (xhr.status == 200) {
//             console.log('success');
//             let countries = JSON.parse(this.responseText);
//             console.log(countries);
//
//             countries.results.forEach(country => {
//                 console.log(country.name);
//                 const countryCard = document.createElement('div');
//                 countryCard.innerHTML = country.name;
//                 document.getElementById('feed').appendChild(countryCard);
//             });
//         }
//     };
//
//     xhr.send();
// }