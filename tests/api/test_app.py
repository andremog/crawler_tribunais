from unittest.mock import Mock, patch

from api.models import Process


def test_process_number_invalid(client):
    process_number = '2'

    r = client.get(f'/{process_number}')

    expected = {'msg': f'Número do processo {process_number} inválido'}
    assert 422 == r.status_code
    assert expected == r.json


def test_process_number_size_equal_but_invalid(client):
    process_number = 'a' * 25

    r = client.get(f'/{process_number}')

    expected = {'msg':
                f'Número do processo {process_number} inválido'}
    assert 422 == r.status_code
    assert expected == r.json


@patch('crawler.crawlers.HTMLSession')
def test_process_belongs_to_tjal(mock_session, process, client):
    process_number = '0710802-55.2018.8.02.0001'
    client.db.session.add(Process(process_number=process_number))
    client.db.session.commit()
    instance = mock_session.return_value
    html_response = Mock(html=process)
    instance.get.return_value = html_response

    r = client.get(f'/{process_number}')

    assert 200 == r.status_code


@patch('crawler.crawlers.HTMLSession')
def test_process_belongs_to_tjms(mock_session, process, client):
    process_number = '0821901-51.2018.8.12.0001'
    client.db.session.add(Process(process_number=process_number))
    client.db.session.commit()
    instance = mock_session.return_value
    html_response = Mock(html=process)
    instance.get.return_value = html_response

    r = client.get(f'/{process_number}')
    assert 200 == r.status_code
