angular.module('bangoo.content.edit', ['codehouse.ui'], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
})
.controller('BangooContentEditController', ['$http', '$element', '$scope', function($http, $element, $scope){
    var self = this;
    this.data = {};
    this.errors = {};
    this.url = $element.attr('action');

    $http.get(this.url).success(function(data){
        self.data = data;
    });

    this.submit = function(e){
        e.preventDefault();
        $http({
            method: 'POST',
            url: self.url,
            data: self.data,
            xsrfHeaderName: 'X-CSRFToken',
            xsrfCookieName: 'csrftoken'
        }).success(function(){
            $('.top-right').notify({
                type: 'success',
                message: { text: 'Content updated!' },
                fadeOut: { enabled: true, delay: 5000 }
            }).show();
            self.errors = {};
        }).error(function(retval, status, headers, config){
            if(status !== 500){
                self.errors = retval;
            }
            else {
                $('.top-right').notify({
                    type: 'danger',
                    message: {text: 'Unexpected error happened!'},
                    fadeOut: {enabled: true, delay: 5000}
                }).show();
            }
        });
    }
}]);