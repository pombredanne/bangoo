angular.module('bangoo.blog.list', ['codehouse.ui'], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
})
.controller('BangooBlogListController', ['$http', '$element', '$scope', function($http, $element, $scope){
    var self = this;
    this.url = $element.attr('url');

    $scope.posts = [];

    $http.get(this.url).success(function(data){
        self.posts = data;
    });
}]);