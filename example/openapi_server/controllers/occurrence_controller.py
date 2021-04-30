import connexion
import six

from openapi_server.models.occurrence import Occurrence  # noqa: E501
from openapi_server import util


def occurrences_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Occurrence

    Gets a list of all instances of Occurrence (more information in http://aimas.cs.pub.ro/robin/ontologies/2021/04/precis-schedule#Occurrence) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Occurrence]
    """
    return 'do some magic!'


def occurrences_thingid_get(thingid):  # noqa: E501
    """Get a single Occurrence by its id

    Gets the details of a given Occurrence (more information in http://aimas.cs.pub.ro/robin/ontologies/2021/04/precis-schedule#Occurrence) # noqa: E501

    :param thingid: The ID of the Occurrence to be retrieved
    :type thingid: str

    :rtype: Occurrence
    """
    return 'do some magic!'
