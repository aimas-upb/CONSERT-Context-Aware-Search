import connexion
import six

from openapi_server.models.laboratory import Laboratory  # noqa: E501
from openapi_server import util


def laboratorys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Laboratory

    Gets a list of all instances of Laboratory (more information in http://aimas.cs.pub.ro/robin/ontologies/2021/04/precis-schedule#Laboratory) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Laboratory]
    """
    return 'do some magic!'


def laboratorys_thingid_get(thingid):  # noqa: E501
    """Get a single Laboratory by its id

    Gets the details of a given Laboratory (more information in http://aimas.cs.pub.ro/robin/ontologies/2021/04/precis-schedule#Laboratory) # noqa: E501

    :param thingid: The ID of the Laboratory to be retrieved
    :type thingid: str

    :rtype: Laboratory
    """
    return 'do some magic!'
