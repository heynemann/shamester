'use strict'

angular.module('shamesterApp', ['ngRoute', 'ngAnimate'])
  .config ($routeProvider, $locationProvider) ->
    $routeProvider
      .when '/ranking',
        templateUrl: 'views/ranking.html',
        controller: 'RankingCtrl'
      .when '/',
        templateUrl: 'views/main.html'
        controller: 'MainCtrl'
      .otherwise
        redirectTo: '/'
