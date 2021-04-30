import connexion
import six

from openapi_server.models.person import Person  # noqa: E501
from openapi_server import util


def persons_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Person

    Gets a list of all instances of Person (more information in http://aimas.cs.pub.ro/robin/ontologies/2021/04/precis-schedule#Person) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Person]
    """
    return 'do some magic!'


def persons_thingid_get(thingid):  # noqa: E501
    """Get a single Person by its id

    Gets the details of a given Person (more information in http://aimas.cs.pub.ro/robin/ontologies/2021/04/precis-schedule#Person) # noqa: E501

    :param thingid: The ID of the Person to be retrieved
    :type thingid: str

    :rtype: Person
    """
    return 'do some magic!'
