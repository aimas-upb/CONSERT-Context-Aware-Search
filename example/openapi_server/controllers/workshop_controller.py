import connexion
import six

from openapi_server.models.workshop import Workshop  # noqa: E501
from openapi_server import util


def workshops_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Workshop

    Gets a list of all instances of Workshop (more information in http://aimas.cs.pub.ro/robin/ontologies/2021/04/precis-schedule#Workshop) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Workshop]
    """
    return 'do some magic!'


def workshops_thingid_get(thingid):  # noqa: E501
    """Get a single Workshop by its id

    Gets the details of a given Workshop (more information in http://aimas.cs.pub.ro/robin/ontologies/2021/04/precis-schedule#Workshop) # noqa: E501

    :param thingid: The ID of the Workshop to be retrieved
    :type thingid: str

    :rtype: Workshop
    """
    return 'do some magic!'
