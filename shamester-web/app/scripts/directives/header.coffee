'use strict'

angular.module('shamesterApp')
  .directive('header', () ->
    templateUrl: 'views/header.html',
    restrict: 'E',
    scope: {},
    controller: ($scope, $location) ->
      $scope.getClass = (path) ->
        isActive = $location.path().trim() == path.trim()
        return "active" if isActive
        return "" unless isActive
  )
