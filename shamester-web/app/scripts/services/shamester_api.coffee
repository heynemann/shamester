'use strict'

angular.module('shamesterApp')
  .service 'ShamesterApi', (environment, api_url, $q, $resource, $http)->

    Website = $resource(api_url + 'websites/')

    return {
      addWebsite: (url) ->
        deferred = $q.defer()

        website = new Website(
          url: url
        )

        website.$save((result, putResponseHeaders) ->
          console.log(result, putResponseHeaders)
          deferred.resolve(result)
        )

        return deferred.promise
    , getHallOfShame: ->
      deferred = $q.defer()

      url = api_url + 'websites/hall'

      options =
        method: 'GET'
        url: url

      $http(options)
        .success (data, status, headers, config) ->
          deferred.resolve(
            data: data,
            status: status,
            headers: headers,
            config: config
          )
        .error (data, status, headers, config) ->

      return deferred.promise
    }
