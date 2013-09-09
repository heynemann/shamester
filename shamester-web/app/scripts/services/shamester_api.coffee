'use strict'

angular.module('shamesterApp')
  .service 'ShamesterApi', (environment, $q, $timeout)->
    return {
      createWebsite: (url) ->
        deferred = $q.defer()

        $timeout(->
          deferred.resolve({
            status: "success"
          })
        , 5000)

        return deferred.promise
    }
