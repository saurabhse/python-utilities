import cherrypy,falcon,json,os
from falcon_multipart.middleware import MultipartMiddleware
from falcon_cors import CORS

class global_error_handler(Exception):
    @staticmethod
    def handle(ex,req,resp,params):
      raise falcon.HTTPError(falcon.HTTP_506,"error",ex.message)
      
class custom_middleware(object):
  def process_request(self,req,resp):
      # do logic
      
class server(object):
  def _request_valid():
      # validate request here
  
  def on_get(self,req,resp,action):
      
      if(self._request_valid()):
        # do processing of request
        resp.status = falcon.HTTP_200
        resp.content_type = "text/html"
        resp.body = "Success"
      else:
        resp.status = falcon.HTTP_401
        resp.content_type = "text/html"
        resp.body = "Failure"
        
  def on_post(self,req,resp,action):
      if(self._request_valid()):
        # do processing of request
        resp.status = falcon.HTTP_200
        resp.content_type = "text/html"
        resp.body = "Success"
      else:
        resp.status = falcon.HTTP_401
        resp.content_type = "text/html"
        resp.body = "Failure"

cors = CORS(allow_all_origins=True)
app = falcon.API(media_type='application/json,charset=UTF-8',
                  middleware=[
                          cors.middleware,
                          custom_middleware(),
                          MultipartMiddleware()
                          ])
app.add_error_handler(global_error_handler,global_error_handler.handle)
app.add_route("/demo",server())
server_config = {
  'server.socket_host' : '0.0.0.0',
  'server.socket_port' : 8080'
  
  }

if __name__ = "main":
  cherrypy.config.update(server_config)
  cherrypy.tree.graft(app,'/')
  cherrypy.engine.start()
