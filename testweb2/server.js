//TODO include script to clean out folder at end of day


//set up vars for server.js
var express = require('express');
var app = express();
var server = require('http').createServer(app);
var io = require('socket.io')(server);
var execute = require('child_process').exec;

var imgCounter = 0;

//serve static files
app.use(express.static(__dirname + '/public'));
app.use(express.static(__dirname + '/public/imgs'));

//redirect to index file
app.get('/',function(req, res, next) {
	res.sendFile(__dirname + '/public/index.html');
});

//when a client connects, do this
io.on('connection', function(client) { 
	console.log('Client connected...'); 
	var sessionid = client.id;
	client.emit('sendID', {ID: sessionid});

	client.on('emptyModel', function(data) {
		imgCounter = 0;
		console.log('Here we are making a new image for: '+ client.id);
		execute('python3 emptyModel.py '+ data.world.toString() + ' '+ data.prop.toString() + ' ' + client.id.toString() + ' ' + imgCounter.toString(), function(stdout, stderr, error) {
			console.log('stdout: ' + stdout);
			console.log('stderr: ' + stderr);
			if (error !== null) {
				console.log('exec error:' + error);
			}
		});
		client.emit('emptyModelCreated', {src: client.id.toString() + imgCounter.toString()});
	});

	client.on('nonEmptyModelUpdated', function(data) {
		execute('rm -f ./public/imgs/'+ client.id + imgCounter.toString() + '.png', function(stdout, stderr, error) {
			console.log('stdout: ' + stdout);
			console.log('stderr: ' + stderr);
			if (error !== null) {
				console.log('exec error:' + error);
			}
		});
		imgCounter = imgCounter + 1;
		execute('python3 nonEmptyModel.py '+ data.world.toString() + ' '+ data.prop.toString() + ' '+ data.valuation.toString() + ' '+ data.relation.toString() + ' ' + client.id.toString() + ' ' + imgCounter.toString(), function(stdout, stderr, error) {
			console.log('stdout: ' + stdout);
			console.log('stderr: ' + stderr);
			if (error !== null) {
				console.log('exec error:' + error);
			}
		});
		client.emit('modelUpdated', {src: client.id.toString() + imgCounter.toString()});
	});
	
	client.on('modelCheckerInput', function(data) {
		execute('python3 modelChecker.py '+ data.world.toString() + ' '+ data.prop.toString() + ' '+ data.valuation.toString() + ' ' + data.relation.toString() + ' ' + data.checkWorld.toString() + ' ' + data.checkFormula.toString(), function(stdout, stderr, error) {
			console.log('stdout: ' + stdout);
			console.log('stderr: ' + stderr);
			if (error !== null) {
				console.log('exec error:' + error);
			}
		});
		//add client.emit
	});
	
	client.on('disconnect', function(){
		execute('rm -f ./public/imgs/'+ client.id  + imgCounter.toString() +'.png', function(stdout, stderr, error) {
			console.log('stdout: ' + stdout);
			console.log('stderr: ' + stderr);
			if (error !== null) {
				console.log('exec error:' + error);
			}
		});
		console.log('user disconnected and all accompanying files deleted');
	});
});



//start web server and socket.io server listening
server.listen(3000, function() {
	console.log('listening has started');
});
