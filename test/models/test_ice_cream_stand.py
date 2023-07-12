from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    def test_flavors_available_success(self):
        # Setup
        error_msg = 'Não foi possível listar os sabores'
        restaurant_name = 'Sorveteria do João'.title()
        cuisine_type = 'Sorvete'
        flavor_list = ['morango', 'chocolate']
        resultado_esperado = "No momento temos os seguintes sabores de sorvete disponíveis:-morango-chocolate"

        service = IceCreamStand(restaurant_name, cuisine_type, flavor_list)

        # Chamada
        resultado = service.flavors_available()

        # Avaliacao
        assert resultado_esperado == resultado, error_msg

    def test_flavors_available_no_stock(self):
        # Setup
        error_msg = 'Não foi possível listar os sabores'
        restaurant_name = 'Sorveteria do João'.title()
        cuisine_type = 'Sorvete'
        flavor_list = list()
        resultado_esperado = "Estamos sem estoque atualmente!"

        service = IceCreamStand(restaurant_name, cuisine_type, flavor_list)

        # Chamada
        resultado = service.flavors_available()

        # Avaliacao
        assert resultado_esperado == resultado, error_msg

    def test_find_flavor_success(self):
        # Setup
        error_msg = 'Não foi possível encontrar o sabor desejado'
        restaurant_name = 'Sorveteria do João'.title()
        cuisine_type = 'Sorvete'
        flavor = 'morango'
        flavor_list = ['morango', 'chocolate']
        resultado_esperado = f"Temos no momento {flavor}!"

        service = IceCreamStand(restaurant_name, cuisine_type, flavor_list)

        # Chamada
        resultado = service.find_flavor(flavor=flavor)

        # Avaliacao
        assert resultado_esperado == resultado, error_msg

    def test_find_flavor_fail(self):
        # Setup
        error_msg = 'Não foi possível encontrar o sabor desejado'
        restaurant_name = 'Sorveteria do João'.title()
        cuisine_type = 'Sorvete'
        flavor = 'baunilha'
        flavor_list = ['morango', 'chocolate']
        resultado_esperado = f"Não temos no momento {flavor}!"

        service = IceCreamStand(restaurant_name, cuisine_type, flavor_list)

        # Chamada
        resultado = service.find_flavor(flavor=flavor)

        # Avaliacao
        assert resultado_esperado == resultado, error_msg

    def test_find_flavor_no_stock(self):
        # Setup
        error_msg = 'Não foi possível encontrar o sabor desejado'
        restaurant_name = 'Sorveteria do João'.title()
        cuisine_type = 'Sorvete'
        flavor = 'baunilha'
        flavor_list = list()
        resultado_esperado = "Estamos sem estoque atualmente!"

        service = IceCreamStand(restaurant_name, cuisine_type, flavor_list)

        # Chamada
        resultado = service.find_flavor(flavor=flavor)

        # Avaliacao
        assert resultado_esperado == resultado, error_msg

    def test_add_flavor_success(self):
        # Setup
        error_msg = 'Não foi possível adicionar o sabor desejado'
        restaurant_name = 'Sorveteria do João'.title()
        cuisine_type = 'Sorvete'
        flavor = 'baunilha'
        flavor_list = list()
        resultado_esperado = f"{flavor} adicionado ao estoque!"

        service = IceCreamStand(restaurant_name, cuisine_type, flavor_list)

        # Chamada
        resultado = service.add_flavor(flavor=flavor)

        # Avaliacao
        assert resultado_esperado == resultado, error_msg

    def test_add_flavor_fail(self):
        # Setup
        error_msg = 'Não foi possível adicionar o sabor desejado'
        restaurant_name = 'Sorveteria do João'.title()
        cuisine_type = 'Sorvete'
        flavor = 'baunilha'
        flavor_list = ['baunilha', 'morango', 'chocolate']
        resultado_esperado = "Sabor já disponivel!"

        service = IceCreamStand(restaurant_name, cuisine_type, flavor_list)

        # Chamada
        resultado = service.add_flavor(flavor=flavor)

        # Avaliacao
        assert resultado_esperado == resultado, error_msg

    def test_add_flavor_flavor_none(self):
        # Setup
        error_msg = 'Não foi possível adicionar o sabor desejado'
        restaurant_name = 'Sorveteria do João'.title()
        cuisine_type = 'Sorvete'
        flavor = None
        flavor_list = ['baunilha', 'morango', 'chocolate']
        resultado_esperado = "Sabor deve ser informado"

        service = IceCreamStand(restaurant_name, cuisine_type, flavor_list)

        # Chamada
        resultado = service.add_flavor(flavor=flavor)

        # Avaliacao
        assert resultado_esperado == resultado, error_msg

    def test_add_flavor_flavor_not_valid(self):
        # Setup
        error_msg = 'Não foi possível adicionar o sabor desejado'
        restaurant_name = 'Sorveteria do João'.title()
        cuisine_type = 'Sorvete'
        flavor = 33.5
        flavor_list = ['baunilha', 'morango', 'chocolate']
        resultado_esperado = "Sabor deve ser do tipo string"

        service = IceCreamStand(restaurant_name, cuisine_type, flavor_list)

        # Chamada
        resultado = service.add_flavor(flavor=flavor)

        # Avaliacao
        assert resultado_esperado == resultado, error_msg
