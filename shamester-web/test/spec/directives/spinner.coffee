'use strict'

describe 'Directive: spinner', () ->

  # load the directive's module
  beforeEach module 'shamesterApp'

  scope = {}

  beforeEach inject ($controller, $rootScope) ->
    scope = $rootScope.$new()

  it 'should make hidden element visible', inject ($compile) ->
    element = angular.element '<spinner></spinner>'
    element = $compile(element) scope
    expect(element.text()).toBe 'this is the spinner directive'
