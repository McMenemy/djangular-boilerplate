retail
    .controller('RetailController', function($scope, Sequence, Chain, Store, Employee) {
        Sequence.query().$promise.then(function(data) {
          $scope.sequences = data;
        });
        Chain.query().$promise.then(function(data) {
            $scope.chains = data;
        });
        Store.query().$promise.then(function(data) {
            $scope.stores = data;
        });
        Employee.query().$promise.then(function(data) {
            $scope.employees = data;
        });
});
