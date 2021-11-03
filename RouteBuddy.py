
class RouteBuddy:
    
    _route_dispatcher = {}
    
    class Route:
        def __init__(self, middleware, args, mimetype, code):
            self._middleware = (
                middleware
                if type(middleware) in [list, tuple]
                else [middleware]
            )
            self._args = args
            self._mimetype = mimetype
            self._code = code

        def call(self):
            arg = self._args
            for mw in reversed(self._middleware):
                if arg is not None:
                    arg = mw(arg)
                else:
                    arg = mw()
            return self._code, self._mimetype, arg
            
    def __init__(self):
        pass

    def new_route(self, route, callback, args, mimetype, code=200):
        self._route_dispatcher[route] = self.Route(
            callback,
            args,
            mimetype,
            code)

    def dispatch(self, route):
        if route not in self._route_dispatcher:
            return 404, "text/html", self.static_document("not_found.html")
        return self._route_dispatcher[route].call()

    def static_document(self, path):
        with open(path) as f:
            contents = f.read()
        return contents
