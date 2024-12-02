from flask import Blueprint
from importlib import import_module

class Route:
    _blueprints = {}

    @classmethod
    def register(cls, app):
        """Register all blueprints with the Flask app."""
        for blueprint_name, blueprint in cls._blueprints.items():
            app.register_blueprint(blueprint)

    @classmethod
    def group(cls, prefix, blueprint_name, routes):
        """Create a group of routes under a shared prefix and blueprint."""
        blueprint = Blueprint(blueprint_name, __name__, url_prefix=prefix)
        for route in routes:
            route.add_to_blueprint(blueprint)
        cls._blueprints[blueprint_name] = blueprint

    @classmethod
    def add(cls, prefix, path, controller, methods=None):
        """Add a route to a specific prefix/blueprint."""
        if methods is None:
            methods = ["GET"]

        blueprint_name = prefix.strip("/").replace("/", "_") or "default"
        if blueprint_name not in cls._blueprints:
            cls._blueprints[blueprint_name] = Blueprint(blueprint_name, __name__, url_prefix=prefix)

        route = Route(path, controller, methods)
        route.add_to_blueprint(cls._blueprints[blueprint_name])

    def __init__(self, path, controller, methods=None):
        """Initialize a route with path, controller, and methods."""
        if methods is None:
            methods = ["GET"]

        self.path = path
        self.controller, self.action = controller.rsplit(".", 1)
        self.methods = methods

    def add_to_blueprint(self, blueprint):
        try:
            # Dynamically import the module and class
            module = import_module(f"src.app.Http.Controllers.{self.controller}")
            controller_class = getattr(module, self.controller.split('.')[-1])
            controller_instance = controller_class()  # Instantiate the controller

            # Get the action (method) from the instance
            view_func = getattr(controller_instance, self.action)

            # Generate a unique endpoint name if not provided
            endpoint = f"{blueprint.name}.{self.action}"  # e.g., "web.index"

            # Add the route to the blueprint
            blueprint.add_url_rule(self.path, endpoint=endpoint, view_func=view_func, methods=self.methods)
        except ImportError as e:
            raise ImportError(f"Failed to import module {self.controller}: {e}")
        except AttributeError as e:
            raise AttributeError(f"Class '{self.controller}' has no attribute '{self.action}': {e}")