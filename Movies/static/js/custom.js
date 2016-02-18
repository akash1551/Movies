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
    $scope.totalItems = 64;

    $scope.currentPage = 1;

    $scope.setPage = function (pageNo) {
        $scope.currentPage = pageNo;
    };

    $scope.pageChanged = function() {
        console.log('Page changed to: ' + $scope.currentPage);
        console.log('Big Current Page: ' + $scope.bigCurrentPage);
        console.log('Big Total Items: ' + $scope.bigTotalItems);
        console.log('Max Size: ' + $scope.maxSize);
    };

    $scope.maxSize = 5;
    $scope.bigTotalItems = 2;
    $scope.bigCurrentPage = 1;

    var searchFilter = function(){
        $http({method: 'GET', url: '/filter/list/'})
            .then(function successCallback(response) {
                $scope.genreList = response.data.genreList;
                $scope.lenguageList = response.data.languageList;
            }, function errorCallback(response) {
               
            });
    }

    var getMovieList = function(){
        $http.post('/movies_by_filter/',{pageNo: $scope.currentPage, totalEntries: $scope.bigTotalItems, selectedFilterList: $scope.selectedFilterList}).
            success(function(data, status, headers, config) {
                console.log(data);
            }).
            error(function(data, status, headers, config) {
                console.log(data);
            });
    }

    var init = function(){
        searchFilter()
    }
    init();

    $scope.clickFilter = function(obj){
        var checkbox = $('#'+obj.name+"-"+obj.id);
        console.log(checkbox.is(":checked"))
        if (checkbox.is(":checked") == false){
            $scope.selectedFilterList.push(obj);
            checkbox.prop('checked', true);
            console.log($scope.selectedFilterList)
            getMovieList();
        }else{
            $scope.selectedFilterList.pop(obj);
            checkbox.prop('checked', false);
            console.log($scope.selectedFilterList)
            }
    }
        


});

