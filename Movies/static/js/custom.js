$(document).ready(function() {
    var listClass='list-group-item';    
    $('#list').click(function(event){
        event.preventDefault();
        $('#products .item').addClass(listClass);    
    });
    $('#grid').click(function(event){
        event.preventDefault();
        $('#products .item')
            .removeClass(listClass)
            .addClass('grid-group-item');        
    });
});

angular.module("movieApp", ['ui.bootstrap'])
.controller("movieCtrl", function($scope,$http){

    var init = function(){

    }
    init();

    $scope.filterList = []

    $scope.clickFilter = function(obj){
        $scope.filterList.push(obj);
        console.log($scope.filterList)
    }


});

