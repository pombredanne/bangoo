angular.module('bangoo.navigation', ["codehouse.ui"], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
})
.controller('MenuController', ['$scope', '$http', function($scope, $http){
    var self = this;
    $scope.showModal = false;

    $scope.initModal = function(){
        $scope.showModal = !$scope.showModal;
    };
}])
.controller('NewMenuController', ['$http', '$scope', '$element', function($http, $scope, $element){
    var self = this;
    this.data = {};
    this.errors = {};

    $scope.reset = function(obj){
        self.data = obj;
        self.errors = {};
    };

    this.save = function(fn){
        var url = $($element).data('action');
        $http({
            method: 'POST',
            url: url,
            data: $.param(self.data),
            xsrfHeaderName: 'X-CSRFToken',
            xsrfCookieName: 'csrftoken'
        }).error(function(retval, status, headers, config){
            self.errors = retval;
        }).success(function(retval){
            if(Object.keys(retval).length){
                fn(retval);
            }
        });
    };
}]);