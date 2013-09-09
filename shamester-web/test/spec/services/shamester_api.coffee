'use strict'

describe 'Service: shamesterApi', () ->

  # load the service's module
  beforeEach module 'shamesterApp'

  # instantiate service
  shamesterApi = {}
  beforeEach inject (_shamesterApi_) ->
    shamesterApi = _shamesterApi_

  it 'should do something', () ->
    expect(!!shamesterApi).toBe true
