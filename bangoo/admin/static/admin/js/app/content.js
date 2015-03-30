angular.module('bangoo.content.edit', ['codehouse.ui'], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
})
.controller('BangooContentEditController', function(){
    console.log('hello world!');
});