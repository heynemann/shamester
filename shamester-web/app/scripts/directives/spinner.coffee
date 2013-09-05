'use strict'

angular.module('shamesterApp')
  .directive('spinner', () ->
    scope: {}
    replace: true
    templateUrl: 'views/spinner.html'
    restrict: 'E'
  )
