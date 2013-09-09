'use strict'

angular.module('shamesterApp')
  .controller 'MainCtrl', ($scope, ShamesterApi) ->
    $scope.creatingWebsite = false

    $scope.model = {
      url: ''
    }

    $scope.addUrl = ->
      return if $scope.creatingWebsite

      url = $scope.model.url
      alertify.error("URL field must be filled!") unless url? and url != ''

      if url? and url != ''
        $scope.creatingWebsite = true
        create = ShamesterApi.addWebsite(url)

        create.then((result) ->
          $scope.creatingWebsite = false
          alertify.success(url + " added successfully!") if result.success
          alertify.error(url + " could not be added!\n" + result.reason) unless result.success
          $scope.model.url = ''
        )
