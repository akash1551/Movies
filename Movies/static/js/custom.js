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

    $scope.recordNotFound = '';

    $scope.maxSize = 5;
    $scope.bigTotalItems = 2;
    $scope.bigCurrentPage = 1;
    $scope.itemPerPage = 10;

    var getMovieList = function(){
        $http.post('/movies_by_filter/',{pageNo: $scope.bigCurrentPage, itemPerPage: $scope.itemPerPage, selectedFilterList: $scope.selectedFilterList}).
            success(function(data, status, headers, config) {
                if (data.status){
                    console.log(data);
                    $scope.movieList = data.movieList;
                    $scope.bigTotalItems = data.totalEntries;
                    $scope.bigCurrentPage = data.pageNo;
                    console.log('Big Current Page: ' + $scope.bigCurrentPage);
                    console.log('Big Total Items: ' + $scope.bigTotalItems);
                    console.log('Max Size: ' + $scope.maxSize);
                }else{
                    $scope.recordNotFound = data.validation;
                    $scope.movieList = []
                }
            }).
            error(function(data, status, headers, config) {
                console.log(data);
            });
    }

    $scope.pageChanged = function() {
        console.log('Big Current Page: ' + $scope.bigCurrentPage);
        console.log('Big Total Items: ' + $scope.bigTotalItems);
        console.log('Max Size: ' + $scope.maxSize);
        getMovieList();
    };

    var searchFilter = function(){
        $http({method: 'GET', url: '/filter/list/'})
            .then(function successCallback(response) {
                $scope.genreList = response.data.genreList;
                $scope.lenguageList = response.data.languageList;
                $scope.sortByList = response.data.sortByList;
            }, function errorCallback(response) {
               
            });
    }

    var init = function(){
        searchFilter();
        getMovieList();
    }
    init();

    $scope.clickFilter = function(obj){
        obj.isSelected=!obj.isSelected;
        console.log(obj.isSelected)
        if (obj.isSelected){
            $scope.selectedFilterList.push(obj);
            console.log($scope.selectedFilterList)
            getMovieList();
        }else{
            $scope.selectedFilterList.pop(obj);
            console.log($scope.selectedFilterList)
            getMovieList();
            }
    }
        


});

