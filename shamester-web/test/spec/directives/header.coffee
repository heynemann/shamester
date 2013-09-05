'use strict'

describe("Unit: Testing Directives", ->
  elm = null
  scope = null
  linkFn = null

  beforeEach module 'views/header.html'
  beforeEach module 'shamesterApp'

  beforeEach inject(($rootScope, $compile) ->
    elm = angular.element('<header></header>')
    scope = $rootScope
    $compile(elm)(scope)
    scope.$digest()
    elm
  )

  it('should contain the text', ->
    inject(($controller) ->
      #scope.$broadcast('addProductData',{title:"TEST DISPLAY NAME", 
                                    #productId: "123", mainImageUrl: "TEST.JPG"});
      #scope.$digest();
      expect(elm.text().trim()).toBe("this is the header directive")
    )
  )
)

#describe 'Directive: header', () ->
  #element = null

  ## load the directive's module
  #beforeEach module 'shamesterApp'

  #beforeEach inject ($controller, $rootScope, $compile, $httpBackend) ->
    #$httpBackend.whenGET('views/header.html').respond('this is the header directive'); 

    #element = angular.element '<header></header>'
    #scope = $rootScope
    #compileFn = $compile(element)
    #scope.$digest()
    #elment = compileFn(scope)

  #it 'should make hidden element visible', inject ($compile) ->
    #expect(element.html()).toBe 'this is the header directive'
