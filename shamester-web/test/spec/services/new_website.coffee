'use strict'

describe 'Service: NewWebsite', () ->

  # load the service's module
  beforeEach module 'shamesterApp'

  # instantiate service
  NewWebsite = {}
  beforeEach inject (_NewWebsite_) ->
    NewWebsite = _NewWebsite_

  it 'should do something', () ->
    expect(!!NewWebsite).toBe true
