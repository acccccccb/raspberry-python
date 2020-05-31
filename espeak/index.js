var http = require('http');
var exec = require('child_process').exec;
var os=require('os');
var system = os.platform();


function func(){}
func.prototype = {
    execute:function(cmd,callback){
        exec(cmd, function(error, stdout, stderr) {
            if(error){
                console.log(cmd+ ' fail');
                if(callback && typeof callback === 'function') {
                    console.log(error);
                    callback(false);
                }
            } else{
                console.log(cmd+ ' success');
                if(callback && typeof callback === 'function') {
                    callback(true);
                }
            }
        });
        return this;
    }
};
function run() { return new func(); }

var init = function(option){
    http.createServer(function(req, res){
res.setHeader('Access-Control-Allow-Origin', '*');
			res.setHeader('Access-Control-Allow-Headers', 'token');
res.setHeader('Access-Control-Allow-Methods', 'POST,GET,OPTIONS');
			res.setHeader('content-type', 'application/json');
        		
        console.log(req.method);
if(req.method==='OPTIONS') {
					res.writeHead(200, { 'Content-Type': 'text/plain' });
					res.end()
				} else {

res.setHeader('Content-Type', 'text/html; charset=utf-8');
				
			
 			
        if(req.headers['token']===option.acceptToken && req.method===option.method) {
            			// 验证成功
				var query = req.url.split('?')[1];
				var msg = query.split('=')[1];
console.log(query);
console.log(msg);
            	run().execute("ilang '" + msg + "'",function(){
					res.writeHead(200, { 'Content-Type': 'text/plain' });
					res.end(msg)
				})
				

        } else {
            res.writeHead(402, { 'Content-Type': 'text/plain' });
            res.end('fail');
				}
        		
        }

    }).listen(option.port);
    console.log('自动部署服务启动于：' + system + '操作系统，端口号：' + option.port);
};

init({
	url:'/speaker',
	method:'GET',
	port:9999,
	acceptToken:'abc',
	cmd:[
		'ilang "i am robot"'
	]
});