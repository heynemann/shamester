'use strict'

describe 'Controller: RankingCtrl', () ->

  # load the controller's module
  beforeEach module 'shamesterApp'
  beforeEach module 'ngRoute'

  RankingCtrl = {}
  scope = {}

  # Initialize the controller and a mock scope
  beforeEach inject ($controller, $rootScope) ->
    scope = $rootScope.$new()
    RankingCtrl = $controller 'RankingCtrl', {
      $scope: scope
    }

  it 'should have 150 items by default', () ->
    RankingCtrl.updateProducts()
    expect(scope.products.length).toBe 150

  it 'should have G1 items when filtered', () ->
    RankingCtrl.updateProducts('G1')
    expect(scope.products.length).toBe 50
    expect(scope.products[0].name).toBe "G1"
