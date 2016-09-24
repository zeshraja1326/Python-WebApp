angular.module('RADapp', ['ngMaterial']);
var app = angular.module('RADapp');
var serverURL = 'http://127.0.0.1:5000'

app.controller("AppCTRL", function ($scope, $http, $mdToast) {

    $http.get(serverURL + "/API/Tests")
        .success(function (data, status) {
            $scope.tests = data.tests;
        })
        .error(function (response, status) {
            $mdToast.show(
                $mdToast.simple()
                .textContent("Can't load tests :(")
                .position('bottom right')
                .hideDelay(3000)
            );
        });

    $scope.deleteTest = function (id, index) {
        $http.delete(serverURL + "/API/Tests?id=" + id)
            .success(function (data, status) {
                $scope.tests.splice(index, 1);
            })
            .error(function (response, status) {
                alert("No permission to do that/server errors");
            });
    };


    $scope.newTest = function () {
        $http.post(serverURL + '/API/Tests', {
                "title": $scope.test_title
            })
            .success(function (data, status) {
                $scope.tests.push({
                    title: $scope.test_title,
                    id: data.created_id
                });
            })
            .error(function (response, status) {
                $mdToast.show(
                    $mdToast.simple()
                    .textContent('Change Name, or it will not work!')
                    .position('bottom right')
                    .hideDelay(3000)
                );
            });
    };

    $scope.editVisual = function (id, title) {
        $scope.test_title = title;
        $scope.test_id = id;
    };

    $scope.updateTest = function () {
        $http.put(serverURL + '/API/Tests?id=' + $scope.test_id, {
                "title": $scope.test_title
            })
            .success(function (data, status) {
                $mdToast.show(
                    $mdToast.simple()
                    .textContent('Reload Page to see changes!')
                    .position('bottom right')
                    .hideDelay(3000)
                );
            })
            .error(function (response, status) {
                alert('Something goes wrong');
            });
    };

});