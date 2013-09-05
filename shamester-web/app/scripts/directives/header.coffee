'use strict'

angular.module('shamesterApp')
  .directive('header', () ->
    templateUrl: 'views/header.html',
    restrict: 'E'
  )
