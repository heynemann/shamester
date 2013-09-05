'use strict'

angular.module('shamesterApp')
  .controller 'RankingCtrl', ($scope) ->
    $scope.products = []

    for i in [1..50]
      $scope.products.push(
        name: 'Home Globo.com',
        url: 'http://www.globo.com',
        violations: Math.max(0, 40 - i)
      )
      $scope.products.push(
        name: 'G1',
        url: 'http://g1.globo.com',
        violations: 24
      )
      $scope.products.push(
        name: 'GloboEsporte',
        url: 'http://globoesporte.globo.com',
        violations: 42
      )

    $scope.classFor = (violations) ->
      return "success" if violations == 0
      return "error" if violations > 5
      return "warning"
