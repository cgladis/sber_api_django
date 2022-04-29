
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Client, ClientData


class ClientDataView:

    def getPaymentsData(self, incoming_data):
        """Returns payments associated with an account"""
        number = incoming_data[0]
        start = incoming_data[1]
        end = incoming_data[2]
        if start != None and end != None:
            payments = ClientData.objects.filter(account_id=number, type='payments',
                                                 dt__range=(start, end))
        elif start != None and end == None:
            payments = ClientData.objects.filter(account_id=number, type='payments',
                                                 dt__gt=start)
        elif start == None and end != None:
            payments = ClientData.objects.filter(account_id=number, type='payments',
                                                 dt__lt=end)
        else:
            payments = ClientData.objects.filter(account_id=number, type='payments')
        items = payments.values()
        data = {
            'count': len(items),
            'data': items
        }
        return data

    def getBillsData(self, incoming_data):
        """Returns bills associated with an account"""
        number = incoming_data[0]
        start = incoming_data[1]
        end = incoming_data[2]
        if start != None and end != None:
            charges = ClientData.objects.filter(account_id=number, type='charges',
                                                 dt__range=(start, end))
        elif start != None and end == None:
            charges = ClientData.objects.filter(account_id=number, type='charges',
                                                 dt__gt=start)
        elif start == None and end != None:
            charges = ClientData.objects.filter(account_id=number, type='charges',
                                                 dt__lt=end)
        else:
            charges = ClientData.objects.filter(account_id=number, type='charges')
        items = charges.values()
        data = {
            'count': len(items),
            'data': items
        }
        return data

    def getMeasurementsData(self, incoming_data):
        """Returns measurements associated with an account"""
        number = incoming_data[0]
        start = incoming_data[1]
        end = incoming_data[2]
        if start != None and end != None:
            measurements = ClientData.objects.filter(account_id=number, type='measurements',
                                                 dt__range=(start, end))
        elif start != None and end == None:
            measurements = ClientData.objects.filter(account_id=number, type='measurements',
                                                 dt__gt=start)
        elif start == None and end != None:
            measurements = ClientData.objects.filter(account_id=number, type='measurements',
                                                 dt__lt=end)
        else:
            measurements = ClientData.objects.filter(account_id=number, type='measurements')
        items = measurements.values()
        data = {  # собираем данные для ответа
            'count': len(items),
            'data': items
        }
        return data

    def post(self, request, id, type):
        if (id == 0):  # Пустой ответ при client id == 0
            return Response([], status=status.HTTP_200_OK)

        try:
            if request.user.is_superuser:  # Выборка объектов по клиенту
                client = Client.objects.get(pk=id)  # Если admin отбор только по clientID
            else:
                client = Client.objects.get(pk=id, user=request.user)  # иначе отбор по clientID & currentUser

            number = client.account_id
            if not number:  # Пустой ответ если у clientID нет accountID
                response = Response([], status=status.HTTP_200_OK)
                return response

            incoming_data = [  # формируем список параметров ???
                number,
                request.POST.get('start', None),
                request.POST.get('end', None)
            ]

            if type == 'payments':
                result = self.getPaymentsData(incoming_data)
            elif type == 'charges':
                result = self.getBillsData(incoming_data)
            elif type == 'measurements':
                result = self.getMeasurementsData(incoming_data)
            else:  # возвращаем пустой ответ если type другой
                response = Response([], status=status.HTTP_200_OK)
                return response

            data = {  # собираем данные для ответа
                'count': result['count'],
                'data': result['data']
            }

            response = Response(data, status=status.HTTP_200_OK)

        # добавим обработку остальных исключений
        except Exception as ex:
            response = Response([{'error': f"Error {str(ex)}"}], status=status.HTTP_200_OK)

        return response

    @staticmethod
    @api_view(['POST'])
    def run_post(request, id, type):
        new_obj = ClientDataView()
        return new_obj.post(request, id, type)
