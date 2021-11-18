// load the things we need
var express = require('express');
var app = express();

// set the view engine to ejs
app.set('view engine', 'ejs');




// Home page 
app.get('/', function(req, res) {
    var tagline = "Created by Houston Consulting Solutions";

    res.render('pages/index', {
        tagline: tagline
    });
});



// customer page
app.get('/customers', function(req, res) {
    res.render('pages/customers');
});

app.get('/add_customers', function(req, res) {
    res.render('pages/add_customers');
});

app.get('/lookup_customers', function(req, res) {
    res.render('pages/lookup_customers');
});


app.get('/delete_customers', function(req, res) {
    res.render('pages/delete_customers');
});

app.get('/update_customers', function(req, res) {
    res.render('pages/update_customers');
});

app.get('/all_customers', function(req, res) {
    res.render('pages/all_customers');
});



//employees
app.get('/employees', function(req, res) {
    res.render('pages/employees');
});

app.get('/add_employees', function(req, res) {
    res.render('pages/add_employees');
});

app.get('/lookup_employees', function(req, res) {
    res.render('pages/lookup_employees');
});

app.get('/delete_employees', function(req, res) {
    res.render('pages/delete_employees');
});

app.get('/update_employees', function(req, res) {
    res.render('pages/update_employees');
});

app.get('/all_employees', function(req, res) {
    res.render('pages/all_employees');
});


//service request
app.get('/service_request', function(req, res) {
    res.render('pages/service_request');
});

app.get('/add_service_request', function(req, res) {
    res.render('pages/add_service_request');
});

app.get('/lookup_service_request', function(req, res) {
    res.render('pages/lookup_service_request');
});

app.get('/delete_service_request', function(req, res) {
    res.render('pages/delete_service_request');
});

app.get('/update_service_request', function(req, res) {
    res.render('pages/update_service_request');
});

app.get('/all_service_request', function(req, res) {
    res.render('pages/all_service_request');
});








app.listen(8080);
console.log('8080 is the magic port');
