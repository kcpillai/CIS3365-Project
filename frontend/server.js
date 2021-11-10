// load the things we need
var express = require('express');
var app = express();

// set the view engine to ejs
app.set('view engine', 'ejs');

// use res.render to load up an ejs view file

// index page 
app.get('/', function(req, res) {
    var mascots = [
        { name: 'Tammy', organization: "DigitalOcean", birth_year: 2012},
        { name: 'Tuxedo', organization: "Linux", birth_year: 1996},
        { name: 'Moby Dock', organization: "Docker", birth_year: 2013}
    ];
    var tagline = "No programming concept is complete without a cute animal mascot.";

    res.render('pages/index', {
        mascots: mascots,
        tagline: tagline
    });
});

// about page
app.get('/about', function(req, res) {
    res.render('pages/about');
});

// customer page
app.get('/customers', function(req, res) {
    res.render('pages/customers');
});

app.get('/employees', function(req, res) {
    res.render('pages/employees');
});

app.get('/lookup_customers', function(req, res) {
    res.render('pages/add_customers');
});

app.get('/add_customers', function(req, res) {
    res.render('pages/lookup_customers');
});

app.get('/delete_customers', function(req, res) {
    res.render('pages/delete_customers');
});



app.listen(8080);
console.log('8080 is the magic port');
