/**
 * ���tweets���ڣ�����֮ǰ�����ģ����ʾÿһ��΢���������õ�eval������json����ģ����@֮������ݾ��Ƕ����·����ƴ���Ժ�����tweets[i].screen_name�����ر�html����http response��
 */

var http=require('http'),
    tweets = null,
    template = '<p><em>@user.screen_name</em><img src="@user.profile_image_url" /> <span>@text</span><p>';

(function(){
	  http.createClient(80, 'api.t.sina.com.cn')
	      .request('GET', '/statuses/public_timeline.json?source=3243248798', {'host': 'api.t.sina.com.cn'})
	      .addListener('response', function(response){
	         var result = '';
	         response.addListener('data',function(data){
	            result += data
	         })
	         .addListener('end',function(){
	            tweets = JSON.parse(result)
	         })
	      })
	      .end();
	  setTimeout(arguments.callee, 5000);
} )()

http.createServer(function(req,res){
  res.writeHeader(200, {'Content-Type':'text/html; charset=utf-8'});
  res.write('<!docytype html><html><body>');
  if(tweets && tweets.length){
     for(var i = 0; i<tweets.length; i++){        
        var itm = template.replace(/@([\w\.]+)/g, function(){ return eval('tweets[i].'+arguments[1]) });
        res.write(itm);
     }
  }  
  res.end('</body></html>')
}).listen(8080);




