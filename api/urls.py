from django.urls import include, path
from .controllers import AccountController, LoginView, LogoutView, GetUserView, UpdateUser, SearchUserView, DeleteUser, CreateProfile, ViewProfile, SearchProfile, DeleteProfile, AddMovie, DeleteMovie, SearchMovie, UpdateMovie, ViewAllMovie, AddCinemaRoom, ViewAllCinemaRoom, DeleteCinemaRoom, UpdateCinemaRoom, DeleteMovieSession, AddMovieSession, ViewAllMovieSession, HelperFunction, AddFnbs, ViewAllFnbs, UpdateFnbs, DeleteFnbs, AddBooking, ViewAllBooking

urlpatterns = [
    # Account
    path('', AccountController.getUserAccount),
    path('add/', AccountController.RegisterAccount, name='add'),

    # Log in/out
    path('login/', LoginView.login, name='login'),
    path('logout/', LogoutView.logout, name='logout'),
    path('getUser/', GetUserView.getUser, name="getUser"),

    # Account management
    #path('suspendUser/', UpdateUser.suspendUser, name='suspendUser'),
    #path('reactivateUser/', UpdateUser.reactivateUser, name='reactivateUser'),
    #path('changePW/', UpdateUser.changePassword, name='changePassword'),
    #path('changeEmail/', UpdateUser.changeEmail, name='changeEmail'),
    path('deleteUser/', DeleteUser.deleteUser, name='deleteUser'),
    path('updateUser/', UpdateUser.updateUser, name='updateUser'),
    path('searchUser/', SearchUserView.searchUser, name='searchUser'),

    #Profile management
    path('createProfile/', CreateProfile.createProfile, name='createProfile'),
    path('viewProfile/', ViewProfile.viewProfile, name='viewProfile'),
    path('searchProfile/', SearchProfile.searchProfile, name='searchProfile'),
    path('deleteProfile/', DeleteProfile.deleteProfile, name='deleteProfile'),

    # Movie management
    path('addMov/', AddMovie.addMov, name='addMov'),
    path('delMov/', DeleteMovie.delMov, name='delMov'),
    path('searchMovie/', SearchMovie.SearchMov, name='SearchMovie'),
    path('updateMovie/', UpdateMovie.updateMov, name='updateMov'),
    path('viewMov/', ViewAllMovie.viewAllMovie, name='viewMov'),

    # Cinema room management
    path('addCR/', AddCinemaRoom.addCR, name='addCR'),
    path('viewAllCR/', ViewAllCinemaRoom.viewAllCR, name='viewAllCR'),
    path('updateCR/', UpdateCinemaRoom.updateCR, name='updateCR'),
    path('delCR/', DeleteCinemaRoom.delCR, name='delCR'),

    # Movie session management
    path('addMS/', AddMovieSession.addMS, name='addMS'),
    path('viewAllMS/', ViewAllMovieSession.viewAllMS, name='viewAllMS'),
    path('delMS/', DeleteMovieSession.delMS, name='delMS'),
    path('getMovieSession/', HelperFunction.getMovieSession, name='getMovieSession'),

    # Fnb management
    path('addFnb/', AddFnbs.addFnb, name='addFnb'),
    path('viewAllFnb/', ViewAllFnbs.viewAllFnb, name='viewAllFnb'),
    path('updateFnB/', UpdateFnbs.updateFnB, name='updateFnb'),
    path('delFnB/', DeleteFnbs.delFnB, name='delFnb'),

    # Purchase booking                                                                                      
    path('addBook/', AddBooking.addBook, name='addBook'),
    path('viewAllBook/', ViewAllBooking.viewAllBook, name='viewAllBook'),

    #helper function
    path('viewUpcoming/', HelperFunction.getUpComing),
    path('viewNowShowing/', HelperFunction.getNowShowing)
]