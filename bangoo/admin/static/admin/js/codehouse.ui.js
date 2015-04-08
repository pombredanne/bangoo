angular.module('codehouse.ui.checkbox', [])
.controller('BsCheckboxController', ['$scope', function($scope){
    var self = this;
}])
.directive('bsCheckbox', function(){
    return {
        restrict: 'E',
        require: '^form',
        scope: {
            model: "=",
            errors: '=',
            id: '@inputid',
            help: '@',
            initial: '@',
            label: '@',
            required: '@'
        },
        controller: 'BsCheckboxController',
        template:
            '<div class="form-group" ng-class="{\'has-error\': errors.length}" id=""> ' +
                 '<label for="{{ id }}" class="control-label">{{ label }}<span class="asteriskField" ng-show="{{ required }}">*</span></label>' +
                 '<div class="controls">' +
                     '<input type="checkbox" id="{{ id }}" class="form-control" ng-model="model" nq-required="{{ required }}">' +
                     '<p id="hint_{{ id }}" class="help-block">{{ help }}</p>' +
                     '<span id="error_{{ id }}" class="help-block" ng-show="errors.length">' +
                        '<div ng-repeat="text in errors">' +
                            '<strong>{{ text }}</strong>' +
                        '</div>' +
                     '</span>' +
                '</div>' +
            '</div>',
        link: function(scope, elem, attrs, ctrl){
            if(attrs.initial !== undefined){
                scope.model = attrs.initial;
            }
        }
    };
});
angular.module('codehouse.ui.date', [])
.controller('BsDateController', ['$scope', function($scope){
    var self = this;
}])
.directive('bsDate', ['dateFormat', function(dateFormat){
    return {
        restrict: 'E',
        require: '^form',
        replace: true,
        scope: {
            model: '=',
            errors: '=',
            id: '@inputid',
            help: '@',
            initial: '@',
            label: '@',
            required: '@'
        },
        controller: 'BsDateController',
        template:
            '<div class="form-group" ng-class="{\'has-error\': errors}">' +
                 '<label for="{{ id }}" class="control-label">{{ label }}<span class="asteriskField" ng-show="{{ required }}">*</span></label>' +
                 '<div class="controls">' +
                     '<input type="text" id="{{ id }}" class="form-control" ng-model="model" nq-required="{{ required }}">' +
                     '<p id="hint_{{ id }}" class="help-block">{{ help }}</p>' +
                     '<span id="error_{{ id }}" class="help-block" ng-show="errors.length">' +
                        '<div ng-repeat="text in errors">' +
                            '<strong>{{ text }}</strong>' +
                        '</div>' +
                     '</span>' +
                '</div>' +
            '</div>',
        link : function(scope, elem, attrs, ctrl){
            $(document).ready(function () {
                var options = {};
                if(attrs.dateFormat !== undefined){
                    options.dateFormat = attrs.dateFormat;
                }
                else if(typeof dateFormat !== 'undefined'){
                    options.dateFormat = dateFormat
                }
                elem.find('input').datepicker(options);
            });
        }
    };
}]);
angular.module('codehouse.ui.input', [])
.controller('BsInputController', ['$scope', function($scope){
    var self = this;
}])
.directive('bsInput', function(){
    return {
        restrict: 'E',
        require: '^form',
        scope: {
            model: "=",
            errors: '=',
            id: '@inputid',
            help: '@',
            initial: '@',
            label: '@',
            required: '@'
        },
        controller: 'BsInputController',
        template:
            '<div class="form-group" ng-class="{\'has-error\': errors.length}" id=""> ' +
                 '<label for="{{ id }}" class="control-label">{{ label }}<span class="asteriskField" ng-show="{{ required }}">*</span></label>' +
                 '<div class="controls">' +
                     '<input type="text" id="{{ id }}" class="form-control" ng-model="model" nq-required="{{ required }}">' +
                     '<p id="hint_{{ id }}" class="help-block">{{ help }}</p>' +
                     '<span id="error_{{ id }}" class="help-block" ng-show="errors.length">' +
                        '<div ng-repeat="text in errors">' +
                            '<strong>{{ text }}</strong>' +
                        '</div>' +
                     '</span>' +
                '</div>' +
            '</div>',
        link: function(scope, elem, attrs, ctrl){
            if(attrs.initial !== undefined){
                scope.model = attrs.initial;
            }
        }
    };
});
angular.module('codehouse.ui.modal', [])
.controller('BsModalController', ['$scope', function($scope){
    var self = this;
}])
.directive('bsModal', function() {
    return {
        restrict: 'E',
        transclude: true,
        replace:true,
        scope:true,
        template: '<div class="modal fade">' +
                       '<div class="modal-dialog">' +
                            '<div class="modal-content">' +
                                 '<div class="modal-header">' +
                                      '<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button> ' +
                                      '<h4 class="modal-title">{{ title }}</h4>' +
                                 '</div>' +
                                 '<div class="modal-body" ng-transclude></div> ' +
                            '</div>' +
                        '</div>' +
                    '</div>',
        link: function postLink(scope, element, attrs) {
            scope.title = attrs.title;
            scope.$watch(attrs.visible, function(value){
                if(value == true)
                    $(element).modal('show');
                else
                    $(element).modal('hide');
            });

            $(element).on('shown.bs.modal', function(){
                scope.$apply(function(){
                    scope.$parent[attrs.visible] = true;
                });
            });

            $(element).on('hidden.bs.modal', function(){
                scope.$apply(function(){
                    scope.$parent[attrs.visible] = false;
                });
            });
        }
    };
});
angular.module('codehouse.ui.multipanel', [])
.controller('BsMultiPanelController', ['$scope', function($scope){
    var self = this;
}])
.directive('bsMultiPanel', function(){
    return {
        restrict: 'E',
        required: '^form',
        transclude: true,
        scope: {
            model: '=',
            errors: '=',
            id: '@inputid',
            help: '@',
            label: '@',
            required: '@'
        },
        controller: 'BsMultiPanelController',
        template:
            '<div class="form-group" ng-class="{\'has-error\': errors}">' +
                 '<label for="{{ id }}" class="control-label">{{ label }}<span class="asteriskField" ng-show="{{ required }}">*</span></label>' +
                 '<div class="controls">' +
                     '<select id="{{ id }}" class="select form-control" ng-model="model" multiple ng-transclude></select>' +
                     '<p id="hint_{{ id }}" class="help-block">{{ help }}</p>' +
                     '<span id="error_{{ id }}" class="help-block" ng-show="errors.length">' +
                          '<div ng-repeat="text in errors">' +
                               '<strong>{{ text }}</strong>' +
                          '</div>' +
                     '</span>' +
                '</div>' +
            '</div>',
        link: function(scope, elem, attrs, ctrl){
            var deactivateWatcher = scope.$watch('model', function(val){
                if(val !== undefined && val !== null) {
                    elem.find('select').multiSelect();
                    deactivateWatcher();
                }
            });
        }
    }
});
angular.module('codehouse.ui.number', [])
.controller('BsNumberController', ['$scope', function($scope){
    var self = this;
}])
.directive('bsNumber', function(){
    return {
        restrict: 'E',
        required: '^form',
        replace: true,
        scope: {
            model: '=',
            errors: '=',
            id: '@inputid',
            help: '@',
            initial: '@',
            label: '@',
            max: '@',
            min: '@',
            required: '@'
        },
        controller: 'BsNumberController',
        template:
            '<div class="form-group" ng-class="{\'has-error\': errors}">' +
                 '<label for="{{ id }}" class="control-label">{{ label }}<span class="asteriskField" ng-show="{{ required }}">*</span></label>' +
                 '<div class="controls">' +
                     '<input type="number" id="{{ id }}" class="form-control" ng-model="model" nq-required="{{ required }}" min="{{ min }}" max="{{ max }}">' +
                     '<p id="hint_{{ id }}" class="help-block">{{ help }}</p>' +
                     '<span id="error_{{ id }}" class="help-block" ng-show="errors.length">' +
                          '<div ng-repeat="text in errors">' +
                               '<strong>{{ text }}</strong>' +
                          '</div>' +
                     '</span>' +
                '</div>' +
            '</div>'
    }
});
angular.module('codehouse.ui.select', [])
.controller('BsSelectController', ['$scope', function($scope){
    var self = this;
}])
.directive('bsSelect', function(){
    return {
        restrict: 'E',
        required: '^form',
        transclude: true,
        scope: {
            model: '=',
            errors: '=',
            id: '@inputid',
            help: '@',
            label: '@',
            required: '@'
        },
        controller: 'BsSelectController',
        template:
            '<div class="form-group" ng-class="{\'has-error\': errors}">' +
                 '<label for="{{ id }}" class="control-label">{{ label }}<span class="asteriskField" ng-show="{{ required }}">*</span></label>' +
                 '<div class="controls">' +
                     '<select id="{{ id }}" class="select form-control" ng-model="model" ng-transclude fix></select>' +
                     '<p id="hint_{{ id }}" class="help-block">{{ help }}</p>' +
                     '<span id="error_{{ id }}" class="help-block" ng-show="errors.length">' +
                          '<div ng-repeat="text in errors">' +
                               '<strong>{{ text }}</strong>' +
                          '</div>' +
                     '</span>' +
                '</div>' +
            '</div>',
        link: function(scope, elem, attrs, ctrl) {
        }
    }
});
angular.module('codehouse.ui.select2', [])
.controller('BsSelect2Controller', ['$scope', function($scope){
    var self = this;
}])
.directive('bsSelect2', function(){
    return {
        restrict: 'E',
        require: '^form',
        transclude: true,
        scope: {
            model: '=',
            errors: '=',
            id: '@inputid',
            help: '@',
            label: '@',
            required: '@'
        },
        controller: 'BsSelect2Controller',
        template:
            '<div class="form-group" ng-class="{\'has-error\': errors}">' +
                 '<label for="{{ id }}" class="control-label">{{ label }}<span class="asteriskField" ng-show="{{ required }}">*</span></label>' +
                 '<div class="controls">' +
                     '<select id="{{ id }}" class="select form-control" ng-model="model" ng-transclude></select>' +
                     '<p id="hint_{{ id }}" class="help-block">{{ help }}</p>' +
                     '<span id="error_{{ id }}" class="help-block" ng-show="errors.length">' +
                          '<div ng-repeat="text in errors">' +
                               '<strong>{{ text }}</strong>' +
                          '</div>' +
                     '</span>' +
                '</div>' +
            '</div>',
        link : function(scope, elem, attrs, ctrl){
            if(!('initial' in attrs)){
                scope.model = elem.find('option')[0].value;
            }
            else {
                scope.model = attrs.initial;
            }
            $(document).ready(function(){
                elem.find('select').select2();
            });
        }
    };
});
angular.module('codehouse.ui.textarea', [])
.controller('BsTextareaController', ['$scope', function($scope){
    var self = this;
}])
.directive('bsTextarea', function(){
    return {
        restrict: 'E',
        required: '^form',
        replace: true,
        controller: 'BsTextareaController',
        scope: {
            model: '=',
            errors: '=',
            id: '@inputid',
            cols: '@',
            help: '@',
            initial: '@',
            label: '@',
            required: '@',
            rows: '@'
        },
        template:
            '<div class="form-group" ng-class="{\'has-error\': errors}">' +
                 '<label for="{{ id }}" class="control-label">{{ label }}<span class="asteriskField" ng-show="{{ required }}">*</span></label>' +
                 '<div class="controls">' +
                     '<textarea ng-model="model" id="{{ id }}" class="textarea form-control" cols="{{ cols }}" rows="{{ rows }}" ng-required="{{ required }}"></textarea>' +
                     '<p id="hint_{{ id }}" class="help-block">{{ help }}</p>' +
                     '<span id="error_{{ id }}" class="help-block" ng-show="errors.length">' +
                          '<div ng-repeat="text in errors">' +
                               '<strong>{{ text }}</strong>' +
                          '</div>' +
                     '</span>' +
                '</div>' +
            '</div>'
    }
});
angular.module('codehouse.ui.redactor', [])
.controller('BsRedactorController', ['$scope', function($scope){
    var self = this;
}])
.directive('bsRedactor', function(){
    return {
        restrict: 'E',
        required: '^form',
        replace: true,
        controller: 'BsRedactorController',
        scope: {
            model: '=',
            errors: '=',
            id: '@inputid',
            cols: '@',
            help: '@',
            initial: '@',
            label: '@',
            required: '@',
            rows: '@'
        },
        template:
            '<div class="form-group" ng-class="{\'has-error\': errors}">' +
                 '<label for="{{ id }}" class="control-label">{{ label }}<span class="asteriskField" ng-show="{{ required }}">*</span></label>' +
                 '<div class="controls">' +
                     '<textarea ng-model="model" id="{{ id }}" class="textarea form-control" cols="{{ cols }}" rows="{{ rows }}" ng-required="{{ required }}"></textarea>' +
                     '<p id="hint_{{ id }}" class="help-block">{{ help }}</p>' +
                     '<span id="error_{{ id }}" class="help-block" ng-show="errors.length">' +
                          '<div ng-repeat="text in errors">' +
                               '<strong>{{ text }}</strong>' +
                          '</div>' +
                     '</span>' +
                '</div>' +
            '</div>',
        link: function(scope, elem, attrs){
            var deactivateWatcher = scope.$watch('model', function(val){
                if(val !== undefined && val !== null) {
                    redactorElem.redactor('code.set', scope.model)
                }
            });

            var redactorElem = $(elem).find('textarea').redactor({
                buttonSource: true,
                paragraphize: false,
                replaceDivs: false,
                plugins: ['imagemanager'],
                changeCallback: function(){
                    scope.model = this.code.get();
                    scope.$apply();
                    deactivateWatcher();
                }
            });
        }
    }
});
angular.module('codehouse.ui', [
    'codehouse.ui.checkbox',
    'codehouse.ui.date',
    'codehouse.ui.input',
    'codehouse.ui.modal',
    'codehouse.ui.multipanel',
    'codehouse.ui.number',
    'codehouse.ui.redactor',
    'codehouse.ui.select',
    'codehouse.ui.select2',
    'codehouse.ui.textarea'
]);
