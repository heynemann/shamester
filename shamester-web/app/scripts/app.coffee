'use strict'

angular.module('shamesterApp', ['ngRoute', 'ngAnimate', 'configData'])
  .config ($routeProvider, $locationProvider) ->
    $locationProvider.html5Mode(true)

    $routeProvider
      .when '/ranking',
        templateUrl: 'views/ranking.html',
        controller: 'RankingCtrl'
      .when '/',
        templateUrl: 'views/main.html'
        controller: 'MainCtrl'
      .otherwise
        redirectTo: '/'
