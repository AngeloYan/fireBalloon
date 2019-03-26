var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
const processMessage = require('./process-message');

app.get('/', function (req, res) {
	res.sendFile(__dirname + '/index.html');
});

io.on('connection', function (socket) {
	socket.on('chat message', function (msg) {
		io.emit('chat message', msg);
		// io.emit('chat message', processMessage(msg));
		// processMessage(msg);
		requestDialogflow(msg);
	});
});

http.listen(3000, function () {
	console.log('listening on *:3000');
});

async function requestDialogflow(msg) {
	var processedMessage = await processMessage(msg);
	io.emit('chat message', processedMessage);
}