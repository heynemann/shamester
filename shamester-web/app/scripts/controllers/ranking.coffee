'use strict'

angular.module('shamesterApp')
  .controller 'RankingCtrl', ($scope, $timeout) ->
    $scope.products = []
    timer = null

    $scope.classFor = (violations) ->
      return "success" if violations == 0
      return "error" if violations > 5
      return "warning"

    $scope.$watch('productName', =>
      if timer?
        $timeout.cancel(timer)
        timer = null

      $scope.hasResults = false
      timer = $timeout(=>
        @updateProducts($scope.productName)
      , 500)
    )

    @updateProducts = (name) ->
      showAll = (!name?) or name == ''

      allProducts = []
      $scope.hasResults = true

      for i in [1..50]
        allProducts.push(
          name: 'Home Globo.com',
          url: 'http://www.globo.com',
          violations: Math.max(0, 40 - i)
        ) if name == 'Home Globo.com' or showAll

        allProducts.push(
          name: 'G1',
          url: 'http://g1.globo.com',
          violations: 24
        ) if name == 'G1' or showAll

        allProducts.push(
          name: 'GloboEsporte',
          url: 'http://globoesporte.globo.com',
          violations: 42
        ) if name == 'GloboEsporte' or showAll

      $scope.products = allProducts
