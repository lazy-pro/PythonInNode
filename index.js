var csv = require('csv');
var formidable = require('formidable');
//app.use(express.static('public'));
var obj = csv();

var MyData = [];

var { PythonShell } = require('python-shell');
var pyshell = new PythonShell('script.py');

obj.from.path('train.csv').to.array(function (data) {
    for (var index = 0; index < data[0].length; index++) {
        MyData.push(data[0][index]);
    }
    //console.log(MyData)
    str = JSON.stringify(MyData)
    str = str + "\nLoan_Status";
    pyshell.send(str);

    pyshell.on('message', function (message) {
        // received a message sent from the Python script (a simple "print" statement)
        console.log(message);
    });
    
    // end the input stream and allow the process to exit
    pyshell.end(function (err) {
        if (err) {
            throw err;
        };
    
        console.log('finished');
    });
});

var str = [];
str.push("ksjksjbv\ndfvdzf");



