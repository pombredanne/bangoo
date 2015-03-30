angular.module('bangoo.content.edit', ['codehouse.ui'], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
})
.controller('BangooContentEditController', ['$http', '$element', function($http, $element){
    var self = this;
    this.data = {};
    this.url = $element.data('url');

    $http.get(this.url).success(function(data){
        self.data = data;
    })
}]);