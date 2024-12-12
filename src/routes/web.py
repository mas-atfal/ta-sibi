# Coming Soon

# from src.config.routes import Route

# # Frontend Routes
# Route.group("/", "web", [
#     Route("/", "Frontend.HomeController.index"),
#     Route("/dictionaries", "Frontend.DictionaryController.index"),
#     Route("/learning", "Frontend.LearningController.index"),
#     Route("/learning/predict", "Frontend.LearningController.predict", ["POST"]),
#     Route("/articles", "Frontend.ArticleController.index"),
#     Route("/articles/<string:slug>", "Frontend.ArticleController.show"),
#     Route("/about", "Frontend.AboutController.index"),
# ])

# # Auth Routes
# Route.group("/auth", "auth", [
#     Route("/login", "Backend.AuthController.index"),
#     Route("/forgot-password", "Backend.AuthController.forgotPassword"),
#     Route("/login/doLogin", "Backend.AuthController.doLogin", ["POST"]),
#     Route("/logout", "Backend.AuthController.logout", ["POST"]),
# ])

# # Admin Routes
# Route.group("/admin", "admin", [
#     Route("/", "Backend.HomeController.index"),
# ])

# Route.group("/admin/categories", "admin_categories", [
#     Route("/", "Backend.CategoryController.index"),
#     Route("/store", "Backend.CategoryController.store", ["POST"]),
#     Route("/show/<int:id>", "Backend.CategoryController.show"),
#     Route("/update/<int:id>", "Backend.CategoryController.update", ["PATCH"]),
#     Route("/destroy/<int:id>", "Backend.CategoryController.destroy", ["DELETE"]),
# ])


from flask import Blueprint
from flask_login import login_required

from ..app.Http.Controllers.Frontend.HomeController import HomeController as FrontendHomeController
from ..app.Http.Controllers.Frontend.Vocabulary.VocabularyController import VocabularyController as FrontendVocabularyController
from ..app.Http.Controllers.Frontend.ArticleController import ArticleController as FrontendArticleController
from ..app.Http.Controllers.Frontend.LearningController import LearningController as FrontendLearningController
from ..app.Http.Controllers.Frontend.AboutController import AboutController as FrontendAboutController

from ..app.Http.Controllers.Backend.HomeController import HomeController
from ..app.Http.Controllers.Backend.CategoryController import CategoryController
from ..app.Http.Controllers.Backend.ArticleController import ArticleController
from ..app.Http.Controllers.Backend.Vocabulary.AlphabetController import AlphabetController
from ..app.Http.Controllers.Backend.Vocabulary.WordController import WordController
from ..app.Http.Controllers.Backend.Vocabulary.AffixController import AffixController
from ..app.Http.Controllers.Backend.Vocabulary.NumberController import NumberController
from ..app.Http.Controllers.Backend.AuthController import AuthController

from flask import request

bpWeb = Blueprint("web", __name__, url_prefix="/")
bpWebVocabulary = Blueprint("vocabularies", __name__, url_prefix='/vocabularies')
bpWebArticle = Blueprint("articles", __name__, url_prefix='/articles')
bpWebLearning = Blueprint("learning", __name__, url_prefix='/learning')
bpWebAbout = Blueprint("about", __name__, url_prefix='/about')

bpAuth = Blueprint("auth", __name__, url_prefix='/auth')

bpAdmin = Blueprint("admin", __name__, url_prefix='/admin')
bpAdminArticles = Blueprint("articles", __name__, url_prefix='/articles')
bpAdminCategories = Blueprint("categories", __name__, url_prefix='/categories')

# Admin Vocabularies
bpAdminVocabularies = Blueprint("vocabularies", __name__, url_prefix='/vocabularies')
bpAdminAlphabets = Blueprint("alphabets", __name__, url_prefix='/alphabets')
bpAdminWords = Blueprint("words", __name__, url_prefix='/words')
bpAdminNumbers = Blueprint("numbers", __name__, url_prefix='/numbers')
bpAdminAffixes = Blueprint("affixes", __name__, url_prefix='/affixes')

bpWeb.register_blueprint(bpWebVocabulary)
bpWeb.register_blueprint(bpWebArticle)
bpWeb.register_blueprint(bpWebLearning)
bpWeb.register_blueprint(bpWebAbout)

bpAdmin.register_blueprint(bpAdminCategories)
bpAdmin.register_blueprint(bpAdminArticles)
bpAdmin.register_blueprint(bpAdminVocabularies)

bpAdminVocabularies.register_blueprint(bpAdminAlphabets)
bpAdminVocabularies.register_blueprint(bpAdminNumbers)
bpAdminVocabularies.register_blueprint(bpAdminAffixes)
bpAdminAlphabets.register_blueprint(bpAdminWords)

# Blueprint Frontend
@bpWeb.route("/")
def index():
    return FrontendHomeController.index()

@bpWebVocabulary.route("/")
def index():
    return FrontendVocabularyController.index()

@bpWebLearning.route("/")
def index():
    return FrontendLearningController.index()

@bpWebLearning.route("/predict", methods=['POST'])
def predict():
    return FrontendLearningController.predict()

