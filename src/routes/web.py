from flask import Blueprint, g

from ..app.Http.Controllers.Frontend.HomeController import HomeController as FrontendHomeController
from ..app.Http.Controllers.Frontend.DictionaryController import DictionaryController as FrontendDictionaryController
from ..app.Http.Controllers.Frontend.ArticleController import ArticleController as FrontendArticleController
from ..app.Http.Controllers.Frontend.LearningController import LearningController as FrontendLearningController
from ..app.Http.Controllers.Frontend.AboutController import AboutController as FrontendAboutController

from ..app.Http.Controllers.Backend.HomeController import HomeController
from ..app.Http.Controllers.Backend.CategoryController import CategoryController
from ..app.Http.Controllers.Backend.ArticleController import ArticleController
from ..app.Http.Controllers.Backend.DictionaryController import DictionaryController
from ..app.Http.Controllers.Backend.AuthController import AuthController

bpWeb = Blueprint("web", __name__, url_prefix="/")
bpWebDictionary = Blueprint("dictionaries", __name__, url_prefix='/dictionaries')
bpWebArticle = Blueprint("articles", __name__, url_prefix='/articles')
bpWebLearning = Blueprint("learning", __name__, url_prefix='/learning')
bpWebAbout = Blueprint("about", __name__, url_prefix='/about')

bpAuth = Blueprint("auth", __name__, url_prefix='/auth')

bpAdmin = Blueprint("admin", __name__, url_prefix='/admin')
bpAdminArticles = Blueprint("articles", __name__, url_prefix='/articles')
bpAdminCategories = Blueprint("categories", __name__, url_prefix='/categories')
bpAdminDictionaries = Blueprint("dictionaries", __name__, url_prefix='/dictionaries')

bpWeb.register_blueprint(bpWebDictionary)
bpWeb.register_blueprint(bpWebArticle)
bpWeb.register_blueprint(bpWebLearning)
bpWeb.register_blueprint(bpWebAbout)

bpAdmin.register_blueprint(bpAdminCategories)
bpAdmin.register_blueprint(bpAdminArticles)
bpAdmin.register_blueprint(bpAdminDictionaries)

# Blueprint Frontend
@bpWeb.route("/")
def index():
    return FrontendHomeController.index()

@bpWebDictionary.route("/")
def index():
    return FrontendDictionaryController.index()

@bpWebLearning.route("/")
def index():
    return FrontendLearningController.index()

@bpWebArticle.route("/")
def index():
    return FrontendArticleController.index()

@bpWebAbout.route("/")
def index():
    return FrontendAboutController.index()

# Blueprint Auth
@bpAuth.route("/login", methods=["GET"])
def index():
    return AuthController.index()

@bpAuth.route("/login/doLogin", methods=["POST"])
def login():
    return AuthController.doLogin()

# Blueprint Backend
@bpAdmin.route("/")
def index():
    return HomeController.index()

@bpAdminCategories.route("/")
def index():
    return CategoryController.index()

@bpAdminCategories.route("/store", methods=["POST"])
def store():
    return CategoryController.store()

@bpAdminArticles.route("/")
def index():
    return ArticleController.index()
@bpAdminArticles.route("/create")
def create():
    return ArticleController.create()
@bpAdminArticles.route("/<int:id>/edit")
def edit(id):
    return ArticleController.edit(id)

@bpAdminDictionaries.route("/")
def index():
    return DictionaryController.index()

