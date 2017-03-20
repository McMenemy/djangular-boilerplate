angular.module('Synthego', ['ngMaterial'])

  .controller('SynthegoController', function ($scope, $http) {
    $http.get('http://localhost:8000/sequences/')
      .success(function (data) {
        $scope.sequences = data;
      }
    );

    $scope.clickSequence = function (id) {
      console.log(id);
    };
  });
