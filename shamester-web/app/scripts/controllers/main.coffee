'use strict'

angular.module('shamesterApp')
  .controller 'MainCtrl', ($scope) ->
    $scope.model = {
      url: ''
    }

    $scope.addUrl = ->
      url = $scope.model.url
      alertify.success(url + " added successfully!") if url? and url != ''
      alertify.error("URL field must be filled!") unless url? and url != ''
      $scope.model.url = ''