@bpWebArticle.route("/", methods=["GET"])
def index():
    return FrontendArticleController.index()

@bpWebArticle.route("/<string:slug>", methods=["GET"])
def show(slug):
    return FrontendArticleController.show(slug)

@bpWebAbout.route("/")
def index():
    return FrontendAboutController.index()

# Blueprint Auth
@bpAuth.route("/login", methods=["GET"])
def login():
    return AuthController.index()

@bpAuth.route("/login/doLogin", methods=["POST"])
def do_login():
    return AuthController.doLogin()

@bpAuth.route("/logout", methods=["POST"])
def logout():
    return AuthController.logout()

@bpAuth.route("/forgot-password", methods=["GET"])
def forgot_password():
    return AuthController.forgotPassword()

@bpAuth.route("/send-reset-password", methods=["POST"])
def send_reset_password():
    return AuthController.sendResetPassword()

@bpAuth.route("/reset-verified/<token>", methods=["POST", "GET"])
def reset_verified(token):
    if request.method == "POST":
        return AuthController.resetVerifiedPassword(token)
    else:
        return AuthController.resetVerifiedShow(token)

# Blueprint Backend

@bpAdmin.before_request
@login_required
def before_request():
    pass

@bpAdmin.route("/", methods=["GET"])
def index():
    return HomeController.index()

# Admin Categories Routes
@bpAdminCategories.route("/", methods=["GET"])
def index():
    return CategoryController.index()

@bpAdminCategories.route("/store", methods=["POST"])
def store():
    return CategoryController.store()

@bpAdminCategories.route("/show/<int:id>", methods=["GET"])
def show(id):
    return CategoryController.show(id)

@bpAdminCategories.route("/update/<int:id>", methods=["PATCH"])
def update(id):
    return CategoryController.update(id)

@bpAdminCategories.route("/destroy/<int:id>", methods=["DELETE"])
def destroy(id):
    return CategoryController.destroy(id)

# Admin Articles Routes
@bpAdminArticles.route("/", methods=["GET"])
def index():
    return ArticleController.index()

@bpAdminArticles.route("/create", methods=["GET"])
def create():
    return ArticleController.create()

@bpAdminArticles.route("/store", methods=["POST"])
def store():
    return ArticleController.store()

@bpAdminArticles.route("/<int:id>/edit", methods=["GET"])
def edit(id):
    return ArticleController.edit(id)

@bpAdminArticles.route("/<int:id>/update", methods=["PATCH"])
def update(id):
    return ArticleController.update(id)

@bpAdminArticles.route("/destroy/<int:id>", methods=["DELETE"])
def destroy(id):
    return ArticleController.destroy(id)

# Admin Alphabets Routes
@bpAdminAlphabets.route("/", methods=["GET"])
def index():
    return AlphabetController.index()

@bpAdminAlphabets.route("/store", methods=["POST"])
def store():
    return AlphabetController.store()

@bpAdminAlphabets.route("/show/<int:id>", methods=["GET"])
def show(id):
    return AlphabetController.show(id)

@bpAdminAlphabets.route("/update/<int:id>", methods=["PATCH"])
def update(id):
    return AlphabetController.update(id)

@bpAdminAlphabets.route("/destroy/<int:id>", methods=["DELETE"])
def destroy(id):
    return AlphabetController.destroy(id)

# Admin Words Routes
@bpAdminWords.route("/", methods=["GET"])
def index():
    return WordController.index()

@bpAdminWords.route("/store", methods=["POST"])
def store():
    return WordController.store()

@bpAdminWords.route("/show/<int:id>", methods=["GET"])
def show(id):
    return WordController.show(id)

@bpAdminWords.route("/update/<int:id>", methods=["PATCH"])
def update(id):
    return WordController.update(id)

@bpAdminWords.route("/destroy/<int:id>", methods=["DELETE"])
def destroy(id):
    return WordController.destroy(id)

# Admin Affixes Routes
@bpAdminAffixes.route("/", methods=["GET"])
def index():
    return AffixController.index()

@bpAdminAffixes.route("/store", methods=["POST"])
def store():
    return AffixController.store()

@bpAdminAffixes.route("/show/<int:id>", methods=["GET"])
def show(id):
    return AffixController.show(id)

@bpAdminAffixes.route("/update/<int:id>", methods=["PATCH"])
def update(id):
    return AffixController.update(id)

@bpAdminAffixes.route("/destroy/<int:id>", methods=["DELETE"])
def destroy(id):
    return AffixController.destroy(id)

# Admin Numbers Routes
@bpAdminNumbers.route("/", methods=["GET"])
def index():
    return NumberController.index()

@bpAdminNumbers.route("/store", methods=["POST"])
def store():
    return NumberController.store()

@bpAdminNumbers.route("/show/<int:id>", methods=["GET"])
def show(id):
    return NumberController.show(id)

@bpAdminNumbers.route("/update/<int:id>", methods=["PATCH"])
def update(id):
    return NumberController.update(id)

@bpAdminNumbers.route("/destroy/<int:id>", methods=["DELETE"])
def destroy(id):
    return NumberController.destroy(id)
