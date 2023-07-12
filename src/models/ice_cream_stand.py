from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""

        """
        Issues:
        Alterações:
            - Prints atribuidos a mensagens para serem retornados e usados nos testes;
        """
        if self.flavors:
            print("\nNo momento temos os seguintes sabores de sorvete disponíveis:")
            msg = "No momento temos os seguintes sabores de sorvete disponíveis:"
            for flavor in self.flavors:
                print(f"\t-{flavor}")
                msg += f"-{flavor}"
        else:
            print("Estamos sem estoque atualmente!")
            msg = "Estamos sem estoque atualmente!"
        return msg

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""

        """
        Issues:
            - A lista de sabores estava sendo exibida nos prints;
            - Erro ao não passar o parametro 'flavor';
            - Parametro 'flavor' aceitando valores não string;
        Alterações:
            - Prints atribuidos a mensagens para serem retornados e usados nos testes;
            - Exibir somente o sabor buscado nos prints;
        """
        is_valid, msg = self._validate_flavor(flavor)
        if is_valid:
            if self.flavors:
                if flavor in self.flavors:
                    print(f"Temos no momento {flavor}!")
                    msg = f"Temos no momento {flavor}!"
                else:
                    print(f"Não temos no momento {flavor}!")
                    msg = f"Não temos no momento {flavor}!"
            else:
                print("Estamos sem estoque atualmente!")
                msg = "Estamos sem estoque atualmente!"
        return msg

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""

        """
        Issues:
            - Não é necessário verificar se o estoque está vazio ao adicionar um sabor;
            - Erro ao não passar o parametro 'flavor';
            - Parametro 'flavor' aceitando valores não string;
        Alterações:
            - Prints atribuidos a mensagens para serem retornados e usados nos testes;
            - Remover verificação de estoque vazio;
        """
        is_valid, msg = self._validate_flavor(flavor)
        if is_valid:
            if flavor in self.flavors:
                print("\nSabor já disponivel!")
                msg = "Sabor já disponivel!"
            else:
                self.flavors.append(flavor)
                print(f"{flavor} adicionado ao estoque!")
                msg = f"{flavor} adicionado ao estoque!"
        return msg

    @staticmethod
    def _validate_flavor(flavor):
        """Função para validar o parametro sabor informados nas outras funções"""

        if flavor is not None:
            if type(flavor) == str:
                return True, ''
            else:
                msg = "Sabor deve ser do tipo string"
                return False, msg
        else:
            msg = "Sabor deve ser informado"
            return False, msg
