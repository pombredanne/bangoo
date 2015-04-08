angular.module('bangoo.navigation', ["codehouse.ui"], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
})
.controller('MenuController', ['$scope', '$http', function($scope, $http){
    $scope.showModal = false;

    this.callback = function(data){
        // TODO: Implement dynamic menu tree redrawing
        console.log(data);
        location.reload();
    };

    $scope.initModal = function(url){
        $http.get(url).success(function(data){
            $('#newMenuForm').data('action', url);
            angular.element($('#newMenuForm')).scope().reset(data);
            $scope.showModal = !$scope.showModal;
        });
    };
}])
.controller('NewMenuController', ['$http', '$scope', '$element', function($http, $scope, $element){
    $scope.url = $($element).data('url');

    $scope.data = {};
    $scope.errors = {};

    $scope.reset = function(obj){
        $scope.data = obj;
        $scope.errors = {};
    };

    this.save = function(fn){
        var url = $($element).data('action');

        $http({
            method: 'POST',
            url: url,
            data: $scope.data,
            xsrfHeaderName: 'X-CSRFToken',
            xsrfCookieName: 'csrftoken'
        }).error(function(retval, status, headers, config){
            $scope.errors = retval;
        }).success(function(retval){
            fn(retval);
        });
    };
}]);