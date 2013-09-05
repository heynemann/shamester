'use strict'

describe 'Controller: RankingCtrl', () ->

  # load the controller's module
  beforeEach module 'shamesterApp'

  RankingCtrl = {}
  scope = {}

  # Initialize the controller and a mock scope
  beforeEach inject ($controller, $rootScope) ->
    scope = $rootScope.$new()
    RankingCtrl = $controller 'RankingCtrl', {
      $scope: scope
    }

  it 'should attach a list of awesomeThings to the scope', () ->
    expect(scope.awesomeThings.length).toBe 3
