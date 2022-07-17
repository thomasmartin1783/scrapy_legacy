const translate = require('google-translate-api-x');
var fs = require('fs');

data = [
    "The aristrocat hotel",

]

async function test(i) {

    const res = await translate(i, {
        from: 'en',
        to: 'bn',
    });
    console.log(res.text); //=> I speak English

    var dataToWrite = `"${res.text}",\n`
    fs.appendFile('output.csv', dataToWrite, 'utf8', function (err) {
        if (err) {
            console.log('Some error occured');
        } else {
            console.log('It\'s saved!');
        }
    });

    // console.log(res.from.language.iso); //=> nlx
}

data.forEach(i => {
    test(i);
});