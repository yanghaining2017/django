#coding=utf-8
class UrlPathMiddleware:
    def process_request(self,request):
        #如果当前请求的路径与用户登录|注册相关|则不需要记录
        if request.path not in ['/user/register/',
                        '/user/register_check/',
                        '/user/login_check2/',
                        '/user/register_valid/',
                        '/user/login/',
                        '/user/login_handle/',
                        '/user/logout/',]:
            request.session['url_path']=request.get_full_path()
