const fs = require('fs');
const businesses = require('./business.json');

const businessMap = new Map();
const categories = new Set();
businesses.forEach(business => {
    businessMap.set(business.business_id, business)
    if(business.categories) business.categories.split(", ").forEach((cat) => categories.add(cat));
});
console.log(categories.size);

const category = "Seafood"

var stream = fs.createReadStream('review.json', {flags: 'r', encoding: 'utf-8'});
var writeStream = fs.createWriteStream(`${category}_reviews.json`);

writeStream.on('finish', () => {
    console.log('Wrote all reviews to file');
})


var buf = '';
var categoryReviews = [];
var processedReviews = 0;

stream.on('data', function(d) {
    buf += d.toString(); // when data is read, stash it in a string buffer
    processBuffer();
});

stream.on('end', () => {
    writeStream.end();
    // fs.writeFile(`${category}_reviews.json`,JSON.stringify(categoryReviews), (err) => {
    //     if(err) {
    //         return console.log(err);
    //     }
    //     console.log("The file was saved");
    // })
})

function processBuffer() {
    var pos;

    while ((pos = buf.indexOf('\n')) >= 0) { // keep going while there's a newline somewhere in the buffer
        if (pos == 0) { // if there's more than one newline in a row, the buffer will now start with a newline
            buf = buf.slice(1); // discard it
            continue; // so that the next iteration will start with data
        }
        processLine(buf.slice(0,pos)); // hand off the line
        buf = buf.slice(pos+1); // and slice the processed data off the buffer
    }
}


var formattingObj = {};
function processLine(line) { // here's where we do something with a line

    if (line[line.length-1] == '\r') line=line.substr(0,line.length-1); // discard CR (0x0D)

    if (line.length > 0) { // ignore empty lines
        processedReviews += 1;
        if (processedReviews % 1000 === 0) {
            console.log({ processedReviews });
        }
        var obj = JSON.parse(line); // parse the JSON
        business = businessMap.get(obj.business_id);
        reviewCategories = business.categories;

        if (reviewCategories && reviewCategories.includes(category)){
            formattingObj = { stars: obj.stars, useful: obj.useful, funny: obj.funny, cool: obj.cool, text: obj.text };
            writeStream.write(`${JSON.stringify(formattingObj)}\n`, 'utf-8')
            // categoryReviews.push({ ...obj, business: { categories: business.categories, name: business.name} });
            // console.log({ obj, business }); // do something with the data here!
        }
    }
}