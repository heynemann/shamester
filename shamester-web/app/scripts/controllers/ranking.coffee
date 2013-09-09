'use strict'

angular.module('shamesterApp')
  .controller 'RankingCtrl', ($scope, ShamesterApi) ->
    $scope.products = []

    $scope.classFor = (violations) ->
      return "success" if violations == 0
      return "error" if violations > 5
      return "warning"

    $scope.updateProducts = ->
      hall = ShamesterApi.getHallOfShame()

      hall.then((result) ->
        $scope.hasResults = result.data.length > 0
        $scope.products = result.data
      )

    #$scope.updateProducts()
