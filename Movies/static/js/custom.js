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

    $scope.selectedFilterList = []
    var searchFilter = function(){
        $http({method: 'GET', url: '/filter/list/'})
            .then(function successCallback(response) {
                $scope.genreList = response.data.genreList;
                $scope.lenguageList = response.data.languageList;
            }, function errorCallback(response) {
               
            });
    }

    var init = function(){
        searchFilter()
    }
    init();

    $scope.clickFilter = function(obj){
        $scope.selectedFilterList.push(obj);
        console.log($scope.selectedFilterList)
    }


});

