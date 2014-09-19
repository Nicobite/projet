// A very basic web server in node.js
// Stolen from: Node.js for Front-End Developers by Garann Means (p. 9-10)
 
var port = 5555;
var serverUrl = "127.0.0.1";
 
var http = require("http");
var path = require("path");
var fs = require("fs");

var page = "test.html";
 
console.log("Starting web server at " + serverUrl + ":" + port);


var mysql      = require('mysql');
var connectionDB = mysql.createConnection({
  host     : "localhost",
  user     : "root",
  password : "root",
  database : "test1"
});

//connectionDB.connect();
connectionDB.query(
	'SELECT * FROM messages', 
	function(err, rows, fields){
	  if (err) throw err;
	  else{
		console.log('[request] line#1: ' + rows[0]['action']);
		console.log('[request] line#2: ' + rows[1]['action']);
		//console.log('[request] line#3: ' + rows[2]['action']);
	  }
	  connectionDB.end();
	}
);

//
//*/

http.createServer( function(req, res) {
	var now = new Date();
	var filename = req.url || page;
	var ext = path.extname(filename);
	var localPath = __dirname;
	var validExtensions = {
		".html" : "text/html",	
		".js": "application/javascript",
		".css": "text/css",
		".txt": "text/plain",
		".jpg": "image/jpeg",
		".gif": "image/gif",
		".png": "image/png"
	};
	var isValidExt = validExtensions[ext];
	if (isValidExt) {
		localPath += filename;
		path.exists(localPath, function(exists) {
			if(exists) {
				console.log("Serving file: " + localPath);
				getFile(localPath, res, ext);
			} else {
				console.log("File not found: " + localPath);
				res.writeHead(404, {'Content-Type': 'text/plain'});
				res.end(filename+' not found\n');
			}
		});
	} else {
		console.log("Invalid file extension detected: " + ext)
	}
}).listen(port, serverUrl);
 
function getFile(localPath, res, mimeType) {
	fs.readFile(localPath, function(err, contents) {
	if(!err) {
		res.setHeader("Content-Length", contents.length);
		res.setHeader("Content-Type", mimeType);
		res.statusCode = 200;
		res.end(contents);
	} else {
			res.writeHead(500);
			res.end();
		}
	});
}