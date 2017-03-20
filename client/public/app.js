angular.module('Synthego', ['ngMaterial'])

  .controller('SynthegoController', function ($scope, $http, $mdDialog) {
    // initial defaults
    $scope.sequences = [];
    $scope.selectedSeq = { name: '', owner: '', design: '', description: '', formatted: '' };
    $scope.newSeq = { name: '', owner: '', design: '', description: '', formatted: '' };
    $scope.status = '';
    $scope.addStatus = '';

    $http.get('http://localhost:8000/sequences/')
      .success(function (data) {
        $scope.sequences = data;
      }
    );

    $scope.clickSequence = function (ev, id, index) {
      $scope.selectedSeq = { design: '', description: '', formatted: '' };
      $scope.status = '';
      $http.get('http://localhost:8000/detailed-sequences/' + id + '/')
        .success(function (data) {
          $scope.selectedSeq = data;
          $scope.selectedIndex = index;
          $mdDialog.show({
            contentElement: '#modal',
            parent: angular.element(document.body),
            targetEvent: ev,
            clickOutsideToClose: true
          });
        }
      );
    };

    $scope.updateSequence = function (id) {
      $scope.status = '';
      $http.patch('http://localhost:8000/detailed-sequences/' + id + '/', $scope.selectedSeq)
        .success(function (data) {
          $scope.selectedSeq = data;
          $scope.sequences[$scope.selectedIndex] = data;
          $scope.status = 'Success!';
        })
        .error(function (data) {
          console.log(data);
          $scope.status = 'Error: ' + JSON.stringify(data).slice(0, 200);
        });
    };

    $scope.addSequence = function () {
      $scope.addStatus = '';
      console.log($scope.newSeq);
      $http.post('http://localhost:8000/detailed-sequences/', $scope.newSeq)
        .success(function (data) {
          $scope.newSeq = { design: '', description: '', owner: '', name: '' };
          $scope.sequences.push(data);
          $scope.addStatus = 'Success!';
        })
        .error(function (data) {
          console.log(data);
          $scope.addStatus = 'Error: ' + JSON.stringify(data).slice(0, 200);
        });
    };

    $scope.clearForm = function () {
      $scope.newSeq = { design: '', description: '', owner: '', name: '' };
    };

    $scope.hideModal = function () {
      $mdDialog.hide();
    };
  });
