from src.models.restaurant import Restaurant


class TestRestaurant:

    def test_describe_restaurant(self, capsys):
        """
        Teste usando capsys para capturar o print da função e comparar o resultado.
        Apenas este teste foi feito desta forma, conforme informado no README.md
        """
        # Setup
        error_msg = 'Descrição impressa diferente do esperado'
        restaurant_name = 'Sorveteria do João'.title()
        cuisine_type = 'Sorvete'
        number_served = 0
        resultado_esperado = f"Esse restaurante chama {restaurant_name} e serve {cuisine_type}.\n" \
                             f"Esse restaurante está servindo {number_served} consumidores desde que está aberto.\n"

        service = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        service.describe_restaurant()
        resultado, _ = capsys.readouterr()

        # Avaliacao
        assert resultado_esperado == resultado, error_msg

    def test_open_restaurant_success(self):
        # Setup
        error_msg = 'Não foi possível abrir o restaurante'
        restaurant_name = 'Sorveteria do João'.title()
        cuisine_type = 'Sorvete'
        resultado_esperado = f"{restaurant_name} agora está aberto!"

        service = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = service.open_restaurant()

        # Avaliacao
        assert resultado_esperado == resultado, error_msg

    def test_open_restaurant_fail(self):
        # Setup
        error_msg = 'Não foi possível abrir o restaurante'
        restaurant_name = 'Sorveteria do João'.title()
        cuisine_type = 'Sorvete'
        resultado_esperado = f"{restaurant_name} já está aberto!"

        service = Restaurant(restaurant_name, cuisine_type)
        service.open_restaurant()

        # Chamada
        resultado = service.open_restaurant()

        # Avaliacao
        assert resultado_esperado == resultado, error_msg

    def test_close_restaurant_success(self):
        # Setup
        error_msg = 'Não foi possível fechar o restaurante'
        restaurant_name = 'Sorveteria do João'.title()
        cuisine_type = 'Sorvete'
        resultado_esperado = f"{restaurant_name} agora está fechado!"

        service = Restaurant(restaurant_name, cuisine_type)
        service.open_restaurant()

        # Chamada
        resultado = service.close_restaurant()

        # Avaliacao
        assert resultado_esperado == resultado, error_msg

    def test_close_restaurant_fail(self):
        # Setup
        error_msg = 'Não foi possível fechar o restaurante'
        restaurant_name = 'Sorveteria do João'.title()
        cuisine_type = 'Sorvete'
        resultado_esperado = f"{restaurant_name} já está fechado!"

        service = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = service.close_restaurant()

        # Avaliacao
        assert resultado_esperado == resultado, error_msg

    def test_set_number_served_success(self):
        # Setup
        error_msg = 'Não foi possível alterar o número de pessoas atendidas'
        restaurant_name = 'Sorveteria do João'.title()
        cuisine_type = 'Sorvete'
        number_served = 5
        resultado_esperado = f"Total de clientes atendidos: {number_served}"

        service = Restaurant(restaurant_name, cuisine_type)
        service.open_restaurant()

        # Chamada
        resultado = service.set_number_served(total_customers=number_served)

        # Avaliacao
        assert resultado_esperado == resultado, error_msg

    def test_set_number_served_closed(self):
        # Setup
        error_msg = 'Não foi possível alterar o número de pessoas atendidas'
        restaurant_name = 'Sorveteria do João'.title()
        cuisine_type = 'Sorvete'
        number_served = 5
        resultado_esperado = f"{restaurant_name} está fechado!"

        service = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = service.set_number_served(total_customers=number_served)

        # Avaliacao
        assert resultado_esperado == resultado, error_msg

    def test_increment_number_served_success(self):
        # Setup
        error_msg = 'Não foi possível incrementar o número de pessoas atendidas'
        restaurant_name = 'Sorveteria do João'.title()
        cuisine_type = 'Sorvete'
        number_served = 5
        resultado_esperado = f"Total de clientes atendidos: {number_served}"

        service = Restaurant(restaurant_name, cuisine_type)
        service.open_restaurant()

        # Chamada
        resultado = service.increment_number_served(more_customers=number_served)

        # Avaliacao
        assert resultado_esperado == resultado, error_msg

    def test_increment_number_served_closed(self):
        # Setup
        error_msg = 'Não foi possível incrementar o número de pessoas atendidas'
        restaurant_name = 'Sorveteria do João'.title()
        cuisine_type = 'Sorvete'
        number_served = 5
        resultado_esperado = f"{restaurant_name} está fechado!"

        service = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = service.increment_number_served(more_customers=number_served)

        # Avaliacao
        assert resultado_esperado == resultado, error_msg

    def test_increment_number_served_none(self):
        # Setup
        error_msg = 'Não foi possível incrementar o número de pessoas atendidas'
        restaurant_name = 'Sorveteria do João'.title()
        cuisine_type = 'Sorvete'
        number_served = None
        resultado_esperado = "Número de clientes deve ser informado"

        service = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = service.increment_number_served(more_customers=number_served)

        # Avaliacao
        assert resultado_esperado == resultado, error_msg

    def test_increment_number_served_negative(self):
        # Setup
        error_msg = 'Não foi possível incrementar o número de pessoas atendidas'
        restaurant_name = 'Sorveteria do João'.title()
        cuisine_type = 'Sorvete'
        number_served = -3
        resultado_esperado = "Número de clientes não deve ser negativo"

        service = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = service.increment_number_served(more_customers=number_served)

        # Avaliacao
        assert resultado_esperado == resultado, error_msg

    def test_increment_number_served_not_int(self):
        # Setup
        error_msg = 'Não foi possível incrementar o número de pessoas atendidas'
        restaurant_name = 'Sorveteria do João'.title()
        cuisine_type = 'Sorvete'
        number_served = 'cinco'
        resultado_esperado = "Número de clientes deve ser do tipo inteiro"

        service = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = service.increment_number_served(more_customers=number_served)

        # Avaliacao
        assert resultado_esperado == resultado, error_msg
