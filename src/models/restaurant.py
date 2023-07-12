class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""

        """
        Issues:
            - Palavra 'restaurante' escrita de forma errada nos dois prints;
            - No primeiro print o atributo 'cuisine_type' estava sendo impresso no lugar do nome do restaurante;
            - Existia um 'and' no primeiro print, quando o restante da mensagem está todo em PT/BR;
        Alterações:
            - Corrigido erro na palavra 'restaurante' em ambos os prints;
            - Primeiro print alterado para trazer o nome do restaurante;
            - Alterado 'and' para 'e' no primeiro print;
        """
        print(f"Esse restaurante chama {self.restaurant_name} e serve {self.cuisine_type}.")
        print(f"Esse restaurante está servindo {self.number_served} consumidores desde que está aberto.")

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""

        """
        Issues:
            - O atributo 'open' estava recebendo valor False quando a função deveria abrir o restaurante;
            - O número de clientes servidos estava recebendo o valor -2;
        Alterações:
            - Prints atribuidos a mensagens para serem retornados e usados nos testes;
            - Atribuir valor True ao atributo 'open' do objeto;
            - Atribuir valor 0 ao atributo 'number_served' do objeto;
        """

        if not self.open:
            self.open = True
            self.number_served = 0
            print(f"{self.restaurant_name} agora está aberto!")
            msg = f"{self.restaurant_name} agora está aberto!"
        else:
            print(f"{self.restaurant_name} já está aberto!")
            msg = f"{self.restaurant_name} já está aberto!"
        return msg

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""

        """
        Issues:
        
        Alterações:
            - Prints atribuidos a mensagens para serem retornados e usados nos testes;
            - Removido atribuição de 0 ao atributo 'number_served' para dá opção de obter
              o número de clientes atentidos no dia mesmo após fechamento do restaurante;
        """
        if self.open:
            self.open = False
            msg = f"{self.restaurant_name} agora está fechado!"
        else:
            msg = f"{self.restaurant_name} já está fechado!"
        return msg

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""

        """
        Issues:
            - Erro ao não passar o parametro 'total_customers'
            - Parametro 'total_customers' aceitando quantidade negativa
            - Parametro 'total_customers' aceitando valores não inteiros
        Alterações:
            - Prints atribuidos a mensagens para serem retornados e usados nos testes;
            - Adicionado validações no parametro total_customers;
        """
        is_valid, msg = self._validate_client_number(total_customers)
        if is_valid:
            if self.open:
                self.number_served = total_customers
                print(f"Total de clientes atendidos: {self.number_served}")
                msg = f"Total de clientes atendidos: {self.number_served}"
            else:
                print(f"{self.restaurant_name} está fechado!")
                msg = f"{self.restaurant_name} está fechado!"
        return msg

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""

        """
        Issues:
            - Erro ao não passar o parametro 'more_customers'
            - Parametro 'more_customers' aceitando quantidade negativa
            - Parametro 'more_customers' aceitando valores não inteiros
            - Número de clientes não estava sendo incrementado
        Alterações:
            - Prints atribuidos a mensagens para serem retornados e usados nos testes;
            - Adicionado validações no parametro more_customers;
            - Alterar quantidade de clientes para ser incrementada;
        Observação:
            - Acreditamos que não existe a necessidade desta função, já que o mesmo objetivo
              pode ser atingido através da função 'set_number_served', no entanto, alteramos
              para que funcione de forma correta. 
        """
        is_valid, msg = self._validate_client_number(more_customers)
        if is_valid:
            if self.open:
                self.number_served += more_customers
                print(f"Total de clientes atendidos: {self.number_served}")
                msg = f"Total de clientes atendidos: {self.number_served}"
            else:
                print(f"{self.restaurant_name} está fechado!")
                msg = f"{self.restaurant_name} está fechado!"
        return msg

    @staticmethod
    def _validate_client_number(client_number):
        """Função para validar do número de clientes informados nas outras funções"""

        if client_number is not None:
            if type(client_number) == int:
                if client_number >= 0:
                    return True, ''
                else:
                    msg = "Número de clientes não deve ser negativo"
                    return False, msg
            else:
                msg = "Número de clientes deve ser do tipo inteiro"
                return False, msg
        else:
            msg = "Número de clientes deve ser informado"
            return False, msg
