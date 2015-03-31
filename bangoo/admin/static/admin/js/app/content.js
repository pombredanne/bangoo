angular.module('bangoo.content.edit', ['codehouse.ui'], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
})
.controller('BangooContentEditController', ['$http', '$element', function($http, $element){
    var self = this;
    this.languageCodes = ['hu', 'en'];
    this.data = {};
    this.errors = {};
    this.url = $element.data('url');

    $http.get(this.url).success(function(data){
        self.data = self.loadData(data);
    });

    this.dumpData = function(d){
        var s = d.pageSettings;
        var data = {
            allow_comments: s.allowComments,
            template_name: s.templateName,
            registration_required: s.registrationRequired,
            is_page: s.isPage,
            authors: s.authors
        };

        var translations = d.translations;
        var languages = Object.keys(translations);

        for(var i=0; i<languages.length; i++){
            var language = languages[i];
            var fields = Object.keys(translations[language]);
            for(var j=0; j<fields.length; j++){
                var field = fields[j];
                data[field + '_' + language] = translations[language][field];
            }
        }

        console.log(data);
    };

    window.dumpTest = function(){
        console.log(self.dumpData(self.data));
    };

    this.loadData = function(d){
        var translations = {};
        var fieldNames = Object.keys(d);

        for(var i=0; i<fieldNames.length; i++){
            var fieldName = fieldNames[i];
            var pieces = fieldName.split('_');

            var lastPiece = pieces[pieces.length - 1];
            if(self.languageCodes.indexOf(lastPiece) != -1){
                if(!translations.hasOwnProperty(lastPiece)){
                    translations[lastPiece] = {}
                }
                pieces.splice(-1);
                var rawFieldName = pieces.join('_');
                translations[lastPiece][rawFieldName] = d[fieldName]
            }
        }

        var data = {
            pageSettings: {
                allowComments: d.allow_comments,
                templateName: d.template_name,
                registrationRequired: d.registration_required,
                isPage: d.is_page,
                authors: d.authors
            },
            translations: translations
        };
        return data
    };
}]);